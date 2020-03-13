import pytest
from dashboard import jira_issues

class TestJiraIssues:
    def test_count_open_critical_major_issues(self):
        actual_count = jira_issues.count_open_critical_major_issues("SEAM")
        assert actual_count is not None

    def test_count_open_regression_issues(self):
        actual_count = jira_issues.count_open_regression_issues("SEAM")
        assert actual_count is not None

    def test_count_open_data_issues(self):
        actual_count = jira_issues.count_open_data_issues("SEAM")
        assert actual_count is not None

    def test_count_open_issues(self):
        actual_count = jira_issues.count_open_issues("SEAM")
        assert actual_count is not None

    def test_count_opened_issues_in_sprint(self):
        actual_count = jira_issues.count_opened_issues_in_sprint("SEAM", "2019-10-30", "2019-11-13")
        assert actual_count is not None

    def test_count_closed_issues_in_sprint(self):
        actual_count = jira_issues.count_closed_issues_in_sprint("SEAM", "2019-10-30", "2019-11-13")
        assert actual_count is not None

    def test_count_opened_issues_for_release(self):
        actual_count = jira_issues.count_opened_issues_for_release("SEAM", "1.7.0")
        assert actual_count is not None

    def test_count_closed_issues_for_release(self):
        actual_count = jira_issues.count_closed_issues_for_release("SEAM", "1.7.0")
        assert actual_count is not None

    def test_count_open_issues_targeted_for_release(self):
        actual_count = jira_issues.count_open_issues_targeted_for_release("SEAM", "1.7.0")
        assert actual_count is not None

    def test_count_issues(self):
        jql = open_issues_jql = f'project = SEAM AND issuetype = Bug AND status != Closed'
        actual_count = jira_issues.count_issues(jql)
        assert actual_count is not None
