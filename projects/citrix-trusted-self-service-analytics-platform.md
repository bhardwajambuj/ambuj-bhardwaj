---
type: project
name: Trusted Self-Service Analytics Platform
timeframe: 2022-2024
organization: Citrix (now Cloud Software Group)
project_type: internal
domains: [Customer Service, Technical Support, Digital Experience, Self-Service Analytics, BI Modernization]
tools: [Power BI, Tableau, Microsoft SQL Server, SQL, Salesforce, Workday, Genesys, Git]
role: lead
visibility_level: leadership
status: completed
---

## Problem Statement
Citrix had a centralized data and analytics team responsible for building dashboards and analytical solutions for stakeholders across the company. Over time, dashboard requests became fragmented across teams and individuals. Similar requests were submitted independently by stakeholders from the same business unit, and the analytics team often responded by creating separate dashboards for each request.

This resulted in a large and difficult-to-govern Tableau estate. The same metrics and datasets appeared in multiple dashboards with different business context, calculations and presentation. Some dashboards remained actively used while others became redundant or inactive. The duplication increased development and maintenance effort and created recurring discussions about data accuracy, metric definitions and which dashboard should be treated as the trusted source.

The customer service organization alone had approximately 70-80 dashboards created over time. Across customer service, technical support and digital experience, the broader rationalization exercise identified approximately 120 Tableau dashboards.

## Context & Constraints
- The existing Tableau environment had grown incrementally in response to individual stakeholder requests rather than a coordinated business-unit strategy.
- Reporting depended on data distributed across Salesforce, Workday, Genesys, other operational systems and telemetry sources.
- Different dashboards used overlapping data with inconsistent definitions, creating concerns about accuracy and trust.
- The organization wanted to reduce Tableau licensing costs and take advantage of its integrated Microsoft ecosystem.
- Consolidation had to preserve the useful outcomes of existing dashboards while removing duplication and avoiding disruption for business users.
- Requirements and KPI definitions needed agreement from senior customer service leadership before implementation.

## Objective
Create a trusted, self-service analytics platform in Microsoft SQL Server and Power BI that:

- Consolidated overlapping dashboards around business-unit and audience needs.
- Provided consistent, validated definitions for operational metrics.
- Reduced duplicate development and recurring ad hoc requests.
- Gave users direct access to reliable data without depending on the analytics team for every question.
- Reduced BI licensing costs by migrating from Tableau to the Microsoft analytics ecosystem.
- Re-established stakeholder confidence in reporting accuracy.

## Your Role
I proposed the consolidation approach and led the initiative from dashboard discovery through stakeholder alignment, data modeling and Power BI delivery.

My responsibilities included:

- Inventorying and classifying the existing Tableau dashboards by business unit, target audience, usage and analytical purpose.
- Identifying duplicated, overlapping and inactive reporting assets.
- Consolidating dashboard requirements into a smaller set of business outcomes and decision-making use cases.
- Reviewing and finalizing customer service requirements with director- and VP-level leaders.
- Defining common metrics, business rules and validation criteria.
- Designing the Microsoft SQL Server data model and the Power BI semantic and reporting layers.
- Coordinating data integration across Salesforce, Workday, Genesys and other telemetry and operational sources.
- Mentoring analysts involved in the broader Tableau-to-Power BI migration.

## Approach & Architecture
### 1. Dashboard discovery and rationalization

- Created an inventory of existing Tableau dashboards and grouped them by business unit and intended audience.
- Reviewed usage and business purpose to distinguish actively used dashboards from duplicated, outdated or low-value assets.
- Extracted the underlying questions, decisions and KPI requirements instead of recreating each dashboard individually.
- Consolidated the requirements into a comprehensive dashboard strategy for each business unit.

### 2. Stakeholder and metric alignment

- Worked with customer service directors and the VP to agree on the outcomes the consolidated solution needed to support.
- Standardized KPI definitions and calculation logic before development.
- Used stakeholder validation throughout the build to remove assumptions and resolve data discrepancies early.

### 3. Trusted data foundation

