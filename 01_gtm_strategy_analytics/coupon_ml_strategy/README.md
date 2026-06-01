# Coupon Targeting System

A GTM-oriented decision system designed to improve coupon targeting, campaign efficiency, and promotional decision-making.

This project reframes coupon acceptance analysis as a product and business decision workflow: using customer context, visit behavior, and offer characteristics to help teams decide which offers should be delivered, to whom, and under what conditions.

## Analysis Pipeline
Customer data -> EDA and signal review -> preprocessing -> customer segmentation -> response scoring -> targeting recommendations -> campaign action

## EDA Snapshot
- Dataset shape: 12,684 driving scenarios, 25 decision signals, and a binary coupon acceptance target
- Good for: understanding customer response behavior, identifying segment-level opportunity, comparing coupon performance, and shaping targeting strategy
- Limitations: observational dataset, context-specific to in-vehicle coupon scenarios, and better suited for product and business decision support than direct causal claims

## Problem
Promotional offers are often distributed too broadly, even though customer response varies sharply by behavior, timing, and trip context. This creates a product and operations problem: low targeting precision, wasted budget, and weaker campaign performance.

## Objective
Design a targeting workflow that helps teams identify higher-value customer segments, improve offer fit, and support smarter promotional decisions.

## Workflow
Customer data -> behavioral segmentation -> response scoring -> targeting decision -> campaign action

## System Design
This project combines customer signal review, behavioral segmentation, clustering, and response scoring to create a reusable targeting framework for campaign planning and execution.

## Featured Outputs
- Behavioral segmentation and five customer personas
- Persona-aware response scoring
- Targeting recommendations by coupon type, segment, and timing
- Business-facing presentation and written report

## Key Insights
- Coupon acceptance is strongly influenced by behavioral and contextual signals, not just coupon type.
- Distinct customer personas emerge from response patterns and create more actionable targeting opportunities.
- Segment-aware delivery can outperform blanket promotional distribution by improving offer relevance.

## Business Impact
This project demonstrates how a targeting system can support better offer allocation, stronger campaign timing decisions, and more efficient GTM execution.

## PM Angle
- Defines a clear user and business problem around promotional inefficiency
- Converts raw response data into segment-driven targeting logic
- Connects analytics outputs to product and campaign decisions
- Creates a reusable framework that could evolve into a rules engine, dashboard, or internal targeting tool

## Repository Structure
```text
coupon_ml_strategy/
├── README.md
├── data/
├── notebooks/
├── src/
├── figures/
├── reports/
├── presentations/
├── docs/
└── archive/
```

## Slides
- Download as PDF: `presentations/coupon-targeting-system-presentation.pdf`
- Download as PPTX: `presentations/Group9_invehicle_coupon_strategy_presentation.pptx`

## Key Files
- `notebooks/coupon-targeting-decision-system.ipynb`: end-to-end notebook workflow
- `reports/coupon-targeting-system-report.pdf`: written project summary and findings
- `data/in-vehicle-coupon-dataset.csv`: source dataset
- `src/identify_optimal_k_report.py`: clustering support analysis
- `src/kmeans_k_selection.py`: K-means selection and workflow support
- `figures/k_selection_plots.png`: clustering selection visual

## Supporting Materials
- `docs/`: presentation rewrite notes and core-deck planning
- `archive/`: source materials and earlier working documents

## Future Improvements
- Add supervised prediction models for coupon acceptance
- Compare segmentation approaches across methods
- Build a lightweight decision dashboard for business users
- Translate findings into a deployable targeting workflow
