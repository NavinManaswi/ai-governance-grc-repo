# NovaTech Financial Group
## AI Policy Handbook

**Document ID:** GOV-POL-2026-001

**Effective Date:** 1 March 2026

**Owner:** Chief AI Officer (CAIO)

**Approval:** AI Governance Council (1 March 2026)

---

## 1. Purpose

This Policy Handbook establishes the mandatory principles, standards, and controls for the development, deployment, and operation of Artificial Intelligence (AI) systems at NovaTech Financial Group. It applies to all AI systems, whether internally developed, procured from vendors, or embedded in third-party products.

---

## 2. Scope

This policy applies to:

| Category | Applicability |
|----------|---------------|
| **Internally Developed AI** | All AI/ML models built by NovaTech engineers or data scientists |
| **Third-Party AI** | All AI systems procured from vendors, including embedded SaaS copilots |
| **Generative AI** | All GenAI tools, APIs, and platforms used by NovaTech personnel |
| **Material Changes** | Any significant update to an existing AI system |

**Exclusions:** Non-AI automation (rule-based systems, traditional statistical models without ML components).

---

## 3. Core Principles

### 3.1 Transparency

- **Disclosure:** Customers must be informed when interacting with an AI system
- **Explainability:** Automated decisions must be explainable to affected individuals
- **Documentation:** All AI systems must have comprehensive technical documentation

### 3.2 Fairness

- **Non-Discrimination:** AI systems must not discriminate on protected characteristics
- **Bias Mitigation:** Proactive testing and mitigation of algorithmic bias
- **Equity:** AI systems must consider the impact on disadvantaged groups

### 3.3 Accountability

- **Ownership:** Every AI system must have a designated accountable owner
- **Oversight:** High-risk systems require human oversight
- **Audit Trail:** All AI decisions must be logged and auditable

### 3.4 Security & Privacy

- **Data Protection:** AI systems must comply with data privacy laws
- **Robustness:** AI systems must be resilient to attacks and failures
- **Confidentiality:** Training data and model weights must be protected

---

## 4. AI Use Case Classification

All AI use cases must be classified using the **Use Case Classification Framework (UCCF)** :

| Tier | Risk Level | Definition | Examples |
|------|------------|------------|----------|
| **Tier 0** | Unacceptable Risk | Prohibited practices under EU AI Act Art. 5 | Social scoring, manipulative AI |
| **Tier 1** | High-Risk | Annex III use cases | Credit underwriting, recruitment, insurance pricing |
| **Tier 2** | Limited-Risk | Transparency obligations | Customer chatbots, content generation |
| **Tier 3** | Minimal-Risk | No regulatory obligations | Internal productivity tools |

---

## 5. Acceptable Use Policy

### 5.1 Prohibited Uses

The following AI uses are **strictly prohibited**:

1. **Manipulative AI** — Systems using subliminal techniques to distort behavior
2. **Exploitative AI** — Systems exploiting vulnerabilities (age, disability, socioeconomic status)
3. **Social Scoring** — Systems evaluating individuals for public or private social scoring
4. **Real-Time Biometric Identification** — Systems using real-time remote biometric identification in public spaces
5. **Rogue AI** — Use of unauthorized AI tools without IT/Governance approval

### 5.2 Permitted Uses with Oversight

1. **High-Risk AI** — Requires full AIRA, human oversight, and continuous monitoring
2. **Customer-Facing AI** — Requires transparency disclosure under Art. 50
3. **Internal AI** — Requires baseline security and acceptable use adherence

### 5.3 Employee Responsibilities

1. **Disclosure:** Employees must disclose any AI tool they use for work purposes
2. **Approval:** Employees must obtain approval before using any new AI tool
3. **Data Protection:** Employees must not input confidential data into unauthorized AI tools
4. **Reporting:** Employees must report AI incidents immediately

---

## 6. AI Development Lifecycle Standards

### 6.1 Design Phase

