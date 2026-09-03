# NovaTech Financial Group
## AI Implementation Guidance Policy

**Document ID:** GOV-IGP-2026-001 (Rev. 1)

**Effective Date:** 1 October 2026

**Owner:** AI Governance Council

**Applies To:** All AI/ML initiatives across development, procurement, and deployment lifecycles

---

## 1. Purpose & Strategic Context

### 1.1 Policy Objective

This Implementation Guidance Policy translates NovaTech's AI governance framework into **actionable, enforceable, and auditable controls** across the entire AI lifecycle.

This policy addresses a critical gap observed across the industry: organizations frequently complete governance documentation "on paper" but fail to operationalize risk management into enforceable controls. This guidance closes that gap.

### 1.2 Scope

| Category | Applicability |
|----------|---------------|
| **Internally Developed AI** | All AI/ML models built by NovaTech engineers or data scientists |
| **Third-Party AI** | All AI systems procured from vendors, including embedded SaaS copilots |
| **Generative AI** | All GenAI tools, APIs, and platforms used by NovaTech personnel |
| **Material Changes** | Any significant update to an existing AI system |

**Exclusions:** This policy does not apply to non-AI automation (rule-based systems, traditional statistical models without ML components).

### 1.3 Alignment with Regulatory Frameworks

This policy operationalizes requirements from:

| Framework | Relevance |
|-----------|-----------|
| **NIST AI RMF 1.0** | Core structure (GOVERN, MAP, MEASURE, MANAGE) mapped to lifecycle phases |
| **ISO/IEC 42001:2026** | AI Management System (AIMS) controls and implementation guidance |
| **EU AI Act** | High-risk system obligations (Title III), transparency (Art. 50), and post-market monitoring |
| **U.S. FS AI RMF (Treasury)** | Financial services sector-specific guidance |

---

## 2. Core Principles

### 2.1 Governance is an Operational Problem, Not a Documentation Exercise

This policy treats AI governance as a set of **enforceable controls**, not merely a collection of policies. Every requirement below specifies:

- **Who** is accountable
- **What** action must be taken
- **When** it must occur
- **What evidence** must be preserved for audit

### 2.2 Risk-Proportionate Implementation

Controls scale with risk tier (as classified under the UCCF):

| Risk Tier | Implementation Rigor |
|-----------|---------------------|
| **Tier 1 (High-Risk)** | Full controls — all phases, all gates, all documentation |
| **Tier 2 (Limited-Risk)** | Simplified controls — transparency obligations + basic documentation |
| **Tier 3 (Minimal-Risk)** | Baseline controls — security + acceptable use only |

### 2.3 Evidence-Driven Compliance

Every control must produce **auditable evidence**. "We did it" is not sufficient — "Here is the evidence that we did it" is the standard.

---

## 3. AI Lifecycle Implementation Controls

### 3.1 Phase 1: GOVERN — Establish Organizational Foundation

#### 3.1.1 AI Policy Documentation (ISO 42001 Clause 5.2)

| Requirement | Action | Owner | Evidence |
|-------------|--------|-------|----------|
| **AI Policy** | Document and maintain an enterprise-wide AI policy approved by the AI Governance Council | CAIO | Signed policy document, annual review records |
| **Scope Definition** | Define the scope of the AI Management System (AIMS) | AI Governance Council | AIMS scope document |
| **Objectives** | Establish measurable AI governance objectives aligned with business strategy | CAIO + Business Leads | Objectives register |

#### 3.1.2 Roles & Responsibilities (ISO 42001 Clause 5.3)

| Requirement | Action | Owner | Evidence |
|-------------|--------|-------|----------|
| **Accountability Assignment** | Assign a designated accountable owner for every AI system | AI Governance Council | Org chart with AI ownership mapped |
| **RACI Matrix** | Document RACI for all AI roles | AI CoE | RACI matrix document |
| **Separation of Duties** | Ensure separation between development, validation, and operational teams for high-risk systems | HR + AI CoE | Org structure documentation |

