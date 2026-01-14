# FishForYou Global Services  
## Linux Forensics Investigation: Suspicious User Activity

**Analyst:** Kyrian  
**Date:** [10/12/2025]  
**System Investigated:** `srv-web-02.fishforyou.local`  
**OS:** Ubuntu Server 20.04  
**Severity:** Medium  
**Status:** Resolved  

---

## 1. Executive Summary

On [09/01/2025], unusual activity was detected on the FishForYou Global Services web server (`srv-web-02`). The SIEM flagged multiple failed SSH login attempts followed by a successful login from an IP address not associated with internal operations.  

A forensic review of authentication logs, bash history, and system processes confirmed that the attacker gained access using a weak password but did not escalate privileges or modify system files. The account was disabled, and the server was secured.

---

## 2. Incident Description

- **Alert Source:** SIEM (SSH brute-force detection)  
- **Target System:** Public-facing web server  
- **Suspicious Activity:**  
  - Repeated failed SSH logins  
  - Successful login from foreign IP  
  - Unusual commands executed shortly after login  
- **Affected Account:** `backup-admin` (non-MFA, weak password)  

---

## 3. Initial Forensic Questions

- Who logged in and from where  
- What commands were executed  
- Were any files modified  
- Was privilege escalation attempted  
- Was malware or persistence installed  

---

## 4. Log Analysis

### **4.1 Authentication Logs (`/var/log/auth.log`)**

Key findings:Jan 12 03:14:22 srv-web-02 sshd[1245]: Failed password for backup-admin from 185.203.112.77 port 49822 ssh2 Jan 12 03:14:23 srv-web-02 sshd[1245]: Failed password for backup-admin from 185.203.112.77 port 49822 ssh2 Jan 12 03:14:29 srv-web-02 sshd[1245]: Accepted password for backup-admin from 185.203.112.77 port 49822 ssh2

- **27 failed attempts**, followed by **1 successful login**  
- Source IP not associated with FishForYou operations  
- Login occurred outside normal working hours  

---

### **4.2 Bash History (`/home/backup-admin/.bash_history`)**

Commands executed:whoami uname -a ls -la /var/www/ cat /etc/passwd

Interpretation:
- Attacker was performing **reconnaissance**  
- No destructive or privilege escalation commands found  
- No attempts to install tools or modify system files  

---

### **4.3 Running Processes (`ps aux`)**

Suspicious processes checked:

- No unknown processes  
- No reverse shells  
- No crypto-mining activity  
- No persistent services created  

---

### **4.4 File Integrity Check**

Commands used:sudo find /var/www -mtime -1 sudo diff -r /etc /backup/etc

Findings:
- No recent modifications to web files  
- No changes to `/etc/passwd`, `/etc/shadow`, or cron jobs  

---

## 5. Indicators of Compromise (IOCs)

- **Source IP:** `185.203.112.77`  
- **User Account:** `backup-admin`  
- **Commands Executed:** Basic reconnaissance  
- **Login Time:** 03:14 GMT (outside business hours)  

---

## 6. Impact Assessment

- **Data Exposure:** None  
- **Privilege Escalation:** None  
- **File Modification:** None  
- **Operational Impact:** Low  
- **Risk Level:** Medium (due to unauthorized access)  

---

## 7. Containment & Mitigation

- Disabled the `backup-admin` account  
- Reset all privileged account passwords  
- Enforced MFA for all SSH users  
- Blocked the malicious IP at the firewall  
- Implemented fail2ban to limit SSH attempts  
- Reviewed and hardened SSH configuration:  
  - Disabled password authentication  
  - Enabled key-based authentication only  
  - Restricted SSH access to internal IPs  

---

## 8. Recommendations

- Conduct a full credential audit  
- Enforce strong password policies  
- Implement centralized logging for all Linux servers  
- Schedule regular file integrity monitoring  
- Perform quarterly SSH hardening reviews  
- Train administrators on secure account management  

---

## 9. Lessons Learned

- Weak passwords remain a major attack vector  
- MFA would have prevented this incident entirely  
- Continuous log monitoring is essential for early detection  
- Public-facing servers require strict hardening and regular audits  

---

## 10. Conclusion

The attacker gained access to a FishForYou Global Services web server using a weak password but did not escalate privileges or modify system files. The incident was contained quickly, and additional security controls were implemented to prevent recurrence.

---
