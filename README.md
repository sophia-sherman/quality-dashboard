# Quality Dashboard

Display quality metrics, meant to replace filling this confluence page in by hand: https://confluence.cambiahealth.com/confluence/display/SEAM/Sprint+Quality+Metrics

## Set up dev environment
Add a `.env` file with the following environment variables:
```
JIRA_USERNAME
JIRA_PASSWORD
JIRA_SERVER_URL
```

Install dependencies:
`pip3 install -r requirements.txt`

Run the script:
`python3 quality-dashboard/jira_issues.py`