#### 3.1.3 Competence & Awareness (EU AI Act Art. 4; ISO 42001 Clause 7.2)

| Requirement | Action | Owner | Evidence |
|-------------|--------|-------|----------|
| **AI Literacy Training** | All personnel must complete role-based AI literacy training | L&D + AI CoE | LMS completion records |
| **Board-Level Training** | Annual AI governance briefing for Board AI Oversight Committee | CAIO | Training materials, attendance records |
| **Specialist Training** | Data scientists and ML engineers must complete responsible AI development training (16 hours minimum) | AI CoE | Certification records |
| **Refresher Training** | Annual refresher for all roles; additional training upon material regulatory changes | L&D | Training schedules, completion rates |

---

### 3.2 Phase 2: DESIGN — Requirements & Planning

#### 3.2.1 Use Case Classification (UCCF Gate)

| Requirement | Action | Owner | Evidence |
|-------------|--------|-------|----------|
| **Pre-Development Classification** | Every AI initiative must complete the UCCF Triple-Gate assessment before any development begins | Business Sponsor + AI Risk Working Group | Completed UCCF intake form with classification decision |
| **Classification Approval** | Tier 1 classification requires AI Governance Council approval; Tier 2/3 approved by AI Risk Working Group | AI Governance Council | Signed approval record |
| **Re-classification Triggers** | Material changes require re-classification; escalation protocol documented | System Owner | Change management records |

#### 3.2.2 System Context Documentation (NIST MAP)

| Requirement | Action | Owner | Evidence |
|-------------|--------|-------|----------|
| **Intended Purpose** | Document the system's intended purpose, user population, and deployment context | Product Manager | System context document |
| **Decision Authority** | Define whether the system is fully autonomous, human-in-the-loop, or human-on-the-loop | Product Manager + Legal | Decision authority matrix |
| **Fallback Mechanisms** | Document backup procedures if the AI system fails or is unavailable | Engineering Lead | Fallback runbook |
| **Stakeholder Mapping** | Identify all affected parties | Product Manager | Stakeholder register |

#### 3.2.3 Data Governance (NIST MAP)

| Requirement | Action | Owner | Evidence |
|-------------|--------|-------|----------|
| **Data Lineage** | Document complete data lineage for training, validation, and operational data | Data Engineer | Data flow diagrams |
| **Data Privacy Classification** | Classify all data used by the AI system | Data Privacy Officer | Data classification register |
| **Data Consent** | Verify that all training data has appropriate consent for AI use | Legal + Privacy | Consent records |
| **Data Quality** | Establish data quality standards and validation checks | Data Governance Lead | Data quality report |

#### 3.2.4 Bias & Fairness Planning

| Requirement | Action | Owner | Evidence |
|-------------|--------|-------|----------|
| **Fairness Criteria** | Define fairness metrics and thresholds before development begins | Model Risk | Fairness criteria document |
| **Protected Attributes** | Identify relevant protected attributes for the use case and jurisdiction | Legal + Compliance | Protected attributes register |
| **Proxy Risk Assessment** | Identify potential proxy variables that could introduce bias | Data Scientist + Model Risk | Proxy risk assessment |

---

### 3.3 Phase 3: BUILD — Development & Training

#### 3.3.1 Secure Development (NIST MANAGE; ISO 42001 A.6.2)

| Requirement | Action | Owner | Evidence |
|-------------|--------|-------|----------|
| **Secure Coding Standards** | Apply secure coding practices specific to AI/ML (OWASP LLM Top 10) | ML Engineer | Code review records |
| **Dependency Management** | Maintain an AI Bill of Materials (AI-BOM) | ML Engineer | AI-BOM document |
| **Version Control** | All model code, configurations, and data preprocessing scripts must be version-controlled | ML Engineer | Git/version control logs |
| **Reproducibility** | Ensure full reproducibility of training runs | ML Engineer | Reproducibility documentation |

