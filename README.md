# Quality Dashboard

Display quality metrics, meant to replace filling this confluence page in by hand: https://confluence.cambiahealth.com/confluence/display/SEAM/Sprint+Quality+Metrics

So far, only functionality to automate running jira queries has been implemented.

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

To minimally run the script, specify a jira project name:

`python3 dashboard/jira_issues.py --project SEAM`

Additional optional options:

```
--sprint-start <sprint start date format YYYY-MM-DD>
--sprint-end <sprint end date format YYYY-MM-DD>
--release-version <release version format major.minor.patch>
```

Here are some example of valid commands:

`python3 dashboard/jira_issues.py --project SEAM --sprint-start 2020-03-04 --sprint-end 2020-03-18`
`python3 dashboard/jira_issues.py --project SEAM --sprint-start 2020-03-04 --sprint-end 2020-03-18 --release-version 1.7.0`

## Run unit tests

Make sure all unit tests pass before committing code:

`pytest`