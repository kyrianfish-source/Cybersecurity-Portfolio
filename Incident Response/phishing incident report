# FishForYou Global Services  
## Incident Response Report: Phishing Attempt

**Analyst:** Kyrian  
**Date:** 14/01/2026
**Department:** Security Operations  
**Incident Type:** Phishing / Social Engineering  
**Severity:** Medium  
**Status:** Resolved  

---

## 1. Executive Summary

On 13/01/2026, an employee at FishForYou Global Services reported a suspicious email requesting urgent account verification. The message impersonated the company’s internal IT Support team and contained a malicious link leading to a fake login page.  

The investigation confirmed that this was a targeted phishing attempt. No credentials were compromised, and the malicious domain was blocked. This report documents the investigation, findings, and recommended preventive actions.

---

## 2. Incident Description

- **Company:** FishForYou Global Services  
- **Target:** Employee in the Finance & Billing Unit  
- **Attack Vector:** Email with spoofed sender identity  
- **Payload:** Malicious URL redirecting to a credential‑harvesting page  
- **Initial Detection:** Employee report via the internal “Report Suspicious Email” button  

The email claimed that the employee needed to “verify account access” due to an urgent system update affecting payroll systems.

---

## 3. Indicators of Compromise (IOCs)

- **Sender Address:** `it-support@fishforyou-helpdesk.com` (not a legitimate domain)  
- **Reply-To:** Different from sender domain  
- **Subject Line:** “URGENT: Payroll Access Verification Required”  
- **Malicious URL:** `http://secure-verify-fishportal.com/login`  
- **Email Red Flags:**  
  - Unusual tone and urgency  
  - External domain not associated with FishForYou  
  - Hovering over the link revealed a mismatched URL  
  - Poor grammar and formatting  

---

## 4. Investigation Steps

1. **Collected the original email** from the reporting employee.  
2. **Analyzed email headers** to confirm spoofing and external origin.  
3. **Checked the malicious URL** in a secure sandbox environment.  
4. **Identified a cloned login page** mimicking FishForYou’s employee portal.  
5. **Reviewed SIEM logs** for any clicks or credential submissions.  
6. **Confirmed no other employees received the same email**.  
7. **Blocked the sender domain** at the email gateway.  
8. **Added the malicious URL** to the company’s web filter blacklist.  
9. **Documented the incident** and notified the Security Operations Manager.  

---

## 5. Findings

- The attacker attempted to impersonate FishForYou’s internal IT Support team.  
- The phishing page was hosted on a newly registered domain with no security controls.  
- No employees interacted with the malicious link.  
- No lateral spread or additional phishing attempts were detected.  

---

## 6. Impact Assessment

- **Data Exposure:** None  
- **System Compromise:** None  
- **Operational Impact:** Minimal  
- **Reputational Risk:** Low  
- **Likelihood of Recurrence:** Moderate  

---

## 7. Containment & Mitigation

- Blocked sender domain and malicious URL.  
- Updated email filtering rules to detect similar spoofing patterns.  
- Sent a security awareness reminder to all employees.  
- Logged the incident for trend analysis and future threat modeling.  

---

## 8. Recommendations

- Strengthen email authentication (SPF, DKIM, DMARC).  
- Increase monitoring for newly registered domains targeting FishForYou.  
- Conduct quarterly phishing simulations.  
- Continue employee awareness training, especially for Finance and HR teams.  
- Encourage prompt reporting of suspicious emails.  

---

## 9. Lessons Learned

- Employee vigilance was critical in early detection.  
- Quick reporting prevented credential compromise.  
- Improved email authentication will reduce spoofing attempts.  

---

## 10. Conclusion

The phishing attempt targeting FishForYou Global Services was successfully identified and contained with no impact on systems or data. Continued awareness training and enhanced email security controls will further reduce the risk of similar incidents.

---
