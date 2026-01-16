# Simple Log Parser
# This script prints only the log entries that contain errors.

logs = [
    "INFO: System running normally",
    "ERROR: Disk space low",
    "INFO: Backup completed",
    "ERROR: Unauthorized access attempt"
]

def find_errors(log_list):
    for entry in log_list:
        if "ERROR" in entry:
            print("Found error:", entry)

find_errors(logs)
