# NovaTech Financial Group
## AI Incident Response Runbook

**Document ID:** OPS-IRR-2026-001

**Effective Date:** 1 June 2026

**Owner:** CISO + AI Governance Council

---

## 1. Purpose

This runbook establishes the protocol for detecting, assessing, responding to, and learning from AI-related incidents. It ensures rapid, consistent, and effective response to minimize harm and meet regulatory reporting obligations.

---

## 2. Scope

This runbook applies to all AI systems at NovaTech Financial Group, with enhanced protocols for Tier 1 (High-Risk) systems.

---

## 3. Incident Severity Classification

### 3.1 Severity Tiers

| Severity | Definition | Examples | Reporting Timeline |
|----------|------------|----------|-------------------|
| **Critical** | Death, serious health harm, critical infrastructure disruption, fundamental rights violation | AI misdiagnosis causing physical harm; autonomous system causing mass financial loss | 2-10 days to authority |
| **High** | Material financial harm (>$1M), significant bias (DIR < 70%), regulatory breach | Discriminatory lending pattern; data breach of >10k records; SEC investigation trigger | 15 days to authority |
| **Medium** | Operational disruption, minor compliance issue, service degradation > 1 hour | System outage 30-60 min; minor regulatory breach without material impact | Internal within 24 hours |
| **Low** | Minor errors, user complaints, minor drift | Chatbot hallucination corrected quickly; minimal drift detected | Internal within 7 days |

### 3.2 Severity Decision Matrix

| Impact | Likelihood | Severity |
|--------|------------|----------|
| High | High | Critical |
| High | Medium | High |
| High | Low | Medium |
| Medium | High | High |
| Medium | Medium | Medium |
| Medium | Low | Low |
| Low | Any | Low |

---

## 4. Incident Response Workflow

### 4.1 Step 1: Detection

**Detection Sources:**

| Source | Description | Owner |
|--------|-------------|-------|
| **Automated Alerts** | KRI breaches (drift, fairness, performance) | ML Ops |
| **User Complaints** | Customers or employees reporting issues | Customer Support |
| **Internal Reviews** | Post-market monitoring findings | System Owner |
| **Third-Party Reports** | Vendor incident reports | Vendor Management |
| **Regulatory Inquiries** | Notifications from regulators | Legal |

**Detection Timeline:**

| Severity | Detection Target |
|----------|------------------|
| Critical | < 5 minutes |
| High | < 30 minutes |
| Medium | < 2 hours |
| Low | < 24 hours |

### 4.2 Step 2: Triage & Classification

| Action | Description | Owner | Timeline |
|--------|-------------|-------|----------|
| **Acknowledge** | Log the incident in the incident tracking system | Incident Manager | Immediate |
| **Classify** | Assign severity tier using severity matrix | Incident Manager | < 30 min |
| **Assign** | Assign incident owner based on system and severity | Incident Manager | < 30 min |
| **Notify** | Notify required stakeholders per tier | Incident Manager | Per timeline below |

**Notification Requirements:**

| Severity | Internal Notification | External Notification |
|----------|----------------------|----------------------|
| **Critical** | AI Governance Council within 1 hour; CEO within 2 hours | Regulator per Art. 73 (2-10 days); affected individuals; public disclosure if material |
| **High** | AI Risk Working Group within 2 hours; AI Governance Council within 24 hours | Regulator per Art. 73 (15 days); affected individuals |
| **Medium** | System Owner; AI Risk WG within 24 hours | None unless escalated |
| **Low** | System Owner | None |

### 4.3 Step 3: Containment

| Action | Description | Owner | Timeline |
|--------|-------------|-------|----------|
| **Kill-Switch** | Activate emergency shutdown if necessary | ML Ops | < 15 min for Critical |
| **Rollback** | Revert to previous stable version or fallback | ML Ops | < 30 min |
| **Isolate** | Isolate affected systems and data | Security | < 30 min |
| **Preserve Evidence** | Secure logs, model snapshots, and incident data | Incident Manager | < 60 min |