- Complete UCCF classification before development
- Document system context, intended purpose, and decision authority
- Establish data governance and lineage
- Define fairness criteria and bias thresholds

### 6.2 Build Phase

- Apply secure coding standards (OWASP LLM Top 10)
- Maintain AI Bill of Materials (AI-BOM)
- Ensure full reproducibility of training runs
- Document all data preprocessing and feature engineering

### 6.3 Test Phase

- Validate performance against benchmarks
- Test for bias across protected attributes
- Conduct adversarial robustness testing
- Complete AI Risk Assessment (AIRA) for Tier 1 systems
- Obtain AIRA sign-off before deployment

### 6.4 Deploy Phase

- Complete pre-deployment checklist
- Implement human oversight mechanisms
- Deploy kill-switch and rollback capability
- Establish continuous monitoring

### 6.5 Operate Phase

- Monitor performance, drift, fairness, and security
- Maintain incident response readiness
- Conduct annual AIRA reviews
- Prepare for regulatory audits

---

## 7. Incident Response

### 7.1 Incident Severity Tiers

| Severity | Definition | Reporting Timeline |
|----------|------------|-------------------|
| **Critical** | Death, serious harm, fundamental rights violation | 2-10 days to authority |
| **High** | Material financial harm, significant bias | 15 days to authority |
| **Medium** | Operational disruption, minor compliance issue | Internal within 24 hours |
| **Low** | Minor errors, user complaints | Internal within 7 days |

### 7.2 Incident Response Steps

1. **Detection** — Identify and verify the incident
2. **Containment** — Stop the harm (kill-switch, rollback)
3. **Assessment** — Determine severity and root cause
4. **Notification** — Inform affected stakeholders and regulators
5. **Remediation** — Fix the root cause
6. **Review** — Conduct post-incident review and update controls

---

## 8. Vendor Management

### 8.1 Vendor Due Diligence

Before procuring any AI system, complete:

1. **Vendor AI Risk Assessment** — Model documentation, training data, security
2. **Security Assessment** — Vendor's security practices and compliance posture
3. **Compliance Mapping** — Map vendor's practices to applicable regulations

### 8.2 Ongoing Oversight

1. **Contractual Requirements** — Incident reporting, audit rights, compliance assurances
2. **Performance Monitoring** — Monitor vendor AI systems for issues
3. **Annual Re-assessment** — Re-assess vendors annually

---

## 9. Training & Awareness

### 9.1 Training Requirements

| Role | Training | Frequency |
|------|----------|-----------|
| **Board** | AI governance briefing | Annual |
| **Executives** | AI risk management | Semi-annual |
| **Developers** | Responsible AI development | Quarterly |
| **All Employees** | General AI awareness | Annual |

### 9.2 Training Completion Targets

- 100% completion within 90 days of hire
- 100% annual refresher completion
- 95%+ overall completion rate

---

## 10. Audit & Evidence Retention

### 10.1 Evidence Retention

| Evidence Type | Retention Period |
|---------------|------------------|
| AI risk assessments (AIRA) | 6 years |
| Bias audit reports | 6 years |
| Incident reports | 6 years |
| Training records | 3 years |
| Monitoring logs | 3 years |
| Human oversight logs | 6 years |

### 10.2 Audit Rights

Internal Audit (3rd Line) has the right to:

- Access all AI system documentation and data
- Conduct independent testing of AI systems
- Report findings directly to the Board Audit Committee

---

## 11. Policy Review & Update

| Activity | Frequency | Owner |
|----------|-----------|-------|
| Policy review | Annual | AI Governance Council |
| Regulatory impact assessment | Quarterly | Legal + Compliance |
| Control effectiveness | Annual | Internal Audit |

---

## 12. Signatories

| Signatory | Title | Signature | Date |
|-----------|-------|-----------|------|
| | Chief AI Officer | | |
| | Chief Risk Officer | | |
| | General Counsel | | |
