import os
import argparse
import jira
from dotenv import load_dotenv
load_dotenv()

JIRA_USERNAME = os.environ.get("JIRA_USERNAME")
JIRA_PASSWORD = os.environ.get("JIRA_PASSWORD")
JIRA_SERVER_URL = os.environ.get("JIRA_SERVER_URL")

auth_jira = jira.JIRA(basic_auth=(JIRA_USERNAME, JIRA_PASSWORD), options={'server': JIRA_SERVER_URL})

def initialize_parser():
    parser = argparse.ArgumentParser(description='Setting parameters for your jira queries')
    parser.add_argument("--project", required=True, help="Specify the JIRA project")
    parser.add_argument("--sprint-start", help="Date format YYYY-MM-DD of sprint start")
    parser.add_argument("--sprint-end", help="Date format YYYY-MM-DD of sprint end")
    return parser

def count_open_critical_major_issues(project):
    try:
        open_critical_major_jql = f'project = {project} AND issuetype = Bug AND (priority = Critical OR priority = Major) AND status != Closed'
        return count_issues(open_critical_major_jql)
    except jira.exceptions.JIRAError as error:
        print(f"\nCheck your JQL syntax: {error}\n")


def count_open_regression_issues(project):
    try:
        open_regression_jql = f'project = {project} AND issuetype = "CCS Incident" AND status != Closed'
        return count_issues(open_regression_jql)
    except jira.exceptions.JIRAError as error:
        print(f"\nCheck your JQL syntax: {error}\n")


def count_open_data_issues(project):
    try:
        open_data_issues_jql = f'project = {project} AND status !=  Closed AND labels = data-quality-impact'
        return count_issues(open_data_issues_jql)
    except jira.exceptions.JIRAError as error:
        print(f"\nCheck your JQL syntax: {error}\n")


def count_open_issues(project):
    try:
        open_issues_jql = f'project = {project} AND issuetype = Bug AND status != Closed'
        return count_issues(open_issues_jql)
    except jira.exceptions.JIRAError as error:
        print(f"\nCheck your JQL syntax: {error}\n")


def count_opened_issues_in_sprint(project, sprint_start, sprint_end):
    try:
        opened_issues_jql = f'project = {project} AND issuetype = Bug AND created >= {sprint_start} AND created <= {sprint_end}'
        return count_issues(opened_issues_jql)
    except jira.exceptions.JIRAError as error:
        print(f"\nCheck your JQL syntax: {error}\n")


def count_closed_issues_in_sprint(project, sprint_start, sprint_end):
    try:
        closed_issues_jql = f'project = {project} AND issuetype = Bug AND status = Closed AND resolved >= {sprint_start} AND resolved <= {sprint_end}'
        return count_issues(closed_issues_jql)
    except jira.exceptions.JIRAError as error:
        print(f"\nCheck your JQL syntax: {error}\n")


def count_issues(jql):
    issues = auth_jira.search_issues(jql, fields=['key'])
    return issues.total


def collect_jira_data(args):
    project = args.project  # i.e. SEAM

    print("Open Issues: {0}".format(count_open_issues(project)))
    print("Open Critical Major Issues: {0}".format(count_open_critical_major_issues(project)))
    print("Open Regression Issues: {0}".format(count_open_regression_issues(project)))
    print("Open Data Issues: {0}".format(count_open_data_issues(project)))

    if args.sprint_start and args.sprint_end:
        sprint_start = args.sprint_start
        sprint_end = args.sprint_end
        print("Open Issues This Sprint: {0}".format(count_opened_issues_in_sprint(project, sprint_start, sprint_end)))
        print("Closed Issues This Sprint: {0}".format(count_closed_issues_in_sprint(project, sprint_start, sprint_end)))
    elif args.sprint_start or args.sprint_end:
        print("\nYou have only selected one sprint date, but you must add a date range" \
              "to see open and closed issues for the sprint. Use the --help option to learn more.\n")


if __name__ == "__main__":
    parser = initialize_parser()
    args = parser.parse_args()
    collect_jira_data(args)
