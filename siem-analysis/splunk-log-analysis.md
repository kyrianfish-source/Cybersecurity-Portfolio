# FishForYou Global Services  
## SIEM Log Analysis: Suspicious Login Activity

**Analyst:** Kyrian  
**Date:** 13/01/2026  
**Department:** Security Operations  
**Tool Used:** Splunk (conceptual)  
**Incident Type:** Suspicious Authentication Activity  
**Severity:** Medium  
**Status:** Resolved  

---

## 1. Executive Summary

On 13/01/2026, the SIEM platform generated multiple alerts related to failed login attempts targeting an employee account belonging to the Sales Department. The activity originated from an IP address outside FishForYou’s normal geographic operating regions.  

Further analysis revealed a pattern consistent with a brute-force attempt. No successful login occurred, and the source IP was blocked at the firewall. This report documents the investigation steps, findings, and recommended actions.

---

## 2. Alert Details

- **Alert Name:** Excessive Failed Login Attempts  
- **Triggered By:** Authentication logs (Windows AD)  
- **Threshold:** >10 failed attempts within 5 minutes  
- **Affected Account:** `sarah.madsen@fishforyou.com`  
- **Source IP:** `185.203.112.77` (unrecognized foreign IP)  
- **Time Window:** 02:14–02:19 CET  

---

## 3. Initial SIEM Query

A Splunk-style query used to investigate the event:index=auth_logs sourcetype=windows:security (user="sarah.madsen") EventCode=4625 | stats count by user, src_ip, _time | sort - count

This query returned **27 failed login attempts** within a 5‑minute window.

---

## 4. Investigation Steps

1. **Reviewed authentication logs** to confirm repeated failed attempts.  
2. **Checked geolocation** of the source IP — identified as outside Denmark and unrelated to FishForYou operations.  
3. **Searched for successful logins** from the same IP — none found.  
4. **Correlated events** with VPN logs — no VPN activity associated with the account.  
5. **Checked for password reset attempts** — none initiated.  
6. **Verified account owner’s activity** — employee was offline during the event.  
7. **Checked for similar attempts** on other accounts — no additional anomalies detected.  
8. **Blocked the source IP** at the firewall.  
9. **Forced a password reset** for the affected account as a precaution.  

---

## 5. Findings

- The pattern of repeated failed logins indicates a **brute-force attempt**.  
- The source IP has no legitimate connection to FishForYou Global Services.  
- No successful authentication occurred.  
- No lateral movement or additional suspicious activity was detected.  
- The employee’s account remained secure.  

---

## 6. Impact Assessment

- **Data Exposure:** None  
- **System Compromise:** None  
- **Operational Impact:** Low  
- **Reputational Risk:** Low  
- **Likelihood of Recurrence:** Moderate  

---

## 7. Containment & Mitigation Actions

- Blocked the malicious IP at the firewall.  
- Enforced password reset for the targeted account.  
- Increased monitoring for similar login patterns.  
- Added new detection rules for repeated failed logins from foreign IPs.  
- Notified the employee and provided security awareness guidance.  

---

## 8. Recommendations

- Implement account lockout after a defined number of failed attempts.  
- Enforce MFA (Multi-Factor Authentication) for all employee accounts.  
- Strengthen password complexity requirements.  
- Expand SIEM detection rules to include:  
  - Impossible travel logins  
  - Logins from TOR exit nodes  
  - Logins from newly registered IP ranges  
- Conduct periodic brute-force simulation tests.  

---

## 9. Lessons Learned

- Early SIEM detection prevented unauthorized access.  
- MFA would significantly reduce the risk of credential-based attacks.  
- Continuous monitoring of authentication logs is essential for proactive defense.  

---

## 10. Conclusion

The SIEM successfully detected a brute-force attempt targeting a FishForYou Global Services employee account. The incident was contained quickly, with no compromise or operational impact. Strengthening authentication controls and expanding detection rules will further reduce the risk of similar attacks.

---