- Integrated data from Salesforce, Workday, Genesys and other operational and telemetry sources into Microsoft SQL Server.
- Designed reusable analytical datasets and business-unit data models rather than allowing dashboards to query disconnected source extracts.
- Established SQL transformations, relationships and validation logic to create a consistent reporting foundation.

### 4. Self-service Power BI layer

- Built a compact Power BI data model on top of the governed SQL Server layer.
- Created a consolidated customer service dashboard that brought operational, workforce and customer-support information into one place.
- Enabled users to filter, explore and retrieve the information they needed without submitting routine requests to the analytics team.
- Applied Git-based change management and documented definitions to improve maintainability and governance.

### Data flow

`Salesforce + Workday + Genesys + Operational/Telemetry Sources -> Microsoft SQL Server -> Governed Analytical Data Model -> Power BI Self-Service Dashboard`

## Key Decisions & Trade-offs
- **Consolidate by business outcome rather than migrate dashboard by dashboard:** A one-to-one migration would have transferred the existing duplication into Power BI. Consolidating the questions and decisions first produced a smaller and more useful reporting estate.
- **Use a governed SQL Server layer:** Centralizing transformation and business logic prevented each Power BI report from implementing its own version of the metrics.
- **Align with the Microsoft ecosystem:** Power BI and SQL Server reduced dependency on separate Tableau licensing and integrated with the organization's existing technology landscape.
- **Design for self-service with governance:** Users gained flexibility to explore data, while shared models and definitions protected consistency and trust.
- **Prioritize stakeholder validation:** More time was invested early in agreeing on definitions and outcomes, reducing rework and data-quality disputes after release.

## Execution Highlights
- Reviewed approximately 120 Tableau dashboards across three business units and consolidated them into three comprehensive Power BI solutions.
- Rationalized approximately 70-80 customer service dashboards into a single trusted customer service analytics experience.
- Partnered with director- and VP-level customer service leaders to finalize requirements and KPI definitions.
- Integrated data from multiple business systems into a common Microsoft SQL Server analytical layer.
- Coordinated with data engineering and business stakeholders to validate source data, transformations and calculations.
- Led and mentored three analysts during the broader Tableau-to-Power BI migration.
- Documented metric definitions, calculation logic and validation decisions for future maintenance.

## Outcome & Impact
- Consolidated approximately 120 Tableau dashboards into three business-unit Power BI solutions covering customer service, technical support and digital experience.
- Replaced approximately 70-80 fragmented customer service dashboards with one comprehensive and trusted analytical solution.
- Reduced Tableau licensing dependency and associated BI platform costs by moving reporting into the Microsoft ecosystem.
- Eliminated 95% of ad hoc data requests by enabling reliable self-service access.
- Reduced duplicate development, maintenance effort and back-and-forth between stakeholders and the analytics team.
- Established consistent KPI definitions and a single source of truth across previously fragmented reporting.
- Rebuilt confidence in the data; recurring data-quality complaints were eliminated for the consolidated solution after rollout.
- Created a reusable SQL Server and Power BI foundation for future reporting instead of continuing to build isolated dashboards for individual requests.

## Artifacts
- Consolidated customer service Power BI dashboard.
- Business-unit Power BI solutions for technical support and digital experience.
- Microsoft SQL Server analytical datasets and transformation logic.
- KPI and metric-definition documentation.
- Dashboard inventory and rationalization mapping.
- Data-validation and stakeholder sign-off records.

## Learnings
- Dashboard migration should begin with rationalizing business questions and decisions, not recreating existing reports in a new tool.
- Self-service analytics succeeds only when users trust the underlying data, definitions and validation process.
- A shared analytical model reduces both technical duplication and repeated debates about metric accuracy.
- Senior stakeholder alignment is essential when consolidating reports used by teams with different priorities.
- Usage and ownership should be monitored continuously so obsolete dashboards can be retired before reporting sprawl returns.
- BI platform modernization can deliver both technical and financial benefits when architecture, governance and licensing strategy are considered together.
