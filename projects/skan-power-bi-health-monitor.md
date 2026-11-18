---
type: project
name: Power BI Health Monitor – Capacity and Reporting Governance
timeframe: 2024–2025 (confirm exact dates)
organization: Skan AI
project_type: internal platform monitoring and governance
domains:
  - BI Operations
  - Platform Observability
  - Report Governance
  - Capacity Management
tools:
  - Power BI
  - Power BI Admin and Capacity Metrics
  - Databricks Job Metadata
  - SQL
role: solution designer / BI platform owner
visibility_level: BI team, Data Platform and operations leadership
status: designed and implemented (confirm current adoption)
---

## Quick Answer

I designed a Power BI Health Monitor to provide centralized visibility into workspace and report health. The dashboard covered capacity utilization, slow and inactive reports, refresh performance, alignment between Databricks job completion and Power BI refreshes, and report failures with ownership visibility. It extended BI platform administration beyond reactive troubleshooting by giving the team a way to identify workload degradation, cleanup opportunities and refresh-strategy non-compliance.

## What Business Problem Did the Project Solve?

As the number of workspaces, reports and datasets grew, platform issues became harder to identify through individual report checks. Capacity pressure, slow refreshes, failed jobs and inactive content could remain unnoticed until users reported a problem.

The organization needed a consolidated monitoring view connecting Power BI operations with upstream data pipeline execution.

## What Was the Objective?

1. Monitor Power BI capacity utilization across workspaces and reports.
2. Identify reports with poor refresh performance or low activity.
3. Track refresh duration and failures.
4. Compare Databricks job completion with BI refresh execution.
5. Identify report owners and support proactive remediation.
6. Improve governance of the report lifecycle.

## What Did I Own?

- Defined monitoring objectives and dashboard requirements.
- Identified the operational metrics needed for capacity, refresh and report governance.
- Connected Power BI monitoring needs with Databricks job-completion information.
- Organized the dashboard around actionable operational questions rather than raw metric collection.
- Established the use cases for report cleanup, refresh optimization and failure follow-up.

## What Did the Dashboard Cover?

### 1. Capacity and workload monitoring

- Capacity utilization across workspaces and reports.
- Visibility into periods of elevated resource consumption.
- Signals of potential performance degradation.

### 2. Inactive and slow reports

- Reports with low or no recent activity.
- Reports with long refresh durations.
- Candidates for cleanup, consolidation or optimization.

### 3. Refresh and data pipeline alignment

- Power BI refresh duration and completion status.
- Databricks job completion time.
- Whether reports were refreshed after the required upstream data became available.
- Adherence to the centrally defined refresh window.

### 4. Failure monitoring and ownership

- Refresh failure rate and failure history.
- Visibility into the affected report or dataset.
- Ownership information to support follow-up and proactive remediation.

## Important Design Decisions

### Focus on actionable signals

The dashboard was intended to help answer what was degraded, which reports were affected and who should investigate. A large collection of disconnected charts would not have delivered the same operational value.

### Connect BI and data engineering monitoring

A report refresh cannot be interpreted correctly without knowing whether its source data pipeline completed. Linking those timelines made it easier to distinguish upstream delays from BI refresh problems.

### Include lifecycle governance

Inactive reports consume support attention and can create confusion. Usage visibility supports cleanup and better workspace hygiene, subject to report-owner review.

## What Was the Outcome?

- Created centralized visibility into Power BI platform health and reporting operations.
- Supported proactive identification of capacity and refresh degradation.
- Helped identify slow and inactive reports for review.
- Improved visibility into alignment between Databricks data readiness and BI refresh schedules.
- Established a dashboard-based mechanism for tracking failures and ownership.

No quantified reduction in failures or support tickets is included because a measured before-and-after result has not been supplied.

## What Artifacts Were Produced?

- Power BI Health Monitor dashboard.
- Capacity and report-health metrics.
- Refresh monitoring and pipeline-alignment views.
- Failure and ownership monitoring requirements.
- Operational review use cases for report lifecycle management.

## What Would I Measure Next?

- Number of active reports and datasets monitored.
- Percentage of reports within refresh SLA.
- Refresh failure rate and mean time to resolution.
- Number of inactive reports reviewed or retired.
- Capacity utilization before and after remediation.
- Percentage of refreshes aligned with upstream data completion.

## What Did I Learn?

- Effective observability connects technical metrics to operational ownership.
- BI monitoring should include data-pipeline dependencies, not only report refresh status.
- Report usage and freshness are important inputs to platform governance.
- Centralized visibility enables proactive action only when ownership and remediation workflows are clear.

## Frequently Asked Questions

### What did the monitor track?

Capacity utilization, slow and inactive reports, refresh duration, Databricks job completion alignment and refresh failures.

### Why include Databricks job timings?

To determine whether BI refreshes were aligned with upstream data availability and to distinguish source-pipeline delays from BI refresh issues.

### Was this a general business dashboard?

No. It was an operational governance and health-monitoring view for the Power BI platform.
