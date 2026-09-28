# Cryptography & Network Security - Risk Assessment

## 1. Asset, Vulnerability, and Impact Identification

| Asset | Vulnerability | Possible Consequence |
| :--- | :--- | :--- |
| **Student Records File/Database** | Unencrypted file transfers across campuses & guest network access | Interception, unauthorized access, and breach of confidential student records. |
| **Central Records Server** | Guest network accessibility & repeated external connection attempts | Unauthorized access, privilege escalation, or Denial of Service (DoS) attacks. |
| **Staff Credentials & Accounts** | Weak staff passwords | Brute-force/dictionary attacks leading to credential compromise and unauthorized administrative actions. |

---

## 2. Risk Evaluation and Ranking

Risks are ranked using Likelihood and Impact (Scale: High, Medium, Low):

1. **Risk 1: Guest Network Access to Records Server**
   - **Likelihood:** High | **Impact:** High | **Overall:** High
   - **Reasoning:** Guest networks are open to arbitrary untrusted users. Direct network exposure to critical internal infrastructure invites immediate exploitation.

2. **Risk 2: Weak Staff Passwords & Unencrypted File Transfer**
   - **Likelihood:** High | **Impact:** Medium-High | **Overall:** High
   - **Reasoning:** Weak passwords are standard targets for automated brute-forcing. Unencrypted transfers allow packet sniffing across transit lines.

3. **Risk 3: Unfiltered External Access Attempts**
   - **Likelihood:** Medium | **Impact:** Medium | **Overall:** Medium
   - **Reasoning:** External probes are common on open networks. Without IP/port restriction, an attacker will eventually discover unpatched software or service flaws.

---

## 3. Recommended Controls

1. **Network Segmentation & Firewall Rules:** Implement strict IP/port filtering using `iptables` or `ufw` to isolate the student records server onto a dedicated VLAN, completely dropping all guest network traffic.
2. **Encryption in Transit & Rest:** Use AES-256-GCM symmetric encryption for local file storage and enforce TLS/SSH/SFTP protocols for file transfers across campuses.
3. **Strong Authentication & Account Security:** Enforce strong password policies (min 12 characters, complexity requirements) and multi-factor authentication (MFA) for staff accounts.
