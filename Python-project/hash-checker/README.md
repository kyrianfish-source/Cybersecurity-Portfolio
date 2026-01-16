# File Hash Checker

## Purpose
This script calculates the SHA-256 hash of a file and compares it to a known good hash to verify file integrity.

## Python Concepts Used
- Functions
- Loops (reading file blocks)
- Conditionals
- Hashing with `hashlib`

## How It Works
The script reads a file in small blocks and updates a SHA-256 hash object.  
It then compares the calculated hash to a known hash value.

## Example Output
Calculated Hash: 5d41402abc4b2a76b9719d911017c592 File integrity verified

## What I Learned
- How hashing works in cybersecurity  
- How to read files in binary mode  
- How to compare values to check integrity  