#### 3.3.2 Data Processing & Feature Engineering

| Requirement | Action | Owner | Evidence |
|-------------|--------|-------|----------|
| **Data Preprocessing Documentation** | Document all data preprocessing, feature engineering, and transformation steps | Data Scientist | Preprocessing documentation |
| **Data Leakage Prevention** | Implement controls to prevent data leakage between training and test sets | Data Scientist | Leakage prevention validation |
| **Synthetic Data** | If synthetic data is used, document its generation method and limitations | Data Scientist | Synthetic data documentation |

#### 3.3.3 Model Training & Selection

| Requirement | Action | Owner | Evidence |
|-------------|--------|-------|----------|
| **Training Logs** | Maintain comprehensive logs of all training runs | ML Engineer | Training logs |
| **Model Selection Justification** | Document why the selected model architecture was chosen over alternatives | Data Scientist | Model selection report |
| **Explainability Planning** | For high-risk systems, plan for explainability/interpretability from the outset | Data Scientist | Explainability plan |

---

### 3.4 Phase 4: TEST & VALIDATE — Verification & Validation

#### 3.4.1 Performance Validation

| Requirement | Action | Owner | Evidence |
|-------------|--------|-------|----------|
| **Test Harness** | Establish a comprehensive test harness covering all performance metrics | ML Engineer | Test harness documentation |
| **Performance Benchmarks** | Validate against pre-defined performance benchmarks | Model Validator | Performance validation report |
| **Stress Testing** | Test system performance under edge cases, out-of-distribution data, and adverse conditions | ML Engineer + QA | Stress test results |

#### 3.4.2 Bias & Fairness Testing (NIST MEASURE)

| Requirement | Action | Owner | Evidence |
|-------------|--------|-------|----------|
| **Disparate Impact Analysis** | Compute disparate impact ratios across all protected attributes | Model Risk | Bias test report |
| **Fairness Metric Dashboard** | Generate fairness metrics dashboard for all protected groups | Model Risk | Dashboard screenshots |
| **Remediation Plan** | If fairness thresholds are breached, document remediation plan with timeline | Data Scientist + Model Risk | Remediation plan |
| **Third-Party Audit** | For Tier 1 systems, engage independent third-party for bias audit before deployment | Procurement + Model Risk | Third-party audit report |

#### 3.4.3 Security Testing

| Requirement | Action | Owner | Evidence |
|-------------|--------|-------|----------|
| **Adversarial Testing** | Conduct adversarial robustness testing | Security Team | Red team report |
| **Prompt Injection Testing** | For GenAI systems, test prompt injection and jailbreak vectors | Security Team | Prompt injection test results |
| **Model Extraction Testing** | Test vulnerability to model extraction attacks | Security Team | Extraction test results |
| **Vulnerability Scanning** | Run automated vulnerability scans on AI system components | Security Team | Scan reports |

#### 3.4.4 AI Risk Assessment (AIRA) — Mandatory Pre-Deployment Gate

| Requirement | Action | Owner | Evidence |
|-------------|--------|-------|----------|
| **Complete AIRA** | For Tier 1 and Tier 2 systems, complete the AI Risk Assessment before deployment | AI Risk Working Group | Completed AIRA document |
| **Risk Treatment Plan** | For all identified risks, document treatment strategies with owners and timelines | System Owner | Risk treatment register |
| **Residual Risk Sign-Off** | Obtain sign-off from AI Governance Council on residual risk acceptance | AI Governance Council | Signed AIRA |

---

### 3.5 Phase 5: DEPLOY & MONITOR — Production & Ongoing Oversight

#### 3.5.1 Deployment Controls

