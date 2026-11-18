---
type: project
name: Enterprise Tableau to Power BI Migration and Dashboard Rationalization
timeframe: 2022-2024
organization: Citrix (now Cloud Software Group)
project_type: internal
domains: [BI Modernization, Platform Migration, Dashboard Rationalization, Customer Service, Technical Support, Digital Experience]
tools: [Tableau, Tableau Server, Power BI, Microsoft SQL Server, SQL, Salesforce, Workday, Genesys, Git]
role: lead
visibility_level: leadership
status: completed
---

## Problem Statement
Citrix had accumulated approximately 120 Tableau dashboards across customer service, technical support and digital experience. The dashboards had been created over time in response to requests from individual stakeholders, often without checking whether similar reporting already existed.

This created a fragmented reporting environment with overlapping dashboards, duplicated development effort and inconsistent metric definitions. Some dashboards remained actively used, while others had become redundant or inactive. Similar data appeared in multiple places with different calculations and business context, resulting in repeated questions about accuracy and which report should be treated as the source of truth.

The Tableau estate also introduced avoidable licensing and maintenance costs. Citrix already used the Microsoft ecosystem, creating an opportunity to reduce platform costs and improve integration by moving reporting to Power BI.

## Context & Constraints
- The migration covered three distinct business areas: customer service, technical support and digital experience, including web and chatbot analytics.
- The customer service organization alone had approximately 70-80 dashboards built for different stakeholders and use cases.
- Dashboards depended on data from Salesforce, Workday, Genesys, web telemetry and other operational systems.
- Existing reports contained overlapping but not always identical calculations and definitions.
- Business users still depended on active Tableau dashboards, so the transition needed to preserve critical reporting during migration.
- Requirements had to be consolidated and approved by business leaders rather than copied directly from the existing dashboards.
- Delivery required coordination among three analysts, data engineering teams and stakeholders across the business units.

## Objective
Migrate enterprise reporting from Tableau to Power BI while simplifying the dashboard estate and creating a more trusted and sustainable BI operating model.

Success meant:

- Reducing approximately 120 Tableau dashboards to a small set of comprehensive business-unit solutions.
- Preserving the useful decisions, KPIs and analytical outcomes of the existing reports without recreating their duplication.
- Standardizing metrics and improving confidence in reporting accuracy.
- Reducing Tableau licensing dependency and aligning BI with the Microsoft ecosystem.
- Providing scalable SQL Server and Power BI models that could support governed self-service analytics.
- Completing the transition without disrupting access to essential operational reporting.

## Your Role
I owned the migration and dashboard-rationalization initiative and led three analysts through discovery, requirements consolidation, design, development and validation.

My responsibilities included:

- Creating an inventory of approximately 120 Tableau dashboards.
- Classifying dashboards by business unit, audience, usage and analytical purpose.
- Identifying duplicated, inactive and overlapping reporting assets.
- Extracting the underlying business questions and KPI requirements from existing dashboards.
- Working with directors, VPs and business stakeholders to agree on consolidated requirements.
- Defining the target Power BI information architecture and dashboard structure.
- Designing reusable SQL Server and Power BI data models with data engineering teams.
- Assigning work, mentoring analysts and reviewing delivery quality.
- Coordinating validation, stakeholder sign-off and retirement of redundant Tableau content.

## Approach & Architecture
### 1. Discover and assess the Tableau estate

- Inventoried the dashboards deployed to Tableau Server across the three business units.
- Mapped each dashboard to its owner, audience, subject area, business questions and usage.
- Identified duplicate reports, conflicting definitions and dashboards with limited or no ongoing value.
- Separated the valuable analytical outcomes from the existing visual implementation.

### 2. Rationalize requirements by business unit

- Grouped related dashboard requirements under customer service, technical support and digital experience.
- Consolidated repeated requests into common business questions and decision-making workflows.
- Reviewed the proposed scope with senior leaders, including customer service directors and the VP.
- Agreed on standard KPIs, calculations, filters, dimensions and validation criteria before development.

### 3. Build the target data foundation

