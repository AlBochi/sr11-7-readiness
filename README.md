# SR 11-7 Readiness Framework

A self-assessment framework for SR 11-7 model risk management compliance. Built for US banks, credit unions, and financial institutions supervised by the Federal Reserve and OCC.

## What It Does

- Provides a structured SR 11-7 self-assessment questionnaire
- Maps requirements to Saillent's five-tier governance framework
- Generates a readiness score across model inventory, validation, monitoring, and governance
- Identifies gaps before regulatory examinations

## Quick Start

git clone https://github.com/AlBochi/sr11-7-readiness.git
cd sr11-7-readiness
pip install -r requirements.txt
python assess.py --institution "Your Bank Name"

## Sample Readiness Report

| SR 11-7 Domain | Readiness Score | Critical Gaps |
|----------------|----------------|---------------|
| Model Inventory | 78% | Shadow AI not tracked |
| Independent Validation | 62% | No external validator engaged |
| Ongoing Monitoring | 45% | No real-time dashboard |
| Board Governance | 81% | Committee charter complete |

## Regulatory Alignment

- SR 11-7 (full guidance coverage)
- OCC Model Risk Management Handbook
- FDIC AI/ML Examination Guidance
- CFPB Fair Lending AI Standards

## Status

Proof of concept by Saillent.

## License

MIT