### 4.4 Step 4: Investigation & Root Cause Analysis

| Action | Description | Owner | Timeline |
|--------|-------------|-------|----------|
| **Collect Data** | Gather logs, model outputs, user interactions | Incident Manager | < 24 hours |
| **Analyze** | Determine root cause (technical, process, data, or external) | Root Cause Team | < 72 hours |
| **Document** | Create incident report with findings | Incident Manager | < 5 days |

**Root Cause Categories:**

| Category | Examples |
|----------|----------|
| **Technical** | Model drift, data quality issue, software bug |
| **Process** | Human error, oversight failure, inadequate testing |
| **Data** | Biased training data, data leakage, data poisoning |
| **External** | Adversarial attack, vendor failure, regulatory change |

### 4.5 Step 5: Remediation & Recovery

| Action | Description | Owner | Timeline |
|--------|-------------|-------|----------|
| **Fix Root Cause** | Implement permanent fix | Engineering | < 10 days |
| **Test** | Validate fix before re-deployment | ML Ops + Model Risk | < 5 days |
| **Re-deploy** | Return system to production | ML Ops | After validation |
| **Notify** | Notify stakeholders of resolution | Incident Manager | Upon resolution |

### 4.6 Step 6: Post-Incident Review

| Action | Description | Owner | Timeline |
|--------|-------------|-------|----------|
| **After-Action Report** | Document full timeline, impact, root cause, remediation | Incident Manager | < 7 days |
| **Lessons Learned** | Identify improvements to controls or runbook | AI Governance Council | < 7 days |
| **Control Updates** | Update controls based on findings | AI Risk WG | < 30 days |
| **Board Report** | Report material incidents to Board Committee | CAIO | Quarterly |

---

## 5. Incident Communication Templates

### 5.1 Internal Notification Template
INCIDENT NOTIFICATION — [Severity]

Incident ID: INC-2026-XXX
System: [System Name]
Date/Time: [Timestamp]
Severity: [Critical/High/Medium/Low]
Description: [Brief description]
Status: [Investigating/Containing/Remediated/Closed]
Impact: [Affected users, financial impact, regulatory impact]
Owner: [Name]
Next Update: [Time]


### 5.2 Regulatory Notification Template (EU AI Act Art. 73)
SERIOUS INCIDENT NOTIFICATION

Notification Date: [Date]
Notifying Entity: NovaTech Financial Group
AI System: [System Name]
EU Database Registration: [Registration Number]
Incident Description: [Detailed description]
Date of Incident: [Date]
Date of Detection: [Date]
Affected Individuals: [Number]
Impact Assessment: [Fundamental rights, health, safety, environment]
Root Cause: [Preliminary findings]
Mitigations Taken: [Actions taken]
Contact Person: [Name, Title, Email, Phone]


---

## 6. Incident Log

| Incident ID | System | Severity | Date | Status | Owner |
|-------------|--------|----------|------|--------|-------|
| INC-2026-001 | NovaChat | Low | 15 Jan 2026 | Closed | ML Ops |
| INC-2026-002 | CreditIQ | Medium | 12 Feb 2026 | Closed | Model Risk |
| INC-2026-003 | FraudShield | High | 20 Mar 2026 | Open | Security |
| INC-2026-004 | RecruitAI | High | 15 Aug 2026 | In Review | Compliance |

---

## 7. Incident Response Drills

| Drill Type | Frequency | Participants | Objective |
|------------|-----------|--------------|-----------|
| **Tabletop Exercise** | Quarterly | All incident response roles | Test runbook and escalation |
| **Simulated Incident** | Annually | Technical and operational teams | Test technical response capability |
| **Post-Implementation Review** | After major changes | System Owner + Incident Team | Validate runbook updates |

---

## 8. Runbook Sign-Off

| Signatory | Title | Signature | Date |
|-----------|-------|-----------|------|
| | CISO | | |
| | CAIO | | |
| | AI Governance Council Chair | | |
