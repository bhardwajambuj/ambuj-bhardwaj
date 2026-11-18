---
type: project
name: Automated Standard QBR Generator
timeframe: 2020-2022
organization: Citrix (now Cloud Software Group)
project_type: internal
domains: [Customer Success, Technical Account Management, Reporting Automation, Quarterly Business Reviews]
tools: [Tableau, Power BI, PowerPoint, PDF, SQL]
role: owner
visibility_level: org
status: completed
---

## Problem Statement
Technical Account Managers and Customer Success teams regularly prepared Quarterly Business Review (QBR) presentations for their customer accounts. Depending on each customer's review and billing schedule, the teams created these decks monthly or quarterly.

Preparing a new presentation was a repetitive and largely manual activity. Account teams repeatedly asked the data analytics team to gather customer-specific metrics, update charts and format the information in a presentation. Each deck could take approximately two days to complete.

The volume of repeated requests consumed significant analytics capacity. It also created a risk that decks prepared by different people would use inconsistent layouts, metrics or presentation standards. Analysts spent time reproducing established reporting instead of working on advanced analytics, automation and insight generation.

## Context & Constraints
- QBRs were customer-facing and needed to follow Citrix's standard presentation format.
- Each Technical Account Manager managed different customer accounts and review schedules.
- Users needed to select a customer and reporting period without requesting analyst support.
- The generated deck had to contain current customer-specific information while preserving a consistent structure and visual design.
- The output needed to be downloadable in PowerPoint or PDF format for review and customer presentation.
- The solution had to be simple enough for non-technical users to operate in a few clicks.

## Objective
Create a self-service QBR generator that allowed account teams to produce standardized, customer-ready presentations without recurring support from the data analytics team.

Success meant:

- Reducing QBR preparation from approximately two days to a few minutes.
- Eliminating recurring deck-creation requests to the analytics team.
- Standardizing the structure, metrics and visual presentation of QBRs.
- Allowing users to select a customer and date range independently.
- Producing PowerPoint and PDF files ready for internal review or customer presentation.
- Releasing analyst capacity for higher-value analytics and insight generation.

## Your Role
I designed and delivered the dashboard-based QBR automation workflow.

My responsibilities included:

- Understanding the repeated QBR preparation process and the information required by account teams.
- Consolidating the recurring requirements into a standard presentation structure.
- Defining customer and date-range selection controls.
- Designing the Tableau and Power BI reporting experience.
- Organizing the dashboard pages so they could be exported as a consistent presentation.
- Validating the output with Technical Account Managers and Customer Success stakeholders.
- Enabling users to generate and download presentations without analyst intervention.

## Approach & Architecture
### 1. Standardize the QBR structure

- Identified the metrics, charts and account information repeatedly requested in customer QBRs.
- Converted these requirements into a standard company-aligned presentation template.
- Defined a consistent order and visual structure for every generated deck.

### 2. Parameterize the customer context

- Added customer selection and date-range filters to the dashboard.
- Applied the selected values across all relevant views so every page represented the same account and reporting period.
- Designed the workflow so users could generate a complete account-level QBR with only a few selections.

### 3. Design for presentation export

- Structured the Tableau dashboard pages to align with the standard QBR presentation format.
- Ensured that titles, charts, metrics and filters rendered consistently in exported files.
- Enabled direct download to PowerPoint or PDF for sharing with customers.
- Applied the same reusable reporting approach within the Power BI environment.

### 4. Enable self-service use

- Provided a simple workflow for account teams: open the dashboard, select the customer, choose the date range and export the presentation.
- Removed the need for analysts to manually rebuild charts and decks for each account.

### Workflow

`Select Customer -> Select Reporting Period -> Refresh Customer-Specific Views -> Generate Standard QBR -> Export to PowerPoint or PDF`

## Key Decisions & Trade-offs
- **Automate a standardized deck instead of individual requests:** A common structure enabled reuse and consistency, while one-off deck creation would have continued consuming analytics capacity.
- **Use dashboard filters as the input mechanism:** Customer and date-range controls made the workflow accessible to non-technical users without requiring a separate application.
- **Design the report for export from the beginning:** Dashboard layouts were created to work as presentation pages, avoiding manual reformatting after export.
- **Support PowerPoint and PDF:** PowerPoint allowed account teams to review and adapt the presentation when necessary, while PDF provided a stable customer-ready output.
- **Balance standardization with account flexibility:** The core layout and metrics remained consistent, while customer and period selections allowed each deck to reflect the relevant account context.

## Execution Highlights
- Converted a repeated manual reporting request into a reusable self-service analytics product.
- Consolidated QBR requirements from Technical Account Managers and Customer Success teams.
- Created a standardized dashboard and presentation layout aligned with company expectations.
- Implemented customer and reporting-period selection across all QBR views.
- Enabled direct PowerPoint and PDF export from the Tableau workflow.
- Validated the generated output for consistency, usability and customer readiness.
- Enabled account teams to generate presentations independently in a few clicks.

## Outcome & Impact
- Reduced QBR deck preparation time from approximately two days to approximately two minutes.
- Eliminated recurring QBR deck-creation requests to the data analytics team.
- Established a consistent company-standard format across customer presentations.
- Enabled Technical Account Managers and Customer Success teams to generate customer-specific presentations independently.
- Reduced manual data gathering, chart preparation, formatting and review effort.
- Improved turnaround time for monthly and quarterly customer reviews.
- Released analytics-team capacity for advanced analytics, automation and deeper insight generation.
- Created a repeatable self-service workflow that scaled across accounts and reporting cycles.

## Artifacts
- Tableau-based QBR generator.
- Power BI reporting implementation.
- Standard QBR presentation layout.
- Customer and date-range selection workflow.
- PowerPoint and PDF export outputs.
- User instructions for generating and downloading QBR decks.

## Learnings
- High-volume analytics requests often represent a repeatable product opportunity rather than a need for additional manual capacity.
- Designing dashboards for export requires different layout decisions from designing purely interactive reports.
- Standardization improves both operational efficiency and the consistency of customer-facing communication.
- Self-service tools achieve adoption when the workflow is simpler than submitting a request to the analytics team.
- Automating routine reporting creates space for analysts to focus on interpretation, advanced analysis and innovation.
- Reusable templates should be governed and reviewed periodically so metrics and presentation standards remain current.
