---
type: project
name: Case Volume Forecasting for 24/7 Critical Support Staffing
timeframe: 3 days
organization: Citrix
project_type: internal
domains:
  - Support Analytics
  - Workforce Planning
  - Demand Forecasting
tools:
  - SQL
  - Salesforce
  - Excel
  - Multiple Linear Regression
role: owner
visibility_level: leadership
status: completed
---

## Quick Answer

At Citrix, I built a case-volume forecasting model for the Critical Situation Support team using historical support demand, customer growth, offering mix, and churn data from Salesforce and SQL Server. Delivered in three days, the model informed staffing recommendations across three shifts covering 24 hours. It supported the team's growth from 3 to 11 members within five months and remained useful for workforce planning for the next two years.

## What Business Problem Did the Project Solve?

The Critical Situation Support team handled urgent technical requests for a high-priority customer segment. As the customer base expanded, leadership needed to understand how support demand would grow and how many engineers should be available across regions and hours of the day.

Without a demand forecast, the team risked understaffing critical shifts, increasing response times, and overloading available engineers.

## What Was the Objective?

The project had two connected objectives:

1. Forecast monthly case volume as the eligible customer base changed.
2. Translate expected demand into staffing recommendations for three shifts providing continuous, 24-hour support.

The analysis also considered operational measures such as Time to Response (TTR), Average Handling Time (AHT), First Contact Resolution (FCR), escalations, Net Promoter Score (NPS), and Customer Satisfaction (CSAT).

## What Did I Own?

I owned the project end to end:

- Gathered case-volume data from Salesforce and SQL Server.
- Combined active-account growth, offering type, and customer churn data.
- Built and validated the monthly forecasting model.
- Analyzed historical demand by geography and hour.
- Converted forecast demand into headcount recommendations for three shifts.
- Presented the findings and staffing recommendations to team leadership.

## What Data Was Used?

The model and staffing analysis used:

- Historical monthly case volume.
- Case distribution by geography and hour.
- Active customer and account counts.
- Net-new and churned customers.
- Customer offering and service type.
- TTR, AHT, FCR, escalation, NPS, and CSAT measures.

## How Did the Forecasting Model Work?

I aggregated historical case volume and connected it with changes in the eligible customer population. A multiple linear regression model was used to estimate the relationship between case demand, net customer growth, offering mix, and churn.

The workflow was:

1. Extract and reconcile support and customer data.
2. Aggregate monthly case volume and customer movements.
3. Segment historical demand by geography and hour.
4. Train the regression model using customer and offering variables.
5. Compare forecast volumes with subsequent actual volumes.
6. Use the forecast and historical demand distribution to recommend staffing by shift.

## Why Was This Approach Chosen?

The project had a three-day delivery window. An interpretable regression model provided a practical balance between speed, explainability, and business usability. Leadership could understand how customer growth and churn affected expected support demand without relying on a difficult-to-explain forecasting system.

The trade-off was that the model depended on historical relationships remaining reasonably stable. It therefore provided a planning baseline rather than a guarantee of future demand.

## How Was Forecast Performance Measured?

The retained project record reports approximately 87% forecast accuracy with a ±5% tolerance for monthly case-volume predictions. The model was compared with actual monthly demand as new data became available.

For future implementations, I would report a standard forecasting metric such as Mean Absolute Percentage Error (MAPE) or Weighted Absolute Percentage Error (WAPE), document the holdout period, and track forecast drift over time.

## What Was the Business Outcome?

- The team expanded from 3 to 11 members within five months.
- Staffing was distributed across three shifts covering 24 hours.
- Leadership gained visibility into demand patterns by geography and hour.
- The model continued to support workforce planning for approximately two years without requiring a redesign.
- Hiring and shift-allocation decisions were based on forecast demand rather than intuition alone.

The forecast informed the staffing decision; team growth was ultimately approved and executed by operational leadership.

## What Artifacts Were Produced?

- Monthly case-volume forecast.
- Geographic and hourly demand analysis.
- Three-shift headcount recommendation.
- Leadership presentation of forecast assumptions and staffing needs.

The underlying customer data and internal planning artifacts are confidential and are not published publicly.

## What Did I Learn?

- Customer growth alone was not enough to explain demand; offering mix and churn materially changed the forecast.
- Forecasts became more useful when translated into an operational decision such as shift-level staffing.
- An interpretable model can be more valuable than a complex model when leaders need to understand and act on its assumptions quickly.
- Future versions should use documented forecasting-error metrics, explicit validation periods, and scheduled drift monitoring.

## Frequently Asked Questions

### What was forecast?

Monthly incoming case volume for the Critical Situation Support team.

### Which systems supplied the data?

Salesforce and SQL Server supplied the support, customer, and account data used in the analysis.

### How was the forecast used?

The forecast was combined with historical demand by geography and hour to recommend headcount across three shifts.

### What was the reported forecast performance?

The retained project record reports approximately 87% accuracy with a ±5% tolerance. A future implementation should express this using a standard metric such as MAPE or WAPE.

### What changed after the project?

The team grew from 3 to 11 members within five months and established three-shift coverage for continuous critical support.
