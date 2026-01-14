
This displayed the current permissions for:
- One directory: `drafts/`
- Four project files: `project_k.txt`, `project_m.txt`, `project_r.txt`, `project_t.txt`

The first column of the output showed the permission strings, which indicate:
- File or directory type  
- User permissions  
- Group permissions  
- Other permissions  

Example (before changes):
-rw-rw-rw- project_k.txt

This means:
- `-` → regular file  
- `rw-` → user can read and write  
- `rw-` → group can read and write  
- `rw-` → others can read and write  

---

##  Step 2: Change File Permissions

### **Remove write permission for “other” on `project_k.txt`**

To align with the organization’s policy, I removed write access for the “other” group:
chmod o-w project_k.txt

I confirmed the change using:
ls -l

Updated permissions:
-rw-rw-r-- project_k.txt

Now, “other” can only read the file.

---

## Step 3: Modify Permissions on a Hidden File

The hidden file `.project_x.txt` required stricter access.  
The organization wanted **read‑only** permissions for both the user and group.

I first listed all files, including hidden ones:
ls -la

Then applied the new permissions:
chmod u=r,g=r .project_x.txt

Verification:
ls -la

Result:
-r--r----- .project_x.txt

This ensures:
- User → read only  
- Group → read only  
- Others → no access  

---

## Step 4: Change Directory Permissions

The `drafts` directory needed to restrict group access.  
I removed execute permission for the group:
chmod g-x drafts

Then confirmed:
ls -la

Updated directory permissions:
drwx--x--- drafts

This prevents the group from entering the directory.

---

## Summary

In this project, I:

- Inspected file and directory permissions using `ls -l` and `ls -la`
- Interpreted Linux permission strings
- Applied permission changes using `chmod`
- Verified each change to ensure compliance with organizational standards

This exercise strengthened my understanding of Linux file permissions and demonstrated my ability to apply the principle of least privilege in a practical environment.

---
What I Learned
Through this project, I strengthened my understanding of how Linux file and directory permissions work and why they matter for security. I learned how to:
• 	Interpret permission strings to understand who can read, write, or execute a file
• 	Use  and  to inspect both visible and hidden files
• 	Apply the  command to adjust permissions based on organizational requirements
• 	Remove or assign permissions for users, groups, and others
• 	Verify changes to ensure they align with the principle of least privilege
• 	Recognize how proper permissions help protect sensitive files and prevent unauthorized access
This project helped me build confidence in managing Linux permissions and reinforced the importance of maintaining secure access controls in a real-world environment.
