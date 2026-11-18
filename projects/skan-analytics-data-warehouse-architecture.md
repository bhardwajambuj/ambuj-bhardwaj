---
type: project
name: Enterprise Analytics Data Warehouse Architecture
timeframe: 2024–present
organization: Skan AI
project_type: data platform architecture and engineering
domains:
  - Data Warehouse Architecture
  - Process Mining
  - Clickstream Analytics
  - Analytical Data Modeling
  - Incremental Data Processing
tools:
  - Databricks
  - Delta Lake
  - Apache Spark
  - PySpark
  - StarRocks
  - SQL
  - Materialized Views
role: data warehouse architect / technical lead
visibility_level: multi-team and product leadership
status: implemented foundation; continuously evolving
---

## Quick Answer

I designed and led the implementation of an analytical data warehouse spanning Databricks and StarRocks to move reporting away from direct dependence on granular transactional and clickstream data. The work established reporting-oriented schemas, dataset granularity, aggregation strategies, SQL transformations, materialized views and refresh frequencies for process-mining analytics. Selected reporting tables were reduced by approximately 98% in size and around 70% in record count, while Power BI report refreshes improved by up to 80%. The warehouse also provides reusable data foundations for customer-facing BI and AI-powered analytical capabilities.

## What Business Problem Did the Project Solve?

Skan's process-mining platform captures granular user interactions across enterprise applications, including clicks, key presses and scrolling. These events are enriched and processed to derive process behavior, case outcomes, participant activity and operational insights.

Using raw or near-transactional datasets directly for every analytical query created several challenges:

- Large volumes of granular events had to be scanned for common reporting questions.
- Different reports could implement similar business logic independently.
- Query cost and refresh duration grew with data volume.
- Late-arriving events and historical updates complicated incremental reporting.
- Data models needed to serve both conventional dashboards and newer AI-assisted analytics use cases.

## What Was the Objective?

1. Establish a reusable analytical warehouse for process-mining datasets.
2. Define schemas and data granularity based on business use cases.
3. Separate data processing from customer-facing analytical serving.
4. Reduce the size and query cost of reporting datasets.
5. Support incremental processing, including late-arriving data.
6. Provide reliable datasets for Power BI, Superset and AI-powered analytics.

## What Did I Own?

- Warehouse architecture and analytical modeling approach.
- Definition of schemas, table grain and aggregation strategies.
- SQL transformations and materialized-view design.
- Refresh frequency and data dependency decisions.
- Optimization of reporting datasets across Databricks and StarRocks.
- Documentation of SQL logic, metadata, business definitions and dataset use cases.
- Alignment of warehouse outputs with BI and semantic-layer requirements.

## What Data Domains Did the Warehouse Support?

The analytical subject areas discussed and modeled include:

- Event summaries.
- Case summaries.
- Participant switch and activity analysis.
- Variant analysis.
- Subprocess bottlenecks.
- Task bottlenecks.
- Participant daily engagement, including UTC-oriented reporting requirements.

These datasets support different grains of analysis, from event-level behavior to case, participant and process-level summaries.

## How Did the Architecture Work?

1. **Capture and process:** Granular clickstream events are ingested and processed through the data platform.
2. **Enrich and standardize:** Data processing aligns event attributes and derives analytical fields required by downstream use cases.
3. **Model by analytical grain:** Data is organized into subject-oriented datasets such as event, case, participant and bottleneck summaries.
4. **Aggregate for reporting:** Common analytical questions are served through summarized tables and materialized views rather than repeatedly scanning raw event data.
5. **Serve workloads:** Databricks and StarRocks support processing and analytical serving patterns according to workload requirements.
6. **Refresh incrementally:** Refresh strategies account for normal new data as well as late-arriving records and historical corrections.
7. **Document semantics:** Dataset grain, SQL, metric definitions and use cases are documented for BI developers and semantic-layer/AI consumers.

## Important Architecture Decisions and Trade-offs

### Model around business grain

A table must have a clearly understood grain. Event, case, participant and process-level metrics cannot be safely mixed without explicit aggregation rules. Defining grain reduces double counting and inconsistent KPI calculations.

### Pre-aggregate frequently used analytical patterns

Summaries and materialized views reduce repeated scans of large event datasets. The trade-off is additional storage and refresh complexity, which must be balanced against query frequency and freshness requirements.

### Separate processing and serving concerns

Databricks supports large-scale data processing and transformation, while StarRocks supports analytical serving patterns. Workload placement should be based on query shape, concurrency, latency and operational cost rather than forcing every workload onto one engine.

### Handle late-arriving data explicitly

A simple watermark can miss historical changes if records arrive after the normal processing window. The design therefore needs a controlled lookback or correction strategy so incremental processing can update affected reporting periods.

### Treat semantic documentation as part of the data product

SQL definitions without grain, business meaning and caveats are difficult to reuse safely. Documentation helps reporting teams and AI-assisted tools interpret the warehouse consistently.

## What Was the Outcome?

- Reduced the size of selected reporting tables by approximately 98%.
- Reduced record counts in selected summarized reporting datasets by approximately 70%.
- Improved Power BI report refresh performance by up to approximately 80% in the relevant reporting workstream.
- Established reusable analytical data models for process-mining reporting.
- Enabled incremental reporting patterns that account for late-arriving data.
- Created a data foundation used by BI reporting and AI-assisted analytics initiatives.

The 98%, 70% and 80% figures refer to reported outcomes from selected workloads; they should not be generalized to every warehouse table or every report.

## What Artifacts Were Produced?

- Analytical warehouse schemas and table definitions.
- SQL transformations and aggregation logic.
- Materialized views and refresh strategies.
- Dataset-grain and business-use-case documentation.
- Data dependency and refresh requirements.
- Reusable analytical datasets for BI and AI use cases.

## What Would I Improve or Measure Next?

- Document table-level freshness and completeness SLAs.
- Track query latency, scanned bytes/rows and compute cost by dataset.
- Add automated reconciliation checks between raw and summarized datasets.
- Formalize late-arriving-data correction windows and backfill procedures.
- Track semantic-definition coverage and reuse across dashboards and AI queries.
- Add lineage and ownership metadata to each curated dataset.

## What Did I Learn?

- Data grain is one of the most important design decisions in analytical systems.
- Summarization can deliver major performance gains, but it must preserve the required business meaning.
- Incremental processing needs an explicit strategy for late-arriving and corrected data.
- The warehouse should serve both current BI workloads and emerging AI use cases.
- Documentation of semantics and SQL is part of platform architecture, not an optional handover activity.

## Frequently Asked Questions

### Which platforms were involved?

Databricks and Delta Lake were used for data processing and storage patterns, with StarRocks supporting analytical serving workloads.

### What types of datasets were modeled?

Event, case, participant, variant, task-bottleneck, subprocess-bottleneck and engagement datasets were among the analytical subject areas.

### How did the warehouse improve reporting?

It moved recurring reporting workloads away from raw transactional data and introduced summarized, reporting-oriented tables and materialized views.

### How was late-arriving data handled?

Incremental processing was designed to account for records that arrive after the normal processing window, allowing affected reporting data to be corrected.
