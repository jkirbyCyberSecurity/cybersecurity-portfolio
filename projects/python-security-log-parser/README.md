# Python Security Log Parser

## Overview

A beginner cybersecurity project written in Python that scans text-based log files for entries containing ERROR, FAILED, or CRITICAL. Matching entries are written to a separate alert report.

This project demonstrates Python file handling, string matching, command-line arguments, error handling, and basic security log analysis.

## Features

- Reads a text log file.
- Searches case-insensitively for ERROR, FAILED, and CRITICAL.
- Writes matching entries to an alert report.
- Reports the number of lines examined and alerts found.
- Accepts a custom input filename and optional output filename.
- Handles missing or unreadable input files with an error message and nonzero exit status.

## Requirements

- Python 3
- A terminal or command-line environment
- No third-party Python packages required

## Usage

Run the parser with the included sample:

    python log_parser.py sample.log

Specify another input file:

    python log_parser.py path/to/application.log

Choose a custom report filename:

    python log_parser.py sample.log --output test-report.txt

The default output filename is alerts.txt.

## Sample Test Results

The included fictional sample log contains six entries, three of which match the configured keywords.

Expected summary:

    Lines examined: 6
    Alerts found: 3

A missing-file test using `python log_parser.py missing.log` should display an error and return exit status 1.

## Scope and Limitations

This is an educational log-filtering tool, not a complete security monitoring or intrusion detection system.

It flags matching keywords; it does not determine whether an event is malicious, correlate events, or detect every security incident. It can produce false positives and miss relevant events that do not contain the configured keywords.

Use fictional, sanitized, or authorized logs. Never publish passwords, access tokens, personal information, or confidential production logs.

## Learning Outcomes

- Reading and processing text files with Python.
- Searching strings without case sensitivity.
- Writing alert reports.
- Handling file errors.
- Accepting command-line arguments.
- Testing with sample data.
- Documenting a security tool for a public portfolio.

## Project Status

Tested with a fictional six-line sample log and a missing-file scenario. Results apply to those tests only.
