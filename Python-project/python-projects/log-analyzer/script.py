# Login Attempt Analyzer
# This script checks a list of login attempts and prints warnings for failed attempts.

login_attempts = [
    "Success from 10.0.0.5",
    "Failed from 185.203.112.77",
    "Failed from 185.203.112.77",
    "Success from 10.0.0.8"
]

for attempt in login_attempts:
    if "Failed" in attempt:
        print("Suspicious login detected:", attempt)
