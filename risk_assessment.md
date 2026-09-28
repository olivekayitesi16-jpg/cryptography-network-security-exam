STEP 2: Risk Assessment
Assets
Asset 1
Student records database
Asset 2
File transfer system
Asset 3
Central server
Vulnerabilities
Vulnerability 1
Weak staff passwords
Vulnerability 2
Unencrypted file transfer
Vulnerability 3
Guest network access to records server
Consequences
Vulnerability	ConsequenceWeak Passwords	Unauthorized access
Unencrypted Transfer	Data interception
Guest Access	Data theft or modification
Risk Ranking
Risk	Likelihood	Impact	RankGuest Network Access	High	High	1
Weak Passwords	High	Medium	2
Unencrypted Transfer	Medium	High	3
Recommended Controls
Risk	ControlGuest Access	Firewall restrictions
Weak Passwords	Strong password policy + MFA
Unencrypted Transfer	AES file encryption
Risk assessment is the process of:
Identifying assets that need protection.
Identifying vulnerabilities affecting those assets.
Determining possible threats.
Evaluating likelihood and impact.
Recommending security controls.
Formula:
Risk = Threat × Vulnerability × Impact
2. Asset Identification
Assets are valuable resources that must be protected.
Asset	Description	ImportanceStudent Records Database	Contains student personal and academic information	Very High
Central Server	Stores institutional data and applications	Very High
File Transfer System	Transfers records between campuses	High
Why these are assets
Student Records Database
Contains names
Student IDs
Grades
Academic information
If compromised:
Privacy violations
Data loss
Reputation damage
Central Server
Hosts records
Provides user access
If compromised:
Entire system affected
Services unavailable
File Transfer System
Transfers records between campuses
If compromised:
Data interception
Data alteration
3. Vulnerability Analysis
A vulnerability is a weakness that can be exploited.
Vulnerability 1: Weak Staff Passwords
Description
Employees use passwords that are easy to guess.
Examples:
123456
password
admin123
Threats
Password guessing
Brute force attacks
Credential theft
Consequences
Unauthorized access
Stolen records
Privilege escalation
Vulnerability 2: Unencrypted File Transfers
Description
Files travel across the network in plain text.
Threats
Packet sniffing
Man-in-the-middle attacks
Data interception
Consequences
Exposure of student records
Data tampering
Confidentiality breach
Vulnerability 3: Guest Network Access
Description
Guests can reach the records server.
Threats
Unauthorized system access
Malware spreading
Network reconnaissance
Consequences
Data theft
System compromise
Service disruption
4. Threat Analysis
Threat	Target Asset	ResultPassword Cracking	Student Records	Unauthorized access
Data Interception	File Transfer System	Information disclosure
Guest Network Intrusion	Central Server	System compromise
External Attack Attempts	Central Server	Potential breach
The examination scenario specifically mentions repeated connection attempts from an unfamiliar external address.
5. Risk Evaluation Matrix
Risk is usually measured using:
Likelihood
Level	MeaningLow	Rare
Medium	Possible
High	Frequent
Impact
Level	MeaningLow	Minor damage
Medium	Significant disruption
High	Severe damage
6. Risk Ranking
Risk 1: Guest Network Access
Assessment
Likelihood:
High
Reason: Guest users already have access paths to the server.
Impact:
High
Reason: Sensitive records may be stolen or altered.
Risk Score:
Critical
Show more lines
Risk 2: Weak Passwords
Assessment
High
Reason: Weak passwords are commonly exploited.
Impact:
Medium
Reason: Only accounts with weak credentials may initially be affected.
Risk Score:
High
Risk 3: Unencrypted File Transfers
Assessment
Medium
Reason: An attacker must capture traffic.
Impact:
High
Reason: Student information may be exposed.
Risk Score:
High
7. Risk Matrix
IMPACT
Low Med High
Likelihood High - R2 R1
Likelihood Med - - R3
Likelihood Low - - -
R1 = Guest Network Access
R2 = Weak Passwords
R3 = Unencrypted Transfers