| Requirement | Action | Owner | Evidence |
|-------------|--------|-------|----------|
| **Deployment Checklist** | Complete pre-deployment checklist | ML Ops | Signed deployment checklist |
| **Human Oversight** | Implement human oversight mechanisms as defined in the AIRA | System Owner | Oversight logs |
| **Kill-Switch** | Implement emergency shutdown/kill-switch capability for all Tier 1 systems | ML Ops | Kill-switch test records |
| **Rollback Plan** | Document and test rollback procedures | ML Ops | Rollback runbook |

#### 3.5.2 Continuous Monitoring (NIST MEASURE; EU AI Act Art. 72-73)

| Requirement | Action | Owner | Evidence |
|-------------|--------|-------|----------|
| **Performance Monitoring** | Monitor key performance metrics on an ongoing basis | ML Ops | Monitoring dashboards |
| **Drift Detection** | Implement automated drift detection with alerting | ML Ops | Drift detection logs |
| **Fairness Monitoring** | Continuously monitor fairness metrics; alert if thresholds are breached | Model Risk | Fairness monitoring dashboard |
| **Incident Detection** | Implement automated incident detection and alerting | ML Ops + Security | Incident detection logs |

#### 3.5.3 Post-Market Monitoring (EU AI Act Art. 72-73)

| Requirement | Action | Owner | Evidence |
|-------------|--------|-------|----------|
| **Post-Market Monitoring Plan** | Document and implement post-market monitoring plan for Tier 1 systems | System Owner | Post-market monitoring plan |
| **Systematic Data Collection** | Systematically collect performance data, user feedback, and incident reports | ML Ops | Post-market monitoring reports (monthly) |
| **Serious Incident Reporting** | Report serious incidents to relevant authorities within required timelines | Legal + Compliance | Incident notification records |

#### 3.5.4 Incident Response (NIST MANAGE)

| Requirement | Action | Owner | Evidence |
|-------------|--------|-------|----------|
| **Incident Response Plan** | Maintain AI-specific incident response runbook | CISO + AI CoE | Incident response plan |
| **Incident Drills** | Conduct quarterly incident response drills for Tier 1 systems | CISO | Drill logs |
| **Incident Logging** | Log all incidents with severity classification, root cause, remediation, and lessons learned | System Owner | Incident log |
| **Post-Incident Review** | Conduct post-incident review within 7 days of any material incident | AI Governance Council | Post-incident review report |

#### 3.5.5 Periodic Review & Re-assessment

| Requirement | Action | Owner | Evidence |
|-------------|--------|-------|----------|
| **Annual AIRA Review** | Review and update AIRA annually or upon material change | AI Risk Working Group | Updated AIRA |
| **Regulatory Change Assessment** | Assess impact of regulatory changes on existing AI systems quarterly | Legal + Compliance | Regulatory change impact assessment |
| **Model Retirement** | Document retirement procedures when AI system is decommissioned | System Owner | Retirement checklist |

---

## 4. Third-Party AI Implementation Guidance

### 4.1 Vendor Due Diligence (Pre-Procurement)

| Requirement | Action | Owner | Evidence |
|-------------|--------|-------|----------|
| **Vendor AI Risk Assessment** | Complete vendor AI risk assessment before procurement | Procurement + AI Risk | Vendor risk assessment document |
| **Model Documentation Review** | Review vendor's model documentation, training data practices, and validation results | Model Risk | Documentation review report |
| **Security Assessment** | Assess vendor's security practices, data handling, and compliance posture | CISO | Security assessment report |
| **Compliance Mapping** | Map vendor's practices to EU AI Act, ISO 42001, and other applicable regulations | Legal + Compliance | Compliance mapping matrix |

### 4.2 Ongoing Vendor Oversight

| Requirement | Action | Owner | Evidence |
|-------------|--------|-------|----------|
| **Vendor Monitoring** | Continuously monitor vendor AI systems for performance, security, and compliance | ML Ops | Vendor monitoring dashboard |
| **Vendor Incident Reporting** | Require vendor to report incidents affecting NovaTech within 24 hours | Legal | Vendor incident reporting agreements |
| **Vendor Re-assessment** | Re-assess vendor annually or upon material changes | Procurement | Updated vendor assessment |

