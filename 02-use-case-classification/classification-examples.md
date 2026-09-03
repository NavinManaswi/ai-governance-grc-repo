# NovaTech Financial Group
## UCCF Classification Examples

**Document ID:** GOV-UCCF-EXAMPLES-2026-001

**Effective Date:** 1 March 2026

**Owner:** AI Governance Council

---

## 1. Example 1: CreditIQ — Automated Credit Underwriting

### UCCF Intake Form Summary

| Field | Value |
|-------|-------|
| **System Name** | CreditIQ |
| **Business Unit** | Retail Lending |
| **Intended Purpose** | Automate creditworthiness scoring for personal loans |
| **Deployment Jurisdictions** | USA, UK, EU |
| **Estimated Users** | 2.4 million applicants annually |
| **Decision Authority** | Fully automated (with human review for borderline cases) |

### Gate 1: Absolute Prohibition Filter

| Question | Answer | Pass/Fail |
|----------|--------|-----------|
| Manipulative/deceptive techniques? | No | ✅ Pass |
| Exploits vulnerable groups? | No | ✅ Pass |
| Social scoring? | No | ✅ Pass |
| Real-time biometric identification? | No | ✅ Pass |

**Gate 1 Result:** ✅ PASS — Proceed to Gate 2

### Gate 2: High-Risk Trigger Matrix

| Risk Vector | Assessment | Triggered? |
|-------------|------------|------------|
| **Vector A: Essential Services** | Determines access to credit — an essential financial service | ✅ **YES** |
| **Vector B: Employment** | Not used for employment decisions | ❌ No |
| **Vector C: Legal Rights** | Does not restrict legal rights directly | ❌ No |
| **Vector D: Autonomy & Harm** | Fully automated for 85% of cases; potential financial harm >$5,000 | ✅ **YES** |
| **Vector E: Systemic Scale** | Affects >2.4M applicants annually (EU/UK: ~500k) | ✅ **YES** |

**Gate 2 Result:** 🔴 **TIER 1 — HIGH-RISK**

### Gate 3: Human Interaction & Transparency Test

*(Not applicable — already Tier 1)*

### Final Classification

| Tier | Classification | Approved By | Date |
|------|----------------|-------------|------|
| **TIER 1 — HIGH-RISK** | 🔴 CreditIQ | AI Governance Council | 1 March 2026 |

### Required Actions

- ✅ Complete AI Risk Assessment (AIRA) before deployment
- ✅ Implement human oversight for borderline cases
- ✅ Conduct annual independent bias audits
- ✅ Register in EU AI Act database
- ✅ Maintain Annex IV technical documentation

---

## 2. Example 2: NovaChat — Customer Service Chatbot

### UCCF Intake Form Summary

| Field | Value |
|-------|-------|
| **System Name** | NovaChat |
| **Business Unit** | Wealth Management |
| **Intended Purpose** | Answer customer questions about products and services |
| **Deployment Jurisdictions** | All markets |
| **Estimated Users** | 500,000 customers annually |
| **Decision Authority** | No autonomous decisions; routes complex issues to humans |

### Gate 1: Absolute Prohibition Filter

**Result:** ✅ PASS (No prohibited practices)

### Gate 2: High-Risk Trigger Matrix

| Risk Vector | Assessment | Triggered? |
|-------------|------------|------------|
| **Vector A: Essential Services** | Does not determine access to services | ❌ No |
| **Vector B: Employment** | Not used for employment | ❌ No |
| **Vector C: Legal Rights** | No legal rights impact | ❌ No |
| **Vector D: Autonomy & Harm** | Not fully autonomous; routes to humans | ❌ No |
| **Vector E: Systemic Scale** | Affects >100k, but no high-risk use | ❌ No |

**Gate 2 Result:** ✅ PASS — Proceed to Gate 3

### Gate 3: Human Interaction & Transparency Test

| Question | Answer | Result |
|----------|--------|--------|
| Interacts with external customers? | Yes — text-based chatbot | ✅ Triggers Tier 2 |
| Generates synthetic content externally? | No — uses canned responses | ❌ No |
| Processes biometric data? | No | ❌ No |

**Gate 3 Result:** 🟡 **TIER 2 — LIMITED-RISK**

### Final Classification

| Tier | Classification | Approved By | Date |
|------|----------------|-------------|------|
| **TIER 2 — LIMITED-RISK** | 🟡 NovaChat | AI Risk Working Group | 1 March 2026 |

### Required Actions

- ✅ Implement Art. 50 transparency disclosure ("You are interacting with an AI assistant")
- ✅ Provide clear information about AI capabilities and limitations
- ✅ Ensure human escalation path for complex issues

---

## 3. Example 3: Internal Meeting Scheduler

### UCCF Intake Form Summary

| Field | Value |
|-------|-------|
| **System Name** | SmartScheduler |
| **Business Unit** | IT Operations |
| **Intended Purpose** | Automatically schedule internal meetings based on calendar availability |
| **Deployment Jurisdictions** | Internal only |
| **Estimated Users** | 15,000 employees |
| **Decision Authority** | Fully automated (no human review) |

### Gate 1: Absolute Prohibition Filter

**Result:** ✅ PASS

### Gate 2: High-Risk Trigger Matrix

| Risk Vector | Assessment | Triggered? |
|-------------|------------|------------|
| **Vector A: Essential Services** | No | ❌ No |
| **Vector B: Employment** | No | ❌ No |
| **Vector C: Legal Rights** | No | ❌ No |
| **Vector D: Autonomy & Harm** | No financial harm >$5,000 | ❌ No |
| **Vector E: Systemic Scale** | Affects >100k? No (15k employees) | ❌ No |

**Gate 2 Result:** ✅ PASS

### Gate 3: Human Interaction & Transparency Test

| Question | Answer | Result |
|----------|--------|--------|
| Interacts with external customers? | No — internal only | ❌ No |
| Generates synthetic content externally? | No | ❌ No |
| Processes biometric data? | No | ❌ No |

**Gate 3 Result:** 🟢 **TIER 3 — MINIMAL-RISK**

### Final Classification

| Tier | Classification | Approved By | Date |
|------|----------------|-------------|------|
| **TIER 3 — MINIMAL-RISK** | 🟢 SmartScheduler | AI Risk Working Group | 1 March 2026 |

### Required Actions

- ✅ Standard security controls
- ✅ Acceptable use policy compliance
- ✅ Regular patching and updates
