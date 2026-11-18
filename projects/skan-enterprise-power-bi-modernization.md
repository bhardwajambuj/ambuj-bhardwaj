---
type: project
name: Enterprise Power BI Modernization for a Large Customer
timeframe: 2024–2025 (confirm exact delivery dates)
organization: Skan AI
project_type: customer-facing analytics modernization
domains:
  - Enterprise BI Architecture
  - Process Mining Analytics
  - Data Integration
  - Data Modeling
  - BI Performance Optimization
tools:
  - Power BI Desktop and Service
  - DAX
  - Power Query (M)
  - Databricks
  - Azure Blob Storage
  - SQL
role: architecture and technical delivery owner
visibility_level: customer and cross-functional leadership
status: completed / delivered improvements
---

## Quick Answer

At Skan AI, I took ownership of modernizing a complex Power BI solution for a large enterprise customer. The reporting environment combined approximately three years of Skan clickstream data with the customer's CRM and workforce datasets. With limited documentation or handover, I reverse-engineered a model containing around 70 tables, 350 measures and 150 calculated columns, then redesigned its data preparation and reporting approach. The work included a Databricks and Azure Blob Storage ingestion pipeline, analytical data preparation and a transition towards DirectQuery. The resulting improvements included report refreshes that were up to 80% faster and a substantial reduction in the data required by the reporting model.

## What Business Problem Did the Project Solve?

The customer had accumulated several years of granular process-mining and digital-interaction data. To produce operational insights, the customer combined Skan data with its own CRM and workforce information. Over time, the reporting solution grew in complexity and became difficult to maintain and slow to refresh or interact with.

The Power BI report contained more than 30 worksheets, approximately 70 tables, around 350 measures and approximately 150 calculated columns. There was insufficient technical documentation and no complete handover describing the model, dependencies or business logic.

The challenge was not simply to make individual visuals faster. The underlying data preparation, model structure and refresh strategy needed to be redesigned while preserving the customer-facing analytical requirements.

## What Was the Objective?

1. Understand the existing report and its business logic without relying on complete documentation.
2. Establish a repeatable ingestion and transformation process for Skan and customer-supplied data.
3. Simplify and optimize the reporting model.
4. Improve report refresh and interactive performance.
5. Improve data availability while reducing unnecessary data movement and processing.
6. Leave behind a more supportable and documented solution.

## What Did I Own?

- Reverse-engineered the Power BI report, data model, DAX measures, calculated columns and relationships.
- Identified the upstream data requirements and dependencies needed to reproduce the existing reporting logic.
- Designed the ingestion approach for external customer data using Databricks and Azure Blob Storage.
- Worked through data cleansing, standardization, joining and warehouse preparation requirements.
- Reworked the analytical model and reporting access pattern.
- Evaluated and implemented the transition towards DirectQuery for the relevant reporting workloads.
- Coordinated the technical work needed to retain required dashboard functionality while improving the underlying architecture.

## How Did the Solution Work?

1. **Reverse engineering:** Inspected report structure, tables, measures, calculated columns, relationships and visual dependencies.
2. **Source integration:** Established ingestion for customer CRM and workforce data alongside Skan process-mining data.
3. **Data preparation:** Used Databricks jobs to sanitize, align and combine the required source data.
4. **Analytical modeling:** Prepared reporting-oriented data structures instead of making the report repeatedly process raw source data.
5. **Power BI redesign:** Updated the model and reporting access pattern, including a transition towards DirectQuery where appropriate.
6. **Validation:** Checked the redesigned outputs against the reporting requirements and existing business logic.

## Important Architecture Decisions and Trade-offs

### Move data preparation upstream

Complex integration and repeatable transformations belonged in the data platform rather than being duplicated inside report logic. This improved separation of responsibilities between data engineering and BI.

### Use a reporting-oriented data model

The model needed to support analytical questions without forcing every report interaction to traverse unnecessarily granular event data.

### Adopt DirectQuery selectively

DirectQuery improved data availability and avoided some of the overhead associated with large imported datasets. The trade-off is that interactive performance becomes more dependent on source query performance, concurrency and database capacity. The design therefore needed appropriate query optimization and warehouse support rather than treating DirectQuery as an automatic performance fix.

### Preserve business behavior while changing implementation

The objective was to improve the architecture without silently changing KPI definitions or customer-facing results. Validation of measures and report outputs was therefore a core part of the work.

## What Was the Outcome?

- Improved report refresh performance by up to approximately 80%.
- Reduced the size of selected reporting datasets by approximately 98% through data preparation and summarization.
- Established a repeatable ingestion and transformation approach for external customer data.
- Improved the maintainability of a complex Power BI solution with limited original documentation.
- Created a more scalable foundation for the customer's combined process-mining, CRM and workforce reporting needs.

The 98% figure should be described as the reduction in the relevant reporting dataset or model footprint, not as a universal reduction across all customer data, unless the precise measurement confirms that broader scope.

## What Artifacts Were Produced?

- Reverse-engineered Power BI model documentation.
- Databricks ingestion and transformation jobs.
- Customer-data integration workflow using Azure Blob Storage.
- Reporting-oriented data structures.
- Updated Power BI semantic model and report implementation.
- Validation checks for key reporting requirements.

Customer names, source data and report contents are confidential and are not included in this portfolio.

## What Would I Measure in a Future Version?

- Before-and-after refresh duration by dataset and report.
- P50/P95 visual query latency under representative concurrency.
- Model size and rows scanned by major query patterns.
- Data freshness from upstream pipeline completion to report availability.
- Number of measures, calculated columns and transformations simplified or retired.
- Defect or reconciliation rate following the model redesign.

## What Did I Learn?

- Reverse engineering is a critical architecture skill when inheriting undocumented enterprise BI solutions.
- Report performance is often a data architecture problem, not just a visualization problem.
- DirectQuery requires deliberate source-side modeling and workload planning.
- External customer data integration needs repeatable ingestion, sanitization and reconciliation controls.
- A successful modernization preserves business meaning while changing the technical implementation.

## Frequently Asked Questions

### How large was the original Power BI solution?

It contained more than 30 worksheets, approximately 70 tables, around 350 measures and approximately 150 calculated columns.

### What data was combined?

Skan clickstream/process-mining data was combined with customer CRM and workforce datasets.

### What was the reported performance improvement?

Report refreshes improved by up to approximately 80%. The exact before-and-after timings should be added if available.

### Why was DirectQuery introduced?

It was part of the effort to improve data availability and reduce dependence on large imported datasets. Its performance depended on the quality and capacity of the underlying analytical layer.
