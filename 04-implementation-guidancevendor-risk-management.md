# NovaTech Financial Group
## Third-Party AI Vendor Risk Management Framework

**Document ID:** GOV-VRM-2026-001

**Effective Date:** 1 June 2026

**Owner:** Procurement + AI Risk Working Group

---

## 1. Purpose

This document establishes the framework for assessing, onboarding, and continuously monitoring third-party AI vendors. It ensures that AI risks introduced through vendors are identified, assessed, and mitigated to acceptable levels.

---

## 2. Scope

This framework applies to:

| Category | Applicability |
|----------|---------------|
| **AI API Providers** | Vendors providing AI APIs (e.g., OpenAI, Anthropic, Google Vertex) |
| **Embedded AI** | SaaS products with embedded AI capabilities |
| **AI Platforms** | ML platforms, MLOps tools, and AI infrastructure |
| **Custom AI Development** | Vendors building custom AI models on behalf of NovaTech |

---

## 3. Vendor Risk Assessment Process

### 3.1 Pre-Procurement Assessment

#### Phase 1: Initial Screening

| Step | Action | Owner | Output |
|------|--------|-------|--------|
| 1 | Identify intended AI use case and vendor | Business Unit | UCCF classification |
| 2 | Determine if vendor AI is high-risk | AI Risk WG | Risk tier |
| 3 | Request vendor documentation | Procurement | AI documentation package |
| 4 | Conduct initial risk screening | AI Risk WG | Screening report |

#### Phase 2: Deep-Dive Assessment

| Assessment Area | Questions to Answer | Evidence Required |
|-----------------|---------------------|-------------------|
| **Model Documentation** | Is the model architecture, training data, and validation results documented? | Model card, technical paper |
| **Bias & Fairness** | Has the vendor tested for bias across protected attributes? | Bias audit report |
| **Security** | What security controls are in place? Is the vendor SOC 2 / ISO 27001 certified? | Security assessment, certifications |
| **Data Privacy** | How is data processed, stored, and protected? Is it used for training? | Data processing agreement, privacy policy |
| **Compliance** | Is the vendor compliant with EU AI Act, GDPR, and other applicable regulations? | Compliance mapping |
| **Incident Response** | Does the vendor have incident response capabilities and reporting obligations? | Incident response plan |
| **Business Continuity** | What happens if the vendor experiences downtime or goes out of business? | BCP/DR plan, exit strategy |

#### Phase 3: Risk Classification & Approval

| Vendor Risk Rating | Definition | Action |
|--------------------|------------|--------|
| **High Risk** | Vendor AI is high-risk; sensitive data is processed; critical business function | Requires AI Governance Council approval; enhanced monitoring |
| **Medium Risk** | Vendor AI is limited-risk; moderate data sensitivity | Requires AI Risk Working Group approval; standard monitoring |
| **Low Risk** | Vendor AI is minimal-risk; non-sensitive data | Business unit approval; baseline monitoring |

---

## 4. Vendor Risk Assessment Questionnaire

### Section 1: AI System Overview

| Question | Details |
|----------|---------|
| What is the vendor's AI system intended purpose? | |
| What type of AI is it (predictive, generative, agentic)? | |
| What data is used for training? Is it proprietary or public? | |
| What is the model architecture? | |
| How often is the model retrained? | |

### Section 2: Bias & Fairness

| Question | Details |
|----------|---------|
| Has the vendor conducted bias testing across protected attributes? | |
| What bias metrics are used (e.g., disparate impact ratio, equalized odds)? | |
| What are the results of bias testing? | |
| What mitigations are in place for identified biases? | |
| Has the vendor been subject to any discrimination lawsuits? | |

### Section 3: Data Privacy

| Question | Details |
|----------|---------|
| What data does the vendor collect from NovaTech? | |
| Is the data used to train the vendor's models? | |
| How is the data stored, encrypted, and secured? | |
| Does the vendor comply with GDPR, CCPA, and other privacy regulations? | |
| Does the vendor have a data processing agreement? | |

### Section 4: Security

| Question | Details |
|----------|---------|
| Is the vendor SOC 2 Type II and/or ISO 27001 certified? | |
| What security controls are in place (encryption, access controls, MFA)? | |
| Does the vendor have a bug bounty or vulnerability disclosure program? | |
| Has the vendor experienced any security incidents in the last 3 years? | |
| Does the vendor provide audit rights to customers? | |

### Section 5: Regulatory Compliance

| Question | Details |
|----------|---------|
| Is the vendor compliant with EU AI Act obligations? | |
| Does the vendor provide Annex IV technical documentation? | |
| Is the vendor registered in the EU AI Act database? | |
| Does the vendor comply with US state AI laws (Colorado, California, NY)? | |

### Section 6: Incident Response & Business Continuity

| Question | Details |
|----------|---------|
| Does the vendor have an incident response plan? | |
| Is NovaTech notified of incidents within 24 hours? | |
| What is the vendor's service level agreement (SLA)? | |
| Does the vendor have a business continuity and disaster recovery plan? | |
| What is the vendor's exit strategy? | |

---

## 5. Vendor Monitoring & Oversight

### 5.1 Ongoing Monitoring Requirements

| Monitoring Activity | Frequency | Owner |
|---------------------|-----------|-------|
| Performance monitoring | Continuous | ML Ops |
| Security review | Quarterly | CISO |
| Compliance review | Quarterly | Compliance |
| Vendor re-assessment | Annual | Procurement |
| Incident report review | Upon incident | AI Risk WG |

### 5.2 Key Risk Indicators (KRIs) for Vendors

| KRI | Threshold | Action |
|-----|-----------|--------|
| Model accuracy drop | > 5% decline | Investigate |
| Bias metric drift | DIR < 80% | Remediate |
| Security incident | Any | Escalate |
| Compliance violation | Any | Escalate |
| SLA breach | > 2 breaches/month | Review |

---

## 6. Vendor Termination & Exit

### 6.1 Termination Triggers

| Trigger | Action |
|---------|--------|
| Material security incident | Immediate vendor pause |
| Regulatory violation | Immediate termination |
| Service quality degradation | 30-day remediation period; termination if unresolved |
| Acquisition by competitor | Review and potential termination |

### 6.2 Exit Plan Requirements

| Requirement | Description |
|-------------|-------------|
| **Data Extraction** | Ability to extract all NovaTech data from vendor systems |
| **Model Handover** | For custom models, vendor must provide model artifacts |
| **Knowledge Transfer** | Vendor must provide documentation and training on decommissioning |
| **Contractual Termination** | Clear notice periods and termination clauses in contract |

---

## 7. Vendor Inventory

| Vendor | System | Risk Tier | Assessment Date | Next Review |
|--------|--------|-----------|-----------------|-------------|
| OpenAI | GPT-4 API | Medium | March 2026 | March 2027 |
| Anthropic | Claude API | Medium | June 2026 | June 2027 |
| AWS | SageMaker | Low | Jan 2026 | Jan 2027 |
| DataRobot | MLOps Platform | Low | Feb 2026 | Feb 2027 |