---

## 5. Generative AI Implementation Guidance

### 5.1 Acceptable Use

| Requirement | Action | Owner | Evidence |
|-------------|--------|-------|----------|
| **Approved Tools List** | Maintain list of approved GenAI tools and platforms | IT + AI CoE | Approved tools list |
| **Prohibited Use Cases** | Define prohibited use cases | Legal + Compliance | Prohibited use policy |
| **User Guidelines** | Provide clear guidelines on what can and cannot be shared with GenAI tools | L&D + AI CoE | User guidelines document |

### 5.2 Transparency & Disclosure (EU AI Act Art. 50)

| Requirement | Action | Owner | Evidence |
|-------------|--------|-------|----------|
| **AI Disclosure** | Clearly disclose when customers are interacting with an AI system | Product + Legal | Disclosure implementation |
| **Content Watermarking** | Implement machine-readable marking and watermarking for AI-generated synthetic content | Engineering | Watermarking implementation |
| **Deepfake Labeling** | Label AI-generated or manipulated images, videos, and audio | Product | Labeling implementation |

### 5.3 Guardrails & Runtime Controls (NIST AI 600-1)

| Requirement | Action | Owner | Evidence |
|-------------|--------|-------|----------|
| **Content Filtering** | Implement guardrails to filter harmful, hateful, or inappropriate content | Engineering | Guardrail implementation |
| **Data Loss Prevention** | Implement DLP controls to prevent sensitive data from being sent to GenAI tools | Security | DLP configuration |
| **Prompt Injection Protection** | Implement controls to detect and block prompt injection attempts | Security | Prompt injection protection |

---

## 6. Evidence & Audit Readiness

### 6.1 Evidence Retention Requirements

| Evidence Type | Retention Period | Format |
|---------------|------------------|--------|
| AI risk assessments (AIRA) | 6 years | Digital repository with version control |
| Model cards / technical documentation | Life of system + 6 years | Standardized templates |
| Bias audit reports | 6 years | Third-party signed reports |
| Incident reports | 6 years | Structured database |
| Training records | 3 years | LMS records |
| Monitoring logs | 3 years | System logs with integrity controls |
| Human oversight logs | 6 years | Audit trails |
| EU database registrations | Life of system | EU AI Act database |
| UCCF classification records | 6 years | Digital repository |

### 6.2 Audit Trail Requirements

| Requirement | Action | Owner | Evidence |
|-------------|--------|-------|----------|
| **Immutable Logging** | Maintain immutable audit logs for all AI system actions | ML Ops | Audit log configuration |
| **Access Controls** | Restrict access to audit logs to authorized personnel only | Security | Access control records |
| **Log Integrity** | Implement controls to prevent tampering with audit logs | Security | Log integrity validation |

---

## 7. Policy Enforcement & Consequences

| Violation Type | Consequence | Responsible Party |
|----------------|-------------|-------------------|
| **Deployment without AIRA** | Immediate system pause; mandatory re-assessment; disciplinary action | AI Governance Council |
| **Failure to complete training** | Access to AI development tools restricted until training completed | IT + AI CoE |
| **Material incident not reported** | Escalation to Board AI Oversight Committee | CISO + Legal |
| **Under-classification of AI system** | Re-classification; mandatory additional controls; audit of classification process | Internal Audit |

---

## 8. Continuous Improvement & Review

| Activity | Frequency | Owner |
|----------|-----------|-------|
| **Policy Review** | Annual (or upon material regulatory change) | AI Governance Council |
| **Control Effectiveness Assessment** | Annual | Internal Audit |
| **Implementation Status Review** | Quarterly | AI Risk Working Group |
| **Regulatory Change Monitoring** | Continuous | Legal + Compliance |
| **Maturity Assessment** | Annual | AI Governance Council |
