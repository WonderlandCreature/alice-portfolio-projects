# Coupon Targeting Decision System

## Core Deck Goal
This 10-slide version is designed for portfolio and hiring use. The focus is business problem framing, system workflow, targeting logic, and decision impact, rather than course-style modeling detail.

## Slide 1
### Title
Coupon Targeting Decision System

### Subtitle
A customer segmentation and decision-support workflow for smarter promotional targeting

### Key message
This project reframes coupon acceptance analysis as a business system for better targeting and campaign execution.

## Slide 2
### Title
The Business Problem

### Key points
- Blanket coupon delivery wastes budget and reduces targeting efficiency.
- Customer response varies by behavior, timing, context, and coupon type.
- Better targeting requires a decision system, not a one-size-fits-all campaign.

### Takeaway
The problem is not just prediction. It is promotion allocation and execution quality.

## Slide 3
### Title
Decision Objective

### Key points
- Identify which customer contexts are most responsive to specific coupon types.
- Support more targeted coupon delivery decisions.
- Translate customer behavior signals into segment-aware campaign actions.

### Takeaway
The system is meant to improve targeting decisions, not just generate model scores.

## Slide 4
### Title
System Workflow

### Visual flow
```text
Customer data -> Behavioral segmentation -> Response scoring -> Targeting decision -> Campaign action
```

### Key points
- Use customer, behavioral, and trip-context signals as inputs.
- Convert raw data into reusable segments and response logic.
- Turn model outputs into campaign actions.

### Takeaway
The workflow is designed to connect analytics to execution.

## Slide 5
### Title
Behavioral Signal Review

### Key points
- The dataset includes 12,684 driving scenarios and 25 decision signals.
- Coupon type drives large differences in baseline acceptance.
- Behavioral frequency and trip context explain why the same coupon performs differently across customers.

### Visuals to keep
- Dataset overview
- Acceptance rate by coupon type
- High-level behavioral signal chart

### Takeaway
Coupon response is shaped by both offer type and customer context.

## Slide 6
### Title
What Drives Coupon Acceptance

### Key points
- Behavioral history is a stronger decision signal than basic demographics alone.
- Timing, urgency, and environmental context influence response likelihood.
- Acceptance behavior reflects a combination of habits, context, and offer fit.

### Visuals to keep
- Behavioral frequency findings
- Time / weather / expiration insights

### Takeaway
Targeting quality improves when the system captures behavior and context together.

## Slide 7
### Title
Customer Segmentation System

### Key points
- Five customer personas emerged from behavioral and demographic signals.
- Segmentation turns raw data into reusable targeting logic.
- Personas make coupon strategy more actionable than broad campaign delivery.

### Visuals to keep
- Five-persona summary
- Cluster profile or cluster visualization

### Takeaway
Segmentation adds business structure to the decision workflow.

## Slide 8
### Title
Decision Engine Summary

### Key points
- Three models were tested to evaluate whether segmentation improved response prediction.
- Adding persona features improved AUC across all models.
- XGBoost with clustering delivered the strongest performance.

### Visuals to keep
- Baseline vs. enhanced model comparison table
- Best-model summary metric

### What to compress
- Detailed tuning explanations
- Multiple model intro slides
- Excessive algorithm comparisons

### Takeaway
Segmentation improved the decision engine consistently, which supports using personas in targeting logic.

## Slide 9
### Title
Targeting Recommendations

### Key points
- Match coupon type to customer persona.
- Prioritize convenience offers for family-oriented segments.
- Reserve bar offers for high-response social segments.
- Use timing and expiration as part of the targeting decision.

### Visuals to keep
- Persona x coupon targeting matrix
- Best send time summary
- Targeted vs. blanket comparison

### Takeaway
The system creates a practical targeting playbook, not just a score.

## Slide 10
### Title
Business Impact

### Key points
- Improves targeting efficiency versus blanket coupon delivery.
- Reduces promotional waste.
- Supports smarter budget allocation and prioritization.
- Creates a reusable coupon decision workflow for campaign strategy.

### Optional close
Next step: convert the targeting logic into a lightweight rules engine or decision dashboard.

### Takeaway
The value of the project is operational: better allocation, better timing, and more effective promotional execution.

## Appendix Guidance
Move these items out of the 10-slide core deck and keep them only as backup:
- Detailed model descriptions
- Full ROC and confusion matrix comparisons
- Hyperparameter tuning details
- Extended SHAP explanation
- Full coefficient tables

## Presentation Style Notes
- Remove `Group 9`, course labels, and semester references from the main deck.
- Use business-facing language such as `decision system`, `targeting workflow`, and `operational impact`.
- Keep each slide focused on one business message.
- Let visuals support decisions, not dominate the story.
