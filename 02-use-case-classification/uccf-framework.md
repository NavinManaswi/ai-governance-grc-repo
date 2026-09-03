# NovaTech Financial Group
## Use Case Classification Framework (UCCF)

**Document ID:** GOV-UCCF-2026-002 (Rev. 2)

**Effective Date:** 1 March 2026

**Owner:** AI Governance Council

**Applies To:** All new AI/ML initiatives, material changes to existing systems, and third-party AI procurements

---

## 1. Framework Purpose

To provide a standardized, auditable, and repeatable methodology for categorizing every AI use case at NovaTech into one of four regulatory/risk tiers. This framework ensures:

- **Regulatory Obligations** are triggered automatically
- **Resource Allocation** is proportionate to risk
- **Audit Defensibility** is maintained (every classification decision is logged with rationale and sign-off)

**The "Zero-Tolerance" Principle:** Any use case exhibiting prohibited practices (EU AI Act Art. 5) is immediately rejected.

---

## 2. The Four Classification Tiers

| Tier | Regulatory Name | NovaTech Definition | Examples |
|------|-----------------|---------------------|----------|
| **Tier 0** | Unacceptable Risk | Prohibited practices | Social scoring, manipulative AI, real-time biometric identification |
| **Tier 1** | High-Risk | AI that materially affects financial well-being, essential services, or legal/employment status | CreditIQ, InsureScore, RecruitAI |
| **Tier 2** | Limited-Risk | AI that interacts with humans or generates content | Customer chatbots, AI-generated marketing |
| **Tier 3** | Minimal-Risk | Internal, non-customer-facing AI with zero impact on rights or finances | IT ticketing, spam filtering |

---

## 3. The Triple-Gate Classification Methodology

### Gate 1: The "Absolute Prohibition" Filter

**If the answer to ANY of these questions is "YES," the use case is REJECTED immediately.**

| Question | Rationale (EU AI Act Art. 5) |
|----------|------------------------------|
| Does the system deploy subliminal, manipulative, or deceptive techniques to distort user behavior causing harm? | Bans manipulative/harmful subliminal techniques |
| Does the system exploit vulnerabilities of a specific group to materially distort behavior? | Bans exploitation of vulnerable populations |
| Does the system assign a "social score" to individuals leading to detrimental/unfavorable treatment? | Bans social scoring |
| Does the system involve real-time, remote biometric identification in publicly accessible spaces for law enforcement? | Bans real-time remote biometric identification in public spaces |

### Gate 2: The "High-Risk Trigger" Matrix

**If ANY condition below is triggered, the use case is provisionally classified as Tier 1 (High-Risk).**

| Risk Vector | Assessment Question | Financial Services Context |
|-------------|---------------------|----------------------------|
| **Vector A: Essential Services** | Does the system determine access to, or pricing of, essential financial services? | Credit scoring, mortgage approval, insurance pricing |
| **Vector B: Employment** | Does the system make decisions regarding recruitment, promotion, or termination? | Resume screening, performance ranking |
| **Vector C: Legal Rights** | Does the system evaluate individuals in a manner that could restrict legal rights? | Fraud scoring used for legal holds |
| **Vector D: Autonomy & Harm** | Is the system fully autonomous AND could a wrong decision result in financial loss >$5,000? | Automated trading algorithms |
| **Vector E: Systemic Scale** | Does the system affect >100,000 individuals per year within EU/UK? | High-volume scoring models |

### Gate 3: The "Human Interaction & Transparency" Test

**If any condition below is triggered, the use case is classified as Tier 2 (Limited-Risk).**

| Question | If YES → Tier 2 | If NO → Tier 3 |
|----------|-----------------|----------------|
| Does the system directly interact with external customers via text, voice, or image? | Yes — requires Art. 50 transparency | Internal tool |
| Does the system generate synthetic content disseminated externally? | Yes — must watermark AI-generated content | Internal content |
| Does the system process biometric data for authentication? | Yes — requires enhanced privacy controls | No biometrics |

---

## 4. Classification Decision Matrix

| Gate 1 (Prohibited) | Gate 2 (High-Risk Vectors) | Gate 3 (Human/Content Interaction) | Final Tier |
|---------------------|----------------------------|------------------------------------|------------|
| **YES** | N/A | N/A | ❌ UNACCEPTABLE (REJECTED) |
| NO | **YES (Any)** | N/A | 🔴 TIER 1 — HIGH-RISK |
| NO | NO | **YES (Any)** | 🟡 TIER 2 — LIMITED-RISK |
| NO | NO | NO | 🟢 TIER 3 — MINIMAL-RISK |

---

## 5. Jurisdictional "Amber Flags" (Elevated Scrutiny)

Even if a use case scores as Tier 2 or 3, **mandatory elevated scrutiny** applies if deployed in:

| Jurisdiction | Trigger | Required Action |
|--------------|---------|-----------------|
| **New York** | AEDT under NYC Local Law 144 | Elevate to Tier 1 for bias audit purposes |
| **Colorado** | High-risk system under SB 24-205 | Elevate to Tier 1; mandate consumer disclosure |
| **California** | Processes CCPA sensitive personal information | Elevate to Tier 2 minimum; mandate DPIA |
| **EU** | GDPR Art. 22 solely automated decision-making | Elevate to Tier 1; mandate human intervention rights |

---

## 6. Classification Governance

| Role | Responsibility |
|------|----------------|
| **Submitting Party** | Fills out the UCCF intake form, provides initial tier recommendation |
| **AI Risk Working Group** | Validates submission, reviews evidence, makes recommended classification |
| **AI Governance Council** | Formally approves classification; overrides require 2/3 majority |
| **Internal Audit** | Quarterly random sampling to ensure under-classification does not occur |

---

## 7. Practical Application

| Use Case | Gate 1 | Gate 2 | Gate 3 | Final Tier | Rationale |
|----------|--------|--------|--------|------------|-----------|
| CreditIQ | Pass | **YES** — Vector A & E | N/A | **Tier 1** | Access to credit; scale >100k |
| NovaChat | Pass | NO | **YES** — Customer interaction | **Tier 2** | Customer-facing chatbot |
| Internal Meeting Scheduler | Pass | NO | NO | **Tier 3** | Internal, no rights impact |
| Social Credit Scoring | **FAIL** | N/A | N/A | **REJECTED** | Prohibited practice |
