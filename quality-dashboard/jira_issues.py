import os
from jira import JIRA
from dotenv import load_dotenv
load_dotenv()

JIRA_USERNAME = os.environ.get("JIRA_USERNAME")
JIRA_PASSWORD = os.environ.get("JIRA_PASSWORD")
JIRA_SERVER_URL = os.environ.get("JIRA_SERVER_URL")

auth_jira = JIRA(basic_auth=(JIRA_USERNAME, JIRA_PASSWORD), options={'server': JIRA_SERVER_URL})

def count_open_critical_major_issues(project):
    # open_critical_major_jql = 'project in ("CCS Janus Platform", "Product: Janus Platform", "Product: Seamless UX", "Product: Journi") AND issuetype = Bug AND status not in (closed, resolved, Done, "PO Approval", Approved) AND priority in (Blocker, Critical, Major) AND resolution = Unresolved'
    open_critical_major_jql = f'project = {project} AND issuetype = Bug AND (priority = Critical OR priority = Major) AND ' \
                              'status != Closed'
    return count_issues(open_critical_major_jql)


def count_open_regression_issues(project):
    # open_regression_jql = 'project in ("CCS Janus Platform",  "Product: Janus Platform", "Product: Journi", "Product: Seamless UX")  AND status not in (closed, resolved, Done, "PO Approval", Approved) AND ((issuetype = Bug AND "Regression Item?" = Yes) OR issuetype = "CCS Incident" ) AND resolution = Unresolved'
    open_regression_jql = f'project = {project} AND issuetype = "CCS Incident" AND status != Closed'
    return count_issues(open_regression_jql)


def count_open_data_issues(project):
    # open_data_issues_jql = 'project in ("Product: Seamless UX", "Product: Journi") AND labels = data-quality-impact AND resolution = Unresolved'
    open_data_issues_jql = f'project = {project} AND status !=  Closed AND labels = data-quality-impact'
    return count_issues(open_data_issues_jql)


def count_open_issues(project):
    # open_issues_jql = 'project in ("Product: Seamless UX", "Product: Journi") AND issuetype = Bug AND status not in (closed, resolved, Done, "PO Approval", Approved) AND resolution = Unresolved'
    open_issues_jql = f'project = {project} AND issuetype = Bug AND status != Closed'
    return count_issues(open_issues_jql)


def count_opened_issues_in_sprint(project):
    opened_issues_jql = f'project = {project} AND issuetype = Bug AND created >= 2019-10-30 AND created <= 2019-11-13'
    return count_issues(opened_issues_jql)


def count_closed_issues_in_sprint(project):
    closed_issues_jql = f'project = {project} AND issuetype = Bug AND status = Closed AND resolved >= 2019-10-30 AND resolved <= 2019-11-13'
    return count_issues(closed_issues_jql)


def count_issues(jql):
    issues = auth_jira.search_issues(jql, fields=['key'])
    return issues.total


def collect_jira_data(project):
    print("Open Issues: {0}".format(count_open_issues(project)))
    print("Open Critical Major Issues: {0}".format(count_open_critical_major_issues(project)))
    print("Open Regression Issues: {0}".format(count_open_regression_issues(project)))
    print("Open Data Issues: {0}".format(count_open_data_issues(project)))
    print("Open Issues This Sprint: {0}".format(count_opened_issues_in_sprint(project)))
    print("Closed Issues This Sprint: {0}".format(count_closed_issues_in_sprint(project)))


if __name__ == "__main__":
    collect_jira_data("SEAM")