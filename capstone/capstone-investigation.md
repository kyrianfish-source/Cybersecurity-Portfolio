# FishForYou Global Services  
## Capstone Security Investigation  
**Incident Type:** Unauthorized Access Attempt  
**Analyst:** Kyrian  
**Date:** [07/01/2026]  
**Status:** Closed  

---

## 1. Executive Summary

On [06/01/2026], FishForYou Global Services detected suspicious activity involving unauthorized access attempts on the company’s internal customer management system (CMS). The SIEM generated multiple alerts indicating failed login attempts followed by a successful login from an IP address outside the company’s normal operating region.

A full investigation was conducted, including log analysis, user activity review, network traffic inspection, and system integrity checks. The investigation confirmed that the attacker gained access using compromised credentials but did not escalate privileges or exfiltrate data. Immediate containment actions were taken, and long‑term security improvements were implemented.

---

## 2. Incident Description

- **System Affected:** Customer Management System (CMS)  
- **User Account Compromised:** `jens.olsen@fishforyou.com`  
- **Initial Detection:** SIEM alert for unusual login location  
- **Attack Vector:** Credential compromise (likely phishing)  
- **Impact:** Unauthorized access to internal CMS  
- **Severity:** High  

The attacker logged in from an IP address located in Eastern Europe, which is outside FishForYou’s operational regions.

---

## 3. Timeline of Events

| Time (CET) | Event |
|-----------|-------|
| 02:11 | 14 failed login attempts detected |
| 02:13 | Successful login from foreign IP |
| 02:14 | SIEM triggers “Impossible Travel” alert |
| 02:16 | SOC begins investigation |
| 02:22 | Account disabled |
| 02:30 | Firewall blocks malicious IP |
| 03:00 | Full log review initiated |
| 04:15 | No data exfiltration detected |
| 05:00 | Incident contained |

---

## 4. Indicators of Compromise (IOCs)

- **Source IP:** `193.56.112.44`  
- **User Agent:** Unknown browser version  
- **Login Location:** Eastern Europe  
- **Unusual Activity:**  
  - Access to customer records outside normal working hours  
  - Attempted export of customer list (blocked by DLP)  

---

## 5. Investigation Steps

### **5.1 Authentication Log Review**
Reviewed `/var/log/auth.log` and SIEM authentication events.

Findings:
- 14 failed login attempts  
- 1 successful login  
- Login occurred at 02:13 CET (employee was offline)  

### **5.2 CMS Application Logs**
Reviewed access logs for suspicious actions.

Findings:
- Attacker viewed 12 customer profiles  
- Attempted CSV export (blocked by DLP)  
- No privilege escalation attempts  

### **5.3 Network Traffic Analysis**
Inspected outbound traffic for anomalies.

Findings:
- No large data transfers  
- No connections to known malicious domains  
- No signs of malware or command‑and‑control activity  

### **5.4 Endpoint Review**
Checked the employee’s workstation.

Findings:
- No malware detected  
- Browser history showed a phishing email link clicked 3 days earlier  
- Employee reported receiving a fake “password reset” email  

### **5.5 Integrity Checks**
- No system files modified  
- No new user accounts created  
- No persistence mechanisms installed  

---

## 6. Root Cause Analysis

**Root Cause:**  
The attacker gained access using stolen credentials obtained through a phishing email that mimicked FishForYou’s IT Support team.

**Contributing Factors:**  
- Employee did not report the phishing email  
- MFA was not enabled for CMS access  
- Password complexity was insufficient  

---

## 7. Impact Assessment

- **Data Exposure:** None (viewed but not exfiltrated)  
- **System Compromise:** Limited to one user account  
- **Operational Impact:** Low  
- **Reputational Risk:** Moderate  
- **Overall Severity:** High (due to unauthorized access)  

---

## 8. Containment Actions

- Disabled compromised account  
- Forced password reset for all CMS users  
- Blocked malicious IP at firewall  
- Enabled MFA for CMS access  
- Updated SIEM rules for early detection  
- Conducted phishing awareness refresher training  

---

## 9. Recommendations

### **Technical Controls**
- Enforce MFA across all systems  
- Strengthen password policy  
- Implement automated phishing detection  
- Enable geo‑blocking for high‑risk regions  
- Improve DLP rules for sensitive data exports  

### **User Awareness**
- Conduct quarterly phishing simulations  
- Provide targeted training for high‑risk departments  
- Encourage immediate reporting of suspicious emails  

### **Process Improvements**
- Review access logs weekly  
- Implement least‑privilege access for CMS  
- Maintain updated asset inventory  

---

## 10. Lessons Learned

- MFA would have prevented the compromise entirely  
- Early SIEM detection reduced the impact  
- Employee awareness remains a critical security layer  
- DLP controls successfully blocked data exfiltration  

---

## 11. Conclusion

The incident was contained quickly, and no customer data was exfiltrated. The investigation confirmed that the attacker gained access through compromised credentials obtained via phishing. FishForYou Global Services has implemented stronger authentication controls, improved monitoring, and enhanced employee awareness to prevent similar incidents in the future.

---