- Integrated Salesforce, Workday, Genesys, web telemetry and operational data into Microsoft SQL Server.
- Worked with data engineering to create reusable reporting datasets rather than dashboard-specific extracts.
- Defined schemas, relationships, calculations, partitions and indexes to support consistent and performant reporting.
- Centralized transformation and business logic to prevent each report from producing a different version of the same metric.

### 4. Deliver consolidated Power BI solutions

- Built compact Power BI semantic models on top of the governed SQL Server layer.
- Designed one comprehensive analytical solution for each business unit.
- Enabled users to move from multiple disconnected dashboards to a consistent reporting experience.
- Used documented definitions, stakeholder validation and Git-based change management to improve governance.

### Target data flow

`Salesforce + Workday + Genesys + Web/Chatbot Telemetry + Operational Sources -> Microsoft SQL Server -> Governed Analytical Models -> Power BI Business-Unit Solutions`

## Key Decisions & Trade-offs
- **Rationalize before migrating:** A one-to-one dashboard conversion would have reproduced the existing sprawl in Power BI. The team first consolidated requirements and removed duplication.
- **Organize around business units and decisions:** Dashboards were grouped according to shared audiences and business outcomes rather than individual requestors.
- **Adopt Power BI:** Power BI reduced Tableau licensing dependency and aligned with the organization's broader Microsoft ecosystem.
- **Centralize data logic in SQL Server:** Shared transformation and metric logic improved consistency, performance and maintainability compared with report-specific calculations and extracts.
- **Validate with senior stakeholders early:** Upfront agreement on outcomes and definitions required additional discovery time but reduced rework and data-quality disputes later.
- **Consolidate without overcrowding:** Combining reports risked producing large, difficult-to-use dashboards. Content was organized around decision workflows, with purposeful navigation and audience-specific views.

## Execution Highlights
- Reviewed and classified approximately 120 Tableau dashboards across three business units.
- Rationalized approximately 70-80 customer service dashboards into one consolidated customer service solution.
- Led and mentored three analysts throughout the migration.
- Partnered with directors, VPs, program managers and business users to finalize scope and KPI definitions.
- Coordinated with data engineering to build reusable SQL Server datasets and resolve source-data inconsistencies.
- Consolidated reporting across Salesforce, Workday, Genesys and digital telemetry.
- Introduced documented metric definitions, data validation and Git-based change control.
- Managed the transition from existing Tableau reports to the target Power BI solutions while maintaining access to essential reporting.

## Outcome & Impact
- Consolidated approximately 120 Tableau dashboards into three comprehensive Power BI solutions: one each for customer service, technical support and digital experience.
- Replaced approximately 70-80 customer service dashboards with a single trusted analytical experience.
- Reduced Tableau licensing dependency and associated BI platform costs.
- Reduced duplicated development and long-term dashboard maintenance.
- Established consistent KPI definitions and a shared source of truth for each business unit.
- Eliminated recurring data-quality complaints for the consolidated solution after rollout.
- Enabled governed self-service analytics, contributing to a 95% reduction in ad hoc data requests.
- Created reusable SQL Server and Power BI models that could support future requirements without creating another isolated dashboard for each request.
- Improved stakeholder confidence by involving business leaders in definition, validation and sign-off.

## Artifacts
- Three consolidated Power BI business-unit solutions.
- Tableau dashboard inventory and rationalization matrix.
- Source-to-target dashboard mapping.
- SQL Server analytical datasets and transformation logic.
- Power BI semantic models.
- KPI definitions and calculation documentation.
- Data-validation and stakeholder sign-off records.
- Git-based change history and deployment artifacts.

## Learnings
- A BI migration is an opportunity to simplify the reporting estate, not merely replace one visualization tool with another.
- Migrating dashboards one for one transfers existing governance and usability problems to the new platform.
- Dashboard rationalization should focus on the decisions users need to make rather than the number of existing reports.
- Trusted self-service requires standardized metrics, reusable data models and continuous stakeholder validation.
- Senior leadership alignment helps resolve conflicting definitions and prevents individual preferences from recreating dashboard sprawl.
- Platform cost reduction is most sustainable when combined with governance, architecture and operating-model improvements.
- Dashboard usage, ownership and duplication should be monitored continuously after migration to prevent future sprawl.
