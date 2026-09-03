# NovaTech Financial Group
## AI Risk Assessment (AIRA) — InsureScore

**Document ID:** AIRA-INS-2026-001 (Draft)

**Assessment Date:** TBD

**Next Review Due:** TBD

**Assessor:** AI Risk Working Group

---

## 1. System Overview

| Attribute | Detail |
|-----------|--------|
| **System Name** | InsureScore |
| **Business Owner** | SVP, Insurance |
| **Technical Owner** | Lead ML Engineer |
| **Intended Purpose** | Automate insurance risk pricing and premium calculation |
| **Model Type** | Gradient Boosting Ensemble |
| **Decision Authority** | Fully automated pricing recommendations (human review for exceptions) |
| **Deployment Jurisdictions** | USA, UK, EU |
| **Affected Population** | ~500,000 insurance applicants annually |

---

## 2. Risk Classification

| Dimension | Classification | Rationale |
|-----------|----------------|-----------|
| **EU AI Act** | **High-Risk (Annex III, Point 5a)** | Determines insurance pricing and access |
| **NIST AI RMF** | **High** | Impacts individual financial well-being |
| **GDPR Art. 22** | **Solely Automated Decision-Making** | Legal/economic effects |

---

## 3. Key Risks Identified

| Risk ID | Risk Description | Inherent Risk |
|---------|------------------|---------------|
| **INS-R01** | **Algorithmic Bias** — Pricing discrimination based on protected characteristics | **Critical** |
| **INS-R02** | **Proxy Discrimination** — Use of zip codes as proxy for race/income | **Critical** |
| **INS-R03** | **Explainability** — Complex ensemble model difficult to explain to regulators | **High** |
| **INS-R04** | **Data Quality** — Historical insurance data contains biases | **High** |

---

## 4. Required Mitigations

| Risk ID | Mitigation | Owner | Target |
|---------|------------|-------|--------|
| **INS-R01** | Fairness constraint during training | Model Risk | Q1 2027 |
| **INS-R02** | Remove proxy variables; use direct protected attributes only for monitoring | Data Scientist | Q1 2027 |
| **INS-R03** | Implement SHAP explanations; train simpler fallback model | ML Ops | Q2 2027 |
| **INS-R04** | Data quality review; address historical bias | Data Governance | Q1 2027 |

---

## 5. Status

- **Draft:** 8 September 2026
- **Under Review:** AI Risk Working Group
- **Expected Completion:** Q4 2026
