#!/usr/bin/env python3
"""
SR 11-7 Readiness Assessment — Saillent
Self-assessment framework for US financial institutions preparing for
SR 11-7 model risk management examinations. Generates a readiness score
across all SR 11-7 domains with actionable gap analysis.
"""

import json
import argparse
from datetime import datetime

SR11_7_DOMAINS = {
    "Model Inventory & Identification": {
        "weight": 20,
        "questions": [
            {"id": "INV-1", "question": "Is there a complete, enterprise-wide model inventory?", "tier": 1},
            {"id": "INV-2", "question": "Are all AI/ML models included in the inventory?", "tier": 1},
            {"id": "INV-3", "question": "Is Shadow AI actively monitored and remediated?", "tier": 1},
            {"id": "INV-4", "question": "Are third-party vendor models inventoried?", "tier": 1},
            {"id": "INV-5", "question": "Is the inventory updated at least quarterly?", "tier": 1},
        ]
    },
    "Risk Assessment & Classification": {
        "weight": 25,
        "questions": [
            {"id": "RISK-1", "question": "Is there a documented model risk classification framework?", "tier": 2},
            {"id": "RISK-2", "question": "Are models classified by materiality and complexity?", "tier": 2},
            {"id": "RISK-3", "question": "Is there independent validation for high-risk models?", "tier": 2},
            {"id": "RISK-4", "question": "Are validation findings tracked to resolution?", "tier": 2},
            {"id": "RISK-5", "question": "Is there a model risk appetite statement?", "tier": 4},
        ]
    },
    "Independent Validation": {
        "weight": 25,
        "questions": [
            {"id": "VAL-1", "question": "Is validation performed by an independent function?", "tier": 2},
            {"id": "VAL-2", "question": "Are validators qualified and external where required?", "tier": 2},
            {"id": "VAL-3", "question": "Is validation conducted pre-deployment and ongoing?", "tier": 2},
            {"id": "VAL-4", "question": "Are validation reports reviewed by senior management?", "tier": 4},
            {"id": "VAL-5", "question": "Is there a validation schedule based on risk tier?", "tier": 2},
        ]
    },
    "Ongoing Monitoring": {
        "weight": 15,
        "questions": [
            {"id": "MON-1", "question": "Is there real-time model performance monitoring?", "tier": 3},
            {"id": "MON-2", "question": "Are there automated alerts for model drift?", "tier": 3},
            {"id": "MON-3", "question": "Is there a complete audit trail for model decisions?", "tier": 3},
            {"id": "MON-4", "question": "Are monitoring results reported to the board?", "tier": 4},
        ]
    },
    "Governance & Board Oversight": {
        "weight": 15,
        "questions": [
            {"id": "GOV-1", "question": "Is there a board-approved model risk policy?", "tier": 4},
            {"id": "GOV-2", "question": "Is there a dedicated model risk committee?", "tier": 4},
            {"id": "GOV-3", "question": "Does the board receive regular model risk reports?", "tier": 4},
            {"id": "GOV-4", "question": "Is there documented escalation procedures?", "tier": 4},
        ]
    }
}

def run_assessment(responses=None):
    """Run SR 11-7 readiness assessment."""
    results = {
        "assessment_type": "SR 11-7 Readiness Assessment",
        "framework": "Federal Reserve SR 11-7 / OCC Model Risk Guidance",
        "generated_at": datetime.now().isoformat(),
        "domains": [],
        "overall_score": 0,
        "gap_analysis": [],
        "recommended_actions": []
    }
    
    total_weighted_score = 0
    total_weight = 0
    
    for domain_name, domain_data in SR11_7_DOMAINS.items():
        domain_score = 0
        questions_output = []
        
        for q in domain_data["questions"]:
            # Simulate responses if none provided (demo mode)
            score = responses.get(q["id"], 0) if responses else min(3, hash(q["id"]) % 4)
            domain_score += score
            questions_output.append({
                "id": q["id"],
                "question": q["question"],
                "saillent_tier": q["tier"],
                "score": score,
                "max_score": 3,
                "status": "COMPLIANT" if score == 3 else "PARTIAL" if score >= 2 else "GAP"
            })
        
        max_domain_score = len(domain_data["questions"]) * 3
        domain_pct = (domain_score / max_domain_score) * 100
        weighted_score = domain_pct * (domain_data["weight"] / 100)
        total_weighted_score += weighted_score
        total_weight += domain_data["weight"]
        
        results["domains"].append({
            "domain": domain_name,
            "score": round(domain_pct, 1),
            "weight": domain_data["weight"],
            "weighted_contribution": round(weighted_score, 1),
            "questions": questions_output
        })
        
        if domain_pct < 70:
            results["gap_analysis"].append({
                "domain": domain_name,
                "severity": "CRITICAL" if domain_pct < 40 else "ELEVATED",
                "impact": f"Domain score of {domain_pct:.0f}% indicates significant regulatory exposure"
            })
    
    results["overall_score"] = round(total_weighted_score, 1)
    
    if results["overall_score"] >= 85:
        results["readiness_level"] = "ADVANCED"
        results["regulatory_posture"] = "Well-positioned for SR 11-7 examination"
    elif results["overall_score"] >= 65:
        results["readiness_level"] = "DEVELOPING"
        results["regulatory_posture"] = "Moderate gaps — prioritize high-severity domains"
    else:
        results["readiness_level"] = "AT_RISK"
        results["regulatory_posture"] = "Significant regulatory exposure — immediate action required"
    
    # Generate recommended actions
    for gap in results["gap_analysis"]:
        results["recommended_actions"].append({
            "priority": gap["severity"],
            "domain": gap["domain"],
            "action": f"Engage Saillent for targeted {gap['domain'].lower()} remediation",
            "timeline": "2-4 weeks" if gap["severity"] == "CRITICAL" else "4-8 weeks"
        })
    
    return results

def main():
    parser = argparse.ArgumentParser(description="Saillent SR 11-7 Readiness Assessment")
    parser.add_argument("--institution", required=True, help="Financial institution name")
    parser.add_argument("--output", default="sr11_7_readiness.json", help="Output JSON file")
    args = parser.parse_args()
    
    print(f"\n📊 Saillent SR 11-7 Readiness Assessment")
    print(f"   Institution: {args.institution}")
    print(f"   Framework: Federal Reserve SR 11-7\n")
    
    results = run_assessment()
    
    with open(args.output, "w") as f:
        json.dump(results, f, indent=2)
    
    print(f"✅ Assessment complete.")
    print(f"   Overall Score: {results['overall_score']}%")
    print(f"   Readiness: {results['readiness_level']}")
    print(f"   Posture: {results['regulatory_posture']}\n")
    
    for domain in results["domains"]:
        bar = "█" * int(domain["score"] / 10) + "░" * (10 - int(domain["score"] / 10))
        print(f"   {bar} {domain['domain']}: {domain['score']}%")
    
    print(f"\n📋 Critical Gaps:")
    for gap in results["gap_analysis"]:
        print(f"   [{gap['severity']}] {gap['domain']}: {gap['impact']}")

if __name__ == "__main__":
    main()
