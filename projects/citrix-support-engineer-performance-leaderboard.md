---
type: project
name: Support Engineer Performance Leaderboard Redesign
timeframe: 2022-2024
organization: Citrix (now Cloud Software Group)
project_type: internal
domains: [Customer Service, Technical Support, Performance Analytics, Employee Recognition, Incentive Programs]
tools: [Power BI, SQL, DAX]
role: owner
visibility_level: leadership
status: completed
---

## Problem Statement
The customer service and technical support organizations used performance leaderboards to recognize and reward representatives and technical staff. Separate peer groups were maintained by product line, service type and operating vertical. The top 10% of performers within each group could receive monetary rewards, gifts or other recognition.

The existing scoring model used z-scores across multiple performance metrics. Because a z-score represents performance relative to the group average, employees performing below the mean on any metric received a negative score for that component. A single below-average result could offset strong performance across several other metrics and materially reduce the employee's overall rank.

This created a scoring experience that felt punitive rather than motivational. Employees needed to perform well across every metric to avoid a negative impact, even when they made meaningful contributions in other areas. Since the leaderboard influenced recognition and rewards, the scoring methodology needed to be fair, transparent and aligned with the behaviors the business wanted to encourage.

## Context & Constraints
- Leaderboards covered multiple customer service and technical support verticals with different product lines and service responsibilities.
- Employees needed to be compared with relevant peers rather than ranked across fundamentally different roles.
- Multiple performance metrics contributed to the final ranking, and each metric did not necessarily have equal business importance.
- The top 10% within each peer group qualified for the incentive or recognition program.
- Any methodology change required support from directors and business leaders because it affected employee rankings and rewards.
- The new calculation had to remain understandable enough for employees and managers to trust the result.
- Historical dashboard functionality needed to be preserved while the scoring logic was redesigned.

## Objective
Redesign the leaderboard methodology to create a fairer and more motivating performance-recognition system that:

- Removed negative scoring for below-average results.
- Recognized positive contribution across every performance metric.
- Applied business-approved weights to reflect the relative importance of each metric.
- Preserved fair comparisons within the appropriate product and service peer groups.
- Clearly identified the top 10% of performers in each vertical.
- Gave employees an engaging, transparent way to track their performance.
- Earned leadership approval for use in the incentive program.

## Your Role
I identified the weakness in the existing z-score methodology and owned the scoring-model redesign from analysis through leadership approval and rollout.

My responsibilities included:

- Reviewing the existing leaderboard calculations and identifying how negative z-scores affected overall rankings.
- Evaluating an alternative normalization approach that preserved relative performance without negative marking.
- Converting each performance metric to a common bounded scale.
- Reviewing and updating metric weights according to business priorities.
- Recalculating composite scores and rankings within each peer group.
- Demonstrating the old and new approaches through data-backed examples.
- Presenting the proposed methodology to directors and business leaders.
- Updating the Power BI dashboard and supporting the rollout of the approved scoring model.

## Approach & Architecture
### 1. Assess the existing scoring model

- Reviewed how z-scores were calculated for each performance metric.
- Traced how a below-average result produced a negative component score.
- Compared representative employee profiles to show how one metric could offset strong contributions elsewhere.
- Identified the disconnect between the mathematical behavior of the model and the program's goal of positive recognition.

### 2. Normalize the performance metrics

- Replaced the z-score approach with bounded normalization.
- Converted metrics measured on different scales into comparable non-negative scores.
- Preserved relative differentiation between employees without subtracting from the contribution earned on other metrics.
- Applied appropriate score direction so that both higher-is-better and lower-is-better measures could contribute consistently.

### 3. Redesign metric weighting

- Reviewed the influence of each metric on the composite score.
- Updated weights to reflect business priorities and the expected contribution of each performance dimension.
- Calculated the final weighted score as the combined normalized contribution across metrics.
- Ranked employees within the relevant product line, service type or vertical.

### 4. Validate and secure leadership approval

- Built data-backed comparisons of employee rankings under the old and proposed methodologies.
- Explained the limitation of negative z-score contributions in business terms.
- Walked directors and business leaders through the revised calculation, weighting and ranking logic.
- Incorporated stakeholder feedback and received approval for immediate rollout.

### 5. Deliver the redesigned leaderboard

- Updated the Power BI calculation and dashboard experience with the approved model.
- Enabled employees to review their metric-level performance, composite score and peer-group position.
- Highlighted top performers while making the leaderboard useful for ongoing self-monitoring.

### Scoring flow

`Performance Metrics -> Metric-Level Normalization -> Business-Approved Weights -> Composite Score -> Peer-Group Ranking -> Top 10% Recognition`

## Key Decisions & Trade-offs
- **Replace z-scores with bounded normalization:** Z-scores are useful for statistical comparison but introduced negative contributions that conflicted with the program's recognition objective. Normalization retained relative performance while keeping contributions non-negative.
- **Rank within relevant peer groups:** Comparing employees within the same product or service vertical reduced bias caused by differences in role, workload and operating context.
- **Use weighted composite scoring:** Equal weighting would have been simpler but would not reflect the business importance of each performance measure.
- **Preserve performance differentiation:** Removing negative scores did not mean treating all results equally; stronger performance still produced a higher normalized contribution and rank.
- **Make the calculation explainable:** A technically sophisticated model would not succeed if employees and leaders could not understand how performance translated into rank.
- **Demonstrate the change with real scenarios:** Side-by-side examples made the model's effect easier for leadership to evaluate than a purely statistical explanation.

## Execution Highlights
- Reverse-engineered the existing z-score-based leaderboard calculation.
- Identified and demonstrated the unintended penalty created by negative component scores.
- Designed a non-negative normalized scoring framework across multiple performance metrics.
- Recalibrated metric weights to align the composite score with business priorities.
- Preserved segmentation and top-10% ranking across product and service verticals.
- Presented the redesigned model to directors and business leaders using data-backed comparisons.
- Secured leadership approval and implemented the new logic in Power BI.
- Rolled out metric-level and overall performance visibility for representatives and technical staff.

## Outcome & Impact
- Eliminated negative marking from the leaderboard's performance-scoring model.
- Created a fairer scoring approach that recognized contribution across all metrics while preserving competitive differentiation.
- Received immediate approval from directors and business leaders for organization-wide rollout.
- Grew the leaderboard into one of the company's most-used internal data products, with more than 100 daily active users.
- Enabled employees to monitor their performance and understand how each metric contributed to their rank.
- Increased engagement with the incentive program by making performance tracking more transparent, competitive and enjoyable.
- Provided a consistent basis for identifying the top 10% of performers within each vertical.
- Demonstrated how analytical-model design could directly influence employee experience and business policy.

## Artifacts
- Power BI performance leaderboard.
- Normalized metric-scoring framework.
- Weighted composite-score calculation.
- Peer-group and top-10% ranking logic.
- Old-versus-new methodology comparison.
- Leadership presentation and approval materials.
- Metric-definition and calculation documentation.

## Learnings
- A statistically valid method may still be unsuitable when its behavior conflicts with the business purpose of the product.
- Incentive-related analytics requires careful consideration of fairness, transparency and unintended behavioral effects.
- Normalization and weighting choices should be evaluated through representative employee scenarios, not only aggregate statistics.
- Explainability is essential when analytical models influence rewards, recognition or employee behavior.
- Data-backed comparisons can help leaders understand and approve a methodological change quickly.
- Successful internal data products combine sound analytical design with an engaging and understandable user experience.
