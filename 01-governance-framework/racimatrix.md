# NovaTech Financial Group
## AI Governance — RACI Matrix

**Document ID:** GOV-RACI-2026-001

**Effective Date:** 1 March 2026

**Owner:** Chief AI Officer (CAIO)

---

## 1. Purpose

This document defines the **RACI** (Responsible, Accountable, Consulted, Informed) matrix for AI governance at NovaTech Financial Group. It ensures clear ownership and accountability across all AI-related activities.

---

## 2. RACI Definitions

| Code | Meaning | Description |
|------|---------|-------------|
| **R** | Responsible | The person who performs the work to complete the task |
| **A** | Accountable | The person ultimately answerable for the task outcome (only one "A" per task) |
| **C** | Consulted | The person whose input is required before the task is completed |
| **I** | Informed | The person who must be kept up-to-date on task progress |

---

## 3. AI System Lifecycle RACI

### 3.1 Design & Planning Phase

| Activity | AI Engineer | Product Manager | Model Risk | Compliance | Privacy | Security | Legal | AI CoE | Business Owner |
|----------|-------------|-----------------|------------|------------|---------|----------|-------|--------|----------------|
| Define AI use case | R | A | C | I | I | I | I | C | C |
| Complete UCCF classification | R | A | C | C | I | I | I | C | C |
| Document system context | R | A | C | I | I | I | I | C | C |
| Define fairness criteria | R | C | A | C | C | I | I | C | I |
| Data lineage documentation | R | I | C | C | A | I | I | C | I |

### 3.2 Build & Development Phase

| Activity | AI Engineer | Product Manager | Model Risk | Compliance | Privacy | Security | Legal | AI CoE | Business Owner |
|----------|-------------|-----------------|------------|------------|---------|----------|-------|--------|----------------|
| Model development | R | C | C | I | I | C | I | C | I |
| Secure coding standards | R | I | I | I | I | A | I | C | I |
| AI-BOM maintenance | R | I | I | I | I | C | I | C | I |
| Training data processing | R | I | C | C | A | C | I | C | I |

### 3.3 Test & Validation Phase

| Activity | AI Engineer | Product Manager | Model Risk | Compliance | Privacy | Security | Legal | AI CoE | Business Owner |
|----------|-------------|-----------------|------------|------------|---------|----------|-------|--------|----------------|
| Performance validation | R | I | A | I | I | I | I | C | I |
| Bias testing | R | I | A | C | C | I | I | C | I |
| Security testing | R | I | I | I | I | A | I | C | I |
| AI Risk Assessment (AIRA) | C | C | R | A | C | C | C | C | C |
| AIRA sign-off | I | I | A | C | C | I | C | C | C |

### 3.4 Deployment & Monitoring Phase

| Activity | AI Engineer | Product Manager | Model Risk | Compliance | Privacy | Security | Legal | AI CoE | Business Owner |
|----------|-------------|-----------------|------------|------------|---------|----------|-------|--------|----------------|
| Deployment approval | R | C | C | A | C | C | C | C | C |
| Human oversight implementation | R | A | C | C | I | I | C | C | C |
| Continuous monitoring | R | I | A | C | C | C | I | C | C |
| Incident detection & response | R | C | C | A | C | C | C | C | C |
| Post-market monitoring | R | I | A | C | C | I | I | C | C |

### 3.5 Regulatory & Audit Activities

| Activity | AI Engineer | Product Manager | Model Risk | Compliance | Privacy | Security | Legal | AI CoE | Business Owner |
|----------|-------------|-----------------|------------|------------|---------|----------|-------|--------|----------------|
| EU AI Act documentation | C | C | C | A | C | I | C | R | I |
| Bias audit (external) | I | I | C | A | C | I | C | C | I |
| Regulatory inquiry response | C | I | C | A | C | C | R | C | C |
| Internal audit | I | I | C | C | C | C | C | A | I |
| ISO 42001 certification | C | I | C | A | C | C | C | R | I |

---

## 4. Key Responsibilities by Role

### 4.1 Executive Roles

| Role | Primary AI Responsibilities |
|------|------------------------------|
| **Chief AI Officer** | Overall AI governance program ownership, AI Council Chair, Board liaison |
| **Chief Risk Officer** | Risk appetite setting, model risk oversight, regulatory engagement |
| **Chief Information Security Officer** | AI security controls, vulnerability management, incident response |
| **Chief Privacy Officer** | Data privacy compliance, GDPR/CCPA oversight, data protection impact assessments |
| **General Counsel** | Regulatory interpretation, legal risk, enforcement response |
| **Chief Data Officer** | Data governance, data quality, data lineage |

### 4.2 Operational Roles

| Role | Primary AI Responsibilities |
|------|------------------------------|
| **Head of Model Risk** | Independent model validation, AI Risk Assessments, bias testing oversight |
| **Head of AI Engineering** | AI development standards, secure coding, technical implementation |
| **AI Compliance Officer** | EU AI Act documentation, regulatory filings, compliance monitoring |
| **Business Unit Lead** | AI system business ownership, resource allocation, risk acceptance |
| **AI Risk Working Group** | Operational risk management, control implementation, incident triage |

---

## 5. Escalation Paths

| Scenario | Escalation Path |
|----------|-----------------|
| **Classification dispute** | AI Risk Working Group → AI Governance Council |
| **Material risk finding** | Model Risk → Head of Model Risk → AI Governance Council |
| **Major incident** | Incident Response Team → CISO/CAIO → AI Governance Council |
| **Regulatory inquiry** | Legal → General Counsel → AI Governance Council |
| **Audit finding** | Internal Audit → Audit Committee → Board |
