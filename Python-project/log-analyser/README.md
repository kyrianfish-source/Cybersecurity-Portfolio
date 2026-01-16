# Login Attempt Analyzer

## Purpose
This script analyzes a list of login attempts and prints a warning whenever a failed login is detected. It simulates how a SOC analyst might review authentication logs.

## Python Concepts Used
- Loops (`for`)
- Conditionals (`if`)
- Basic string matching

## How It Works
The script loops through each login attempt in a list.  
If the word **"Failed"** appears in the entry, it prints a warning message.

## Example Output
Suspicious login detected: Failed from 185.203.112.77 Suspicious login detected: Failed from 185.203.112.77

## What I Learned
- How to loop through lists in Python  
- How to use conditionals to filter data  
- How to simulate simple log analysis  
