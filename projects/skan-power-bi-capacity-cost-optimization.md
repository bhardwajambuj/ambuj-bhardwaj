---
type: project
name: Power BI Capacity and Databricks Cost Optimization
timeframe: 2024–2025 (confirm exact dates)
organization: Skan AI
project_type: platform optimization and operations
domains:
  - BI Platform Administration
  - Cloud Cost Optimization
  - Workload Scheduling
  - Capacity Management
  - Data Platform Operations
tools:
  - Power BI Premium P2
  - Power BI Service
  - Databricks SQL Warehouse
  - Databricks Jobs
  - SQL
  - Power BI Monitoring
role: platform owner / optimization lead
visibility_level: cross-functional and leadership
status: delivered improvements; ongoing ownership
---

## Quick Answer

I took ownership of Power BI platform utilization and worked with the Databricks Architect to identify why BI refresh activity was consuming capacity and compute resources for most of the day. Analysis showed scattered, long-running refreshes that kept Power BI capacity and Databricks SQL Warehouses busy for almost 22 hours per day. I redesigned the refresh strategy around upstream data-pipeline completion and business usage, consolidating refresh execution into a five-hour window. Reported outcomes included Power BI capacity utilization falling from approximately 85% to 45% and Databricks DBU consumption reducing by approximately 58%.

## What Business Problem Did the Project Solve?

The reporting platform ran on Power BI Premium P2 with autoscaling considerations and used Databricks SQL Warehouses as an analytical source. Refreshes were distributed throughout the day, often ran for extended periods and overlapped with other workloads.

This created sustained resource consumption, limited available capacity during peak usage and increased variable infrastructure costs. The organization needed to understand the full chain from data pipeline execution to dataset refresh and customer dashboard availability.

## What Was the Objective?

1. Identify the drivers of sustained Power BI capacity utilization.
2. Correlate BI refreshes with Databricks SQL Warehouse activity.
3. Reduce unnecessary refresh frequency and overlapping workloads.
4. Align dashboard refreshes with data availability and customer usage patterns.
5. Improve resource availability during business hours without compromising required freshness.
6. Establish a repeatable operating strategy and monitoring approach.

## What Did I Own?

- Power BI Premium capacity administration and utilization analysis.
- Investigation of refresh schedules, refresh duration and workload overlap.
- Identification of long-running and scattered refresh operations.
- Design of a centralized refresh strategy.
- Cross-functional analysis with the Databricks Architect to connect BI usage with compute consumption.
- Monitoring of refresh adherence and platform health.

## How Did the Optimization Work?

1. Analyzed capacity utilization and refresh history across the reporting environment.
2. Identified refresh activity distributed across nearly 22 hours of the day.
3. Correlated refresh jobs with Databricks SQL Warehouse usage and upstream data jobs.
4. Defined refresh dependencies so dashboards were refreshed after the required data pipelines completed.
5. Consolidated refreshes into a controlled five-hour window.
6. Monitored capacity and DBU consumption after the change to assess the effect.

## What Decisions and Trade-offs Were Important?

### Refresh based on data readiness, not arbitrary schedules

Refreshing before upstream pipelines completed could waste compute and make dashboards stale again as soon as new data arrived. The refresh plan therefore needed to follow data availability.

### Consolidate workloads without creating a new peak

A narrow refresh window improves predictability but can create a concentrated resource spike. Scheduling and capacity had to be considered together so that consolidation did not simply move the bottleneck.

### Balance freshness and cost

Not every dashboard requires the same refresh cadence. The refresh strategy should reflect business criticality, user activity and source-data update frequency.

## What Was the Outcome?

- Power BI capacity utilization reduced from approximately 85% to 45%.
- Databricks DBU consumption reduced by approximately 58%.
- Refresh activity consolidated from almost 22 hours per day into an approximately five-hour window.
- Improved availability of capacity and compute resources outside the refresh window.
- Better alignment between data engineering completion and BI data freshness.

These are reported project outcomes. Before publishing externally, confirm the measurement period, capacity utilization definition, DBU baseline and whether the percentage reductions represent average, peak or total consumption.

## What Artifacts Were Produced?

- Refresh scheduling and orchestration strategy.
- Capacity and refresh analysis.
- Cross-platform workload investigation with the Databricks team.
- Monitoring requirements for refresh duration, failure rate and schedule adherence.
- Operating guidance for aligning BI refreshes with data pipeline completion.

## What Would I Measure in a Future Version?

- Monthly capacity utilization and autoscaling consumption.
- Total Databricks DBUs attributable to BI refresh workloads.
- Refresh duration distribution and failure rate.
- Data freshness SLA by dashboard or dataset.
- Compute cost per refresh and per active report.
- Capacity headroom during peak concurrent usage.

## What Did I Learn?

- BI platform costs cannot be optimized in isolation from upstream data processing.
- Refresh scheduling is an architecture and operating-model decision, not merely an administrative setting.
- Data readiness, business usage and compute capacity must be planned together.
- A centralized monitoring approach is necessary to keep the savings from eroding as reports and workloads grow.

## Frequently Asked Questions

### What caused the prolonged utilization?

Long-running and scattered refreshes kept Power BI capacity and Databricks SQL Warehouses active for almost 22 hours per day.

### What changed?

Refreshes were aligned with pipeline completion and consolidated into an approximately five-hour window.

### What were the reported improvements?

Power BI capacity utilization moved from approximately 85% to 45%, while Databricks DBU consumption reduced by approximately 58%.

### Did the project remove the need for capacity management?

No. It improved workload scheduling and utilization. Capacity monitoring and optimization remain ongoing platform responsibilities.
