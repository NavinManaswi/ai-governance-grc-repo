# NovaTech Financial Group
## US State AI Law Patchwork — Compliance Mapping

**Document ID:** COMP-US-2026-001

**Effective Date:** 1 June 2026

**Owner:** Legal + AI Compliance

---

## 1. Executive Summary

The United States lacks comprehensive federal AI legislation. Instead, states are enacting their own AI laws, creating a fragmented regulatory landscape. This document maps NovaTech's compliance obligations across key states.

---

## 2. State Law Landscape Overview

| State | Law | Effective Date | Key Requirements | NovaTech Impact |
|-------|-----|----------------|------------------|-----------------|
| **New York** | NYC Local Law 144 (AEDT) | Already in effect | Annual bias audits for Automated Employment Decision Tools | RecruitAI system |
| **Colorado** | SB 26-189 (replacement of SB 24-205) | 1 January 2027 | Consumer notices, 30-day adverse outcome explanations, human review rights | All consumer-facing AI |
| **California** | AB 853 (AI Transparency Act amendments) | 1 January 2027 | Enhanced transparency and disclosure obligations | All customer-facing AI |
| **Illinois** | Various AI employment laws | Various | Bias audit and disclosure requirements | RecruitAI system |
| **Maryland** | HB 1202 (deepfake election materials) | Already in effect | Disclosure of AI-generated political content | N/A |
| **Texas** | HB 2060 (AI in healthcare) | TBD | AI transparency in healthcare decisions | N/A |

---

## 3. New York — NYC Local Law 144 (AEDT)

### 3.1 Applicability

- **Applies to:** Employers using Automated Employment Decision Tools (AEDTs) to evaluate candidates or employees
- **Applicable NovaTech Systems:** RecruitAI

### 3.2 Key Requirements

| Requirement | Description | NovaTech Status |
|-------------|-------------|-----------------|
| **Annual Bias Audit** | Independent bias audit for race, ethnicity, and sex | ✅ Completed (Q1 2026) |
| **Audit Results** | Summary results must be published on company website | ✅ Completed |
| **Candidate Notice** | Provide notice to NYC candidates before using AEDT | ✅ Completed |

### 3.3 Compliance Evidence

| Evidence Type | Location | Status |
|---------------|----------|--------|
| Bias Audit Report (2026) | `audits/recruitAI/bias-2026.pdf` | ✅ Complete |
| Website Publication | `novatech.com/ai/nyc-aedt` | ✅ Live |
| Candidate Notice | Included in application process | ✅ Implemented |

---

## 4. Colorado — SB 26-189 (AI Act)

### 4.1 Applicability

- **Applies to:** Deployers of "high-risk" AI systems in Colorado
- **Applicable NovaTech Systems:** CreditIQ, InsureScore (if deployed in Colorado)

### 4.2 Key Requirements

| Requirement | Description | NovaTech Status |
|-------------|-------------|-----------------|
| **Consumer Notice** | Notice before using high-risk AI | 🔴 Not Started |
| **Adverse Outcome Explanation** | 30-day explanation of adverse outcomes | 🔴 Not Started |
| **Human Review Rights** | Consumer right to review adverse outcomes with human | 🔴 Not Started |
| **Attorney General Enforcement** | AG can investigate and enforce | 🔴 Not Started |

### 4.3 Compliance Plan

| Action | Owner | Target Date | Status |
|--------|-------|-------------|--------|
| Map Colorado users and systems | Legal | 15 Oct 2026 | 🔴 Not Started |
| Draft consumer notice template | Product + Legal | 1 Nov 2026 | 🔴 Not Started |
| Implement adverse outcome workflows | Engineering | 15 Dec 2026 | 🔴 Not Started |
| Implement human review process | Underwriting | 15 Dec 2026 | 🔴 Not Started |

---

## 5. California — AB 853 (AI Transparency Act)

### 5.1 Applicability

- **Applies to:** Companies doing business in California that use AI to make "consequential decisions"
- **Applicable NovaTech Systems:** CreditIQ, InsureScore, RecruitAI, FraudShield

### 5.2 Key Requirements

| Requirement | Description | NovaTech Status |
|-------------|-------------|-----------------|
| **Enhanced Transparency** | Clear disclosure of AI use and decision factors | 🟡 In Progress |
| **Data Privacy** | CCPA compliance for AI data processing | ✅ Complete |
| **User Rights** | Right to know, correct, delete AI-related data | ✅ Complete |

### 5.3 Compliance Plan

| Action | Owner | Target Date | Status |
|--------|-------|-------------|--------|
| Review CCPA compliance for AI systems | Privacy Officer | 1 Oct 2026 | ✅ Complete |
| Draft California-specific disclosures | Product + Legal | 15 Oct 2026 | 🟡 In Progress |
| Implement disclosure in CA user experience | Engineering | 15 Dec 2026 | 🔴 Not Started |

---

## 6. Multi-State Compliance Strategy

### 6.1 "Most Restrictive State" Approach

NovaTech adopts the **Most Restrictive State** approach: compliance standards are set to the most stringent state requirement and applied globally where feasible.

| Requirement | Most Restrictive State | Global Standard Applied |
|-------------|----------------------|------------------------|
| **Bias Audits** | New York (annual) | ✅ Annual for all AEDTs |
| **Consumer Notices** | Colorado (pre-deployment) | ✅ All US consumers |
| **Adverse Outcome Explanations** | Colorado (30-day) | ✅ All US consumers |
| **Transparency Disclosures** | California (most comprehensive) | ✅ Global standard |

### 6.2 Regulatory Monitoring

| Activity | Frequency | Owner |
|----------|-----------|-------|
| State AI bill monitoring | Weekly | Legal |
| Impact assessment for new laws | Monthly | Legal + AI Compliance |
| Compliance gap identification | Quarterly | AI Compliance |
| Control updates | As needed | AI Risk WG |

---

## 7. Federal Landscape

### 7.1 Current Federal AI Activity

| Initiative | Status | Potential Impact |
|------------|--------|------------------|
| **US AI Accountability Act** | Proposed | Mandatory impact assessments, bias audits |
| **FTC AI Enforcement** | Active | Consumer protection authority |
| **DOJ Civil Rights** | Active | Algorithmic discrimination enforcement |
| **SEC AI Disclosure** | Finalized | Material AI risk disclosure requirements |

### 7.2 Federal Agency Guidance

| Agency | Guidance | Applicability |
|--------|----------|---------------|
| **CFPB** | AI in credit underwriting | CreditIQ |
| **FTC** | Deceptive AI practices | All AI systems |
| **DOJ** | Algorithmic discrimination | RecruitAI, CreditIQ |
| **OCC** | Model risk management | All quantitative models |
