# Coupon Targeting Presentation Rewrite

This draft keeps the substance of the original analysis while reframing the deck as a business system project instead of a course-style modeling presentation.

## Slide 1
### Title
Coupon Targeting Decision System

### Subtitle
A customer segmentation and decision-support workflow for smarter promotional targeting

### Suggested content
- Consumer Intelligence Systems
- Alice Dong
- GTM / operational intelligence portfolio project

## Slide 2
### Title
The Business Problem

### Suggested content
- Blanket coupon delivery wastes budget and reduces targeting efficiency.
- Customer response varies by coupon type, timing, behavior, and trip context.
- A one-size-fits-all promotion strategy misses high-response segments and over-targets low-response ones.

### Speaker angle
Frame this as an execution problem, not just a prediction problem.

### PPT-ready short version
- Blanket coupon delivery wastes budget.
- Response varies by customer behavior, timing, and context.
- Better targeting requires a decision system, not a one-size-fits-all campaign.

## Slide 3
### Title
Decision Objective

### Suggested content
- Identify which customer contexts are most responsive to specific coupon types.
- Build a reusable targeting workflow that supports smarter coupon delivery decisions.
- Translate customer behavior signals into segment-aware campaign actions.

## Slide 4
### Title
System Workflow

### Suggested content
```text
Customer data -> Behavioral segmentation -> Response scoring -> Targeting decision -> Campaign action
```

- Customer data includes demographics, visit behavior, coupon type, and trip context.
- Segmentation creates reusable customer personas.
- The decision engine combines context and segment information to support targeting recommendations.

### PPT-ready short version
```text
Customer data -> Behavioral segmentation -> Response scoring -> Targeting decision -> Campaign action
```
- Segment customers by behavior and context
- Score likely coupon response
- Deliver the right offer to the right segment

## Slide 5
### Title
Behavioral Signal Review

### Suggested content
- The dataset contains 12,684 real driving scenarios and 25 decision signals.
- Overall acceptance rate is 56.8%, but acceptance varies sharply by coupon type.
- Coupon type is important, but behavior and context explain why the same coupon performs differently across customers.

### Keep from original
- Coupon type acceptance comparison
- High-level dataset summary

## Slide 6
### Title
What Drives Coupon Acceptance

### Suggested content
- Behavioral frequency is a stronger decision signal than basic demographics.
- Time, weather, destination context, and expiration urgency materially influence acceptance behavior.
- Customer response is shaped by both who the driver is and the context in which the offer appears.

### Keep from original
- Behavioral frequency findings
- Time / weather / expiration insights

## Slide 7
### Title
Customer Segmentation System

### Suggested content
- Five behavioral personas were identified using demographic and visit-frequency signals.
- Segmentation adds structure beyond raw feature analysis by grouping similar response patterns.
- Personas make the targeting workflow more actionable for business teams than individual-level probability alone.

### Keep from original
- The five personas
- Cluster visualization or cluster summary

### PPT-ready short version
- Five customer personas emerged from behavioral and demographic signals.
- Segmentation turns raw data into reusable targeting logic.
- Personas make coupon strategy more actionable than broad campaign delivery.

## Slide 8
### Title
Segment Profiles and Targeting Logic

### Suggested content
- Young Bar Hoppers: strongest response to bar-related offers
- Family Takeout / Conservative Families: stronger response to convenience-driven meal offers
- Social Food Lovers: more responsive to selected dining and coffee scenarios

### Suggested closing line
The same coupon can perform very differently depending on persona, which makes targeting logic more valuable than blanket delivery.

## Slide 9
### Title
Decision Engine Summary

### Suggested content
- Three models were tested to evaluate whether segmentation improved coupon response prediction.
- Adding persona features improved AUC across all models.
- XGBoost with clustering delivered the strongest performance and the clearest ranking signal.

### Keep from original
- Baseline vs. enhanced model comparison table
- XGBoost best-performance summary

### Remove or compress
- Detailed model-by-model educational explanations
- Excessive tuning detail

## Slide 10
### Title
What the Decision Engine Learned

### Suggested content
- Coupon type remains the strongest direct signal.
- Segment-aware features help the model distinguish where targeting should become more selective.
- Timing and contextual features influence whether interest converts into action.

### Keep from original
- Cross-model importance summary
- SHAP summary, but simplify the explanation

## Slide 11
### Title
Targeting Recommendations

### Suggested content
- Match coupon type to customer persona rather than broad distribution.
- Prioritize meal and carryout offers for convenience-oriented family segments.
- Use bar offers selectively for high-response social segments instead of distributing them broadly.
- Schedule offers around coupon-specific peak acceptance windows.

### PPT-ready short version
- Match coupon type to customer persona
- Prioritize convenience offers for family-oriented segments
- Reserve bar offers for high-response social segments
- Use timing as part of the targeting decision

## Slide 12
### Title
Timing and Delivery Strategy

### Suggested content
- Coupon effectiveness depends on both coupon type and send time.
- Short expiration does not necessarily create urgency; in several cases it suppresses acceptance.
- Timing should be treated as a decision variable in the targeting workflow, not as a static campaign setting.

### Keep from original
- Best send time by coupon type
- 1-day vs 2-hour expiration insight

## Slide 13
### Title
Targeted vs. Blanket Delivery

### Suggested content
- Blanket campaigns over-send to low-response groups and under-focus on high-response personas.
- Persona-targeted delivery improves expected response rate and reduces promotional waste.
- The value of the system is not just better prediction, but better allocation.

### Keep from original
- Targeted vs blanket comparison
- Waste reduction / ROI framing

## Slide 14
### Title
Execution Workflow

### Suggested content
1. Identify persona from behavioral profile
2. Match persona to best-fit coupon type
3. Select timing and expiration window
4. Prioritize by expected response and ROI
5. Dispatch only when threshold conditions are met

### Speaker angle
This slide should make the project feel deployable and operational.

## Slide 15
### Title
Business Impact

### Suggested content
- Improves targeting efficiency versus blanket coupon delivery
- Translates behavioral signals into repeatable campaign actions
- Supports smarter budget allocation and segment prioritization
- Creates a reusable decision-support workflow for promotion strategy

### PPT-ready short version
- Improves targeting efficiency
- Reduces promotional waste
- Supports smarter budget allocation
- Creates a reusable coupon decision workflow

## Slide 16
### Title
Next Steps

### Suggested content
- Convert the targeting logic into a lightweight business dashboard or rules engine
- Add live scoring for new campaign scenarios
- Compare segment-driven targeting with supervised-only strategies
- Connect the workflow to a repeatable campaign execution process

## Slide Cleanup Notes
- Remove `Group 9`, course references, and semester labels from the title and closing slides.
- Reduce the total number of appendix-style model detail slides in the main deck.
- Move highly technical backup material, such as full coefficient tables, to appendix only.
- Keep the visual story business-first: fewer model explanations, more targeting logic and action design.
