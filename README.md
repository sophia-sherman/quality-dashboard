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

The script uses `argparse` to parse command line arguments. Use the `--help` option to view the menu of how to use the `jira_issues.py` script:

`python3 dashboard/jira_issues.py --help`

You must pass in the following command line options to run the script properly:

```
--project <Jira project name>
--sprint_start <sprint start date format YYYY-MM-DD>
--sprint_end <sprint end date format YYYY-MM-DD>
```

Here's an example of a valid command:

`python3 dashboard/jira_issues.py --project SEAM --sprint-start 2020-03-04 --sprint-end 2020-03-18`