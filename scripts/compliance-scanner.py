

#!/usr/bin/env python3
"""
=========
1. Reads a sample cloud configuration (JSON/YAML)

2. Checks it against NIST AI RMF controls

3. Outputs a compliance report
=========
Compliance Scanner — Simulates policy-as-code enforcement
for NIST AI RMF controls.
"""

import json
import sys

class ComplianceScanner:
    def __init__(self, config_path):
        with open(config_path, 'r') as f:
            self.config = json.load(f)
        self.findings = []

    def check_encryption(self):
        """Check: Data at rest must be encrypted (NIST AI RMF SECURE.1)"""
        if not self.config.get('encryption_enabled', False):
            self.findings.append({
                'control': 'SECURE.1',
                'status': 'FAIL',
                'message': 'Data at rest encryption is not enabled'
            })
        else:
            self.findings.append({
                'control': 'SECURE.1',
                'status': 'PASS',
                'message': 'Data at rest encryption is enabled'
            })

    def check_access_controls(self):
        """Check: Access controls must enforce least privilege (NIST AI RMF SECURE.2)"""
        if self.config.get('access_controls', {}).get('least_privilege', False):
            self.findings.append({
                'control': 'SECURE.2',
                'status': 'PASS',
                'message': 'Least privilege access controls are enforced'
            })
        else:
            self.findings.append({
                'control': 'SECURE.2',
                'status': 'FAIL',
                'message': 'Least privilege access controls are not enforced'
            })

    def check_bias_mitigation(self):
        """Check: Bias mitigation must be implemented (NIST AI RMF FAIRNESS.1)"""
        if self.config.get('bias_mitigation', {}).get('implemented', False):
            self.findings.append({
                'control': 'FAIRNESS.1',
                'status': 'PASS',
                'message': 'Bias mitigation is implemented'
            })
        else:
            self.findings.append({
                'control': 'FAIRNESS.1',
                'status': 'FAIL',
                'message': 'Bias mitigation is not implemented'
            })

    def run(self):
        self.check_encryption()
        self.check_access_controls()
        self.check_bias_mitigation()
        return self.generate_report()

    def generate_report(self):
        passed = sum(1 for f in self.findings if f['status'] == 'PASS')
        failed = sum(1 for f in self.findings if f['status'] == 'FAIL')
        return {
            'summary': {
                'total': len(self.findings),
                'passed': passed,
                'failed': failed,
                'compliance_score': f"{round((passed / len(self.findings)) * 100)}%"
            },
            'findings': self.findings
        }

if __name__ == "__main__":
    scanner = ComplianceScanner("sample_config.json")
    report = scanner.run()
    print(json.dumps(report, indent=2))


"""
Here, we translate compliance requirements into executable code

We understand modern GRC engineering (policy-as-code)

"""
