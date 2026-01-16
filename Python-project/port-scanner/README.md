# Simple Port Scanner

## Purpose
This script scans a list of common ports on a target system and reports whether each port is open or closed.

## Python Concepts Used
- Loops
- Conditionals
- Basic networking with `socket` library
- Iteration through lists

## How It Works
The script attempts to connect to each port in a list.  
If the connection succeeds, the port is open.  
If it fails, the port is closed.

## Example Output
Port 22 is CLOSED 
Port 80 is OPEN 
Port 443 is OPEN 
Port 3306 is CLOSED

## What I Learned
- How to use Python’s `socket` library  
- How to test network ports  
- How to loop through lists and evaluate results  
