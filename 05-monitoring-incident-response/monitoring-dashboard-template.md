# NovaTech Financial Group
## AI Monitoring Dashboard — Key Risk Indicators (KRIs)

**Document ID:** OPS-MON-2026-001

**Effective Date:** 1 June 2026

**Owner:** ML Ops + Model Risk

---

## 1. Purpose

This document defines the Key Risk Indicators (KRIs) and monitoring dashboards for NovaTech's AI systems. The dashboard enables real-time visibility into AI system health, performance, and risk posture.

---

## 2. Dashboard Structure

### 2.1 Executive Summary View

| Metric | Current | Threshold | Status |
|--------|---------|-----------|--------|
| **Total AI Systems** | 47 | — | — |
| **High-Risk Systems** | 11 | — | — |
| **Systems with Active Alerts** | 3 | < 5 | ✅ OK |
| **Open Incidents** | 2 | < 5 | ✅ OK |
| **Systems in Compliance** | 42 of 47 | > 90% | ✅ OK |

### 2.2 System-Specific Dashboard (CreditIQ Example)

| KRI | Current Value | Threshold | Status | Trend |
|-----|---------------|-----------|--------|-------|
| **Model Accuracy** | 87.4% | > 85% | ✅ OK | Stable |
| **False Positive Rate** | 3.8% | < 4.0% | ✅ OK | Improving |
| **Disparate Impact Ratio (Race)** | 74% | > 80% | 🔴 ALERT | Degrading |
| **Data Drift (PSI)** | 0.12 | < 0.1 | 🟡 WARNING | Stable |
| **Latency (p95)** | 280ms | < 500ms | ✅ OK | Stable |
| **User Complaints (Monthly)** | 8 | < 10 | ✅ OK | Stable |
| **Human Override Rate** | 15% | — | — | Stable |

### 2.3 Fairness Dashboard

| System | Protected Attribute | DIR | Threshold | Status |
|--------|---------------------|-----|-----------|--------|
| CreditIQ | Race | 74% | > 80% | 🔴 ALERT |
| CreditIQ | Gender | 89% | > 80% | ✅ OK |
| RecruitAI | Race | 78% | > 80% | 🟡 WARNING |
| InsureScore | Age | 82% | > 80% | ✅ OK |

---

## 3. KRI Definitions

### 3.1 Performance Metrics

| KRI | Definition | Calculation | Threshold |
|-----|------------|-------------|-----------|
| **Model Accuracy** | % of correct predictions | (TP+TN)/(TP+TN+FP+FN) | > 85% |
| **False Positive Rate (FPR)** | % of false positives | FP/(FP+TN) | < 4% |
| **AUC-ROC** | Area Under ROC Curve | Model metric | > 0.80 |
| **Latency (p95)** | 95th percentile response time | System metric | < 500ms |
| **Throughput** | Requests per minute | System metric | > 1000/min |

### 3.2 Fairness Metrics

| KRI | Definition | Calculation | Threshold |
|-----|------------|-------------|-----------|
| **Disparate Impact Ratio** | Ratio of favorable outcomes | (Approval rate Group A)/(Approval rate Group B) | > 80% |
| **Demographic Parity** | Equal approval rates across groups | Difference in approval rates | < 5% |
| **Equalized Odds** | Equal FPR and TPR across groups | Model metric | < 5% difference |

### 3.3 Drift Metrics

| KRI | Definition | Calculation | Threshold |
|-----|------------|-------------|-----------|
| **Population Stability Index (PSI)** | Distribution shift | ∑(Actual - Expected) * ln(Actual/Expected) | < 0.1 |
| **Concept Drift** | Model performance decay | Accuracy decline over time | < 5% |
| **Data Freshness** | Age of training data | Last training date | < 6 months |

### 3.4 Operational Metrics

| KRI | Definition | Threshold |
|-----|------------|-----------|
| **Human Override Rate** | % of decisions overridden | Varies by system |
| **Incident Count** | Number of incidents | < 5/month |
| **User Complaints** | Complaints related to AI decisions | < 10/month |
| **Compliance Gaps** | Missing regulatory documentation | 0 |

---

## 4. Alerting Rules

### 4.1 Alert Levels

| Alert Level | Color | Action |
|-------------|-------|--------|
| **Critical** | 🔴 Red | Immediate escalation; page on-call engineer |
| **Warning** | 🟡 Yellow | Review within 2 hours; create ticket |
| **Info** | 🔵 Blue | Document and monitor |

### 4.2 Alert Rules (CreditIQ Example)

| KRI | Critical Alert | Warning Alert |
|-----|----------------|---------------|
| **DIR (Race)** | < 70% | < 75% |
| **PSI** | > 0.2 | > 0.1 |
| **FPR** | > 5% | > 4% |
| **Latency (p95)** | > 1000ms | > 500ms |
| **Accuracy** | < 80% | < 85% |

---

## 5. Monitoring Frequency

| Metric | Frequency | Owner |
|--------|-----------|-------|
| **Performance Metrics** | Real-time (every 5 min) | ML Ops |
| **Drift Metrics** | Daily | ML Ops |
| **Fairness Metrics** | Weekly | Model Risk |
| **Incident Review** | Monthly | AI Risk WG |
| **Full System Review** | Quarterly | System Owner |

---

## 6. Dashboard Examples

### CreditIQ Dashboard Snapshot
┌──────────────────────────────────────────────────────────────────┐
│ CREDITIQ — AI SYSTEM MONITORING DASHBOARD │
│ Last Updated: 15 Aug 2026 14:32 UTC │
├──────────────────────────────────────────────────────────────────┤
│ Health: 🟡 WARNING │
│ Systems: 1 Alert │
│ Uptime: 99.97% │
├──────────────────────────────────────────────────────────────────┤
│ 🔴 CRITICAL: Disparate Impact Ratio (Race) │
│ Current: 74% | Threshold: 80% | Status: Degrading │
├──────────────────────────────────────────────────────────────────┤
│ 🟡 WARNING: Data Drift (PSI) │
│ Current: 0.12 | Threshold: 0.1 | Status: Stable │
├──────────────────────────────────────────────────────────────────┤
│ ✅ OK: Performance & Security │
│ Accuracy: 87.4% | FPR: 3.8% | Latency: 280ms │
├──────────────────────────────────────────────────────────────────┤
│ Incident Count: 2 (YTD) | Open: 0 │
└──────────────────────────────────────────────────────────────────┘
