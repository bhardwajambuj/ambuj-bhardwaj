---
type: experience
organization: Skan AI
role: Data and Analytics Platform Lead
start_date: 06-2024
end_date: present
employment_type: full-time
location: Bangalore, India

primary_domains:
  - Analytics Platform Architecture
  - Data Platform Strategy
  - Process Mining
  - Data Warehousing
  - AI-powered Analytics
  - BI Strategy and Governance
  - Analytics Engineering
  - Platform Observability

primary_tools:
  - Databricks
  - Apache Spark / PySpark
  - Power BI
  - Apache Superset
  - StarRocks
  - PostgreSQL
  - Python
  - SQL
  - Azure Blob Storage
  - Microsoft Fabric
  - Grafana
  - Auth0
  - Git
  - Cursor
  - LLMs (ChatGPT, Claude, Gemini, Grok)

seniority_level:
  - Lead
  - Architect
  - Technical Leadership

visibility_level:
  - Multi-team
  - Executive Leadership
  - Customer-facing
---

## 1. Context

Skan AI is a process mining and AI-powered analytics company that enables organizations to understand actual business processes, employee workflows and time utilization across enterprise applications.

The platform captures granular digital interaction events, including mouse clicks, keyboard actions, scrolling and application interactions, followed by AI-assisted data enrichment and processing to generate process insights and power AI-driven analytical capabilities.

This role sits within the Data Platform team, with ownership spanning analytics platform strategy, BI architecture, data warehousing, reporting infrastructure and analytical enablement.

Work closely with Product Leaders, the COO, Engineering Managers, Data Platform Architects, Customer Success and customers to translate business and analytical requirements into scalable platform capabilities.

Responsibilities extend beyond BI development to technology evaluation, architecture decisions, infrastructure planning, platform deployment, cost optimization, governance, team building and production readiness.

## 2. Scope of Ownership

### Analytics Platform Strategy and Architecture
- Own analytics platform strategy, architecture and technology evaluation across Power BI, Apache Superset, Databricks and StarRocks.
- Define architectural patterns for scalable, embedded and customer-facing analytics.
- Lead platform modernization initiatives, including the transition from traditional BI reporting to a more flexible, extensible analytics platform.
- Define deployment, governance, security, performance and operational standards.
- Evaluate technology trade-offs between performance, scalability, infrastructure costs and customer requirements.

### Data Platform and Warehouse Architecture
- Architect analytical data models and data warehouse solutions supporting multi-billion-event datasets.
- Define data granularity, aggregation strategies, schema design, materialized views and refresh mechanisms.
- Establish scalable batch processing and incremental data processing strategies.
- Optimize analytical workloads across Databricks and StarRocks.

### AI and Analytics Enablement
- Establish semantic documentation and metadata standards to enable AI-assisted analytics.
- Enable customer-facing and non-data teams to access analytical insights through AI-assisted SQL generation.
- Drive the evolution towards semantic-layer-powered natural-language analytics and AI-assisted self-service reporting.
- Explore LLM and RAG architectures for analytical query generation and knowledge retrieval.

### Platform Operations and Governance
- Own BI platform performance, capacity utilization and cost optimization.
- Establish monitoring and observability practices across reporting and analytics infrastructure.
- Define platform governance, release management, access control and operational best practices.
- Collaborate with SRE and DevOps teams on production readiness, performance testing and infrastructure sizing.

### Technical and Organizational Leadership
- Build technical capabilities through hiring, mentoring and knowledge sharing.
- Lead cross-functional initiatives involving Data Engineering, BI, Product, Engineering and DevOps.
- Enable customer-facing analytics teams through reusable data models, documentation and engineering standards.
- Communicate architecture decisions, platform capabilities and business impact to senior leadership.

## 3. Major Problems Owned and Solutions Delivered

### 3.1 Enterprise Power BI Modernization and Performance Optimization

**Problem:**

The largest customer had accumulated three years of clickstream data from Skan, combined with external CRM and workforce datasets. This resulted in a highly complex Power BI solution with significant performance and maintainability issues.

The existing solution had over 30 worksheets, 70 tables and approximately 350 measures and 150 calculated columns, with no proper documentation or handover.

**Ownership and solution:**
- Reverse-engineered the existing Power BI solution, including its data model, DAX dependencies, relationships and report-level requirements.
- Designed a new data ingestion and transformation architecture using Databricks and Azure Blob Storage to fetch, sanitize and integrate external customer data.
- Reworked the analytical data model to reduce unnecessary data processing and improve query efficiency.
- Transitioned the reporting architecture from Import Mode towards DirectQuery to improve data availability and interactive performance.
- Optimized summarized datasets and reporting queries to minimize unnecessary processing.
- Established a more maintainable and documented reporting architecture.

**Impact:**
- Improved Power BI report refresh performance by up to 80%.
- Reduced the size of the largest reporting datasets by approximately 98%.
- Established a scalable data preparation pipeline for customer-specific analytical requirements.
- Improved maintainability and reduced dependency on undocumented legacy models.

### 3.2 Power BI Platform Cost and Capacity Optimization

**Problem:**

Power BI Premium P2 capacity and Databricks SQL Warehouses experienced prolonged resource consumption due to scattered refresh schedules, long-running refresh operations and overlapping workloads.

This resulted in sustained capacity utilization and increased infrastructure costs through autoscaling.

**Ownership and solution:**
- Took ownership of Power BI platform administration, performance monitoring and capacity optimization.
- Analyzed capacity utilization, refresh execution patterns and Databricks SQL Warehouse consumption.
- Identified long-running and scattered refreshes that kept Power BI capacity and Databricks compute resources active for almost 22 hours per day.
- Worked with the Databricks Architect to correlate BI refresh activity with data engineering workloads and infrastructure consumption.
- Redesigned the data refresh strategy to align dashboard usage, data pipeline completion and compute availability.
- Consolidated report refreshes into a controlled five-hour execution window.
- Established monitoring to track refresh performance, failures, capacity consumption and adherence to refresh schedules.

**Impact:**
- Reduced Power BI capacity utilization from approximately 85% to 45%.
- Reduced Databricks DBU consumption by approximately 58%.
- Reduced the refresh execution window from almost 22 hours to approximately five hours.
- Improved infrastructure availability and resource utilization during peak business hours.

### 3.3 Enterprise Analytics Platform Transformation – Power BI to Apache Superset

**Problem:**

The organization required a more flexible and cost-effective analytics platform that could support customer-facing embedded analytics, on-premises deployments and evolving customer data requirements.

**Ownership and solution:**
- Led the analytics platform strategy and transition towards Apache Superset.
- Defined a phased implementation roadmap covering technology evaluation, architecture, deployment, data modeling, visualization standards, governance and production rollout.
- Designed Superset as an embedded analytics platform integrated into the Skan web application.
- Collaborated with Product and Engineering teams on dashboard embedding within the Angular application.
- Worked on Auth0-based authentication and SSO integration.
- Designed RBAC and guest-user permission models for controlled access to dashboards, datasets and SQL Lab.
- Evaluated tenant-specific database access and authorization strategies to prevent cross-customer data access.
- Defined Kubernetes-based deployment strategies across Development, QA, Performance Testing, Premaster and Production environments.
- Established dashboard export/import and promotion processes across environments using Git and version-controlled artifacts.
- Evaluated Superset capabilities and limitations against Power BI to define appropriate visualization and data modeling patterns.
- Built the delivery capability by hiring a full-time Analyst, Data Engineer and Superset Consultant.

**Platform engineering and performance:**
- Evaluated Superset web server configurations, Gunicorn workers, threads and Celery concurrency.
- Worked on Redis and asynchronous query execution architecture.
- Investigated Celery task distribution and background query execution issues.
- Conducted concurrent-user performance testing across Superset and StarRocks.
- Investigated performance bottlenecks across application pods, worker infrastructure and analytical database compute nodes.
- Collaborated with SRE and DevOps teams on infrastructure sizing and production readiness.
- Designed the foundation for customer deployments, including on-premises environments for highly regulated customers.

**Impact:**
- Established the architectural foundation for a customer-facing embedded analytics platform.
- Created a reusable deployment and governance framework.
- Enabled the organization to support more flexible customer analytics requirements.
- Established a foundation for cloud and on-premises analytics deployments.

### 3.4 Data Warehouse Architecture and Analytical Data Modeling

**Problem:**

Reporting workloads were heavily dependent on transactional and granular event datasets. This resulted in expensive analytical queries, unnecessarily large reporting datasets and long refresh durations.

**Ownership and solution:**
- Designed and architected the analytical data warehouse across Databricks and StarRocks.
- Defined analytical schemas, table granularity, aggregation strategies and reusable data models.
- Designed SQL transformations and materialized views to support reporting workloads.
- Established data modeling patterns for process mining datasets, including event summaries, case summaries, participant engagement and bottleneck analysis.
- Designed incremental processing strategies to capture late-arriving data and historical changes.
- Established refresh frequencies aligned with reporting requirements and data pipeline execution.
- Optimized summarized datasets to reduce storage requirements and query processing overhead.
- Moved reporting workloads away from direct consumption of transactional data.
- Designed reusable analytical datasets to support Power BI, Superset and AI-powered analytics.
- Documented SQL queries, dataset granularity, business definitions, metadata and analytical use cases to support governance and AI consumption.

**Impact:**
- Reduced the size of the largest reporting tables by approximately 98%.
- Reduced record counts by approximately 70% through strategic aggregation and summarization.
- Improved Power BI report refresh performance by up to 80%.
- Enabled incremental processing with late-arriving data handling.
- Established reusable data models supporting both traditional reporting and AI-powered analytical capabilities.

## 4. Key Initiatives and Projects

### 4.1 PBI Doctor – Automated Power BI Documentation and Model Analysis

**Problem:** Power BI projects lacked sufficient technical documentation, making model maintenance, knowledge transfer, optimization and migration difficult.

**Solution:**
- Independently designed and built a Python-based desktop application using PyQt5.
- Developed automated metadata extraction from PBIP projects, report JSON and TMDL definitions.
- Extracted tables, columns, measures, calculated columns, relationships and Power Query definitions.
- Classified regular and calculated tables and identified dependencies between DAX measures and columns.
- Analyzed usage across DAX expressions, relationships and report visuals.
- Generated technical documentation and Excel-based metadata exports.
- Identified unused columns, measures and model dependencies to simplify existing data models.

**Impact:**
- Introduced repeatable technical documentation for standard and customer-specific Power BI dashboards.
- Improved handover and maintenance processes.
- Supported model simplification and optimization.
- Presented the solution and its organizational use cases during a company-wide town hall.

### 4.2 Power BI Health Monitor – BI Governance and Observability

Designed a centralized monitoring dashboard to provide visibility into Power BI platform health and reporting governance.

**Key capabilities:**
- Monitor capacity utilization across workspaces and reports.
- Identify slow-running and inactive reports for cleanup and optimization.
- Track report refresh duration and Databricks job completion times.
- Monitor refresh failures and identify ownership for proactive resolution.
- Validate adherence to the centralized data refresh strategy.
- Highlight performance degradation and resource consumption patterns.

**Impact:**
- Improved visibility into Power BI platform health.
- Enabled proactive identification of performance and refresh issues.
- Established a governance mechanism for workspace and report lifecycle management.

### 4.3 Skan BI Assistant and Semantic Layer

**Objective:** Enable customer-facing teams and non-data analysts to access analytical insights without requiring extensive SQL knowledge or dependency on BI developers.

**Key contributions:**
- Established a semantic documentation framework covering business metrics, KPI definitions, data granularity, SQL queries and analytical use cases.
- Organized warehouse metadata and business definitions to support consistent metric interpretation.
- Customized Apache Superset with Skan branding and SSO integration to create a consistent product experience.
- Designed a custom SQL Lab widget that organizes common analytical questions into categories and subcategories.
- Enabled users to insert reviewed and verified SQL queries directly into the SQL editor without first understanding the underlying data model.
- Integrated an AI agent that converts plain-English questions into SQL grounded in Skan's semantic-layer documentation.
- Combined deterministic FAQ-based assistance with flexible AI-generated SQL in the same user workflow.
- Designed an observability framework that captures questions, AI responses, generated SQL, timestamps, response latency, token consumption and traceability metadata.
- Established an evaluation loop for improving semantic context, response quality, performance and model cost.

**Impact:**
- Made SQL Lab accessible to users without prior knowledge of Skan's data model.
- Improved discoverability and reuse of approved analytical queries.
- Enabled semantic-layer-grounded natural-language-to-SQL assistance.
- Reduced dependency on analysts for common and exploratory analytical questions.
- Established measurable AI operations covering quality, latency, token usage, cost optimization and interaction-level traceability.

### 4.4 Analytics Platform Observability and Capacity Engineering

**Objective:** Establish production-grade observability and performance monitoring across the analytics stack.

**Key contributions:**
- Designed observability requirements for Superset, StarRocks and supporting infrastructure.
- Worked with SRE teams on Grafana dashboards for platform monitoring.
- Identified key metrics covering query execution, application performance, compute utilization and infrastructure saturation.
- Investigated Superset web pods, Celery workers, Redis and StarRocks compute node performance.
- Conducted load testing and concurrent-user performance analysis.
- Evaluated infrastructure sizing based on workload, customer volumes and concurrency.
- Established a framework for identifying application-level and database-level bottlenecks.

**Impact:**
- Improved visibility into analytics platform performance.
- Enabled systematic investigation of performance degradation.
- Established a foundation for capacity planning and production scalability.

### 4.5 Training, Mentoring and Analytics Capability Development

- Organized three knowledge-sharing and technical grooming sessions focused on handling multi-million and multi-billion-record datasets.
- Mentored and enabled a group of approximately 10 customer-facing Data Analysts.
- Shared best practices for data modeling, SQL optimization, aggregation strategies and Power BI reporting.
- Established documentation and implementation checklists for Power BI and Superset.
- Built and developed the analytics delivery team through hiring, mentoring and technical guidance.

## 5. Additional Architecture and Engineering Responsibilities

### Customer-facing and Multi-tenant Analytics
- Designed approaches for supporting multiple customer databases within a shared Superset instance.
- Evaluated tenant-specific database connections and role-based authorization.
- Worked on mapping Auth0 identities to Superset roles and permissions.
- Evaluated restrictions for cross-tenant access to databases, datasets and dashboards.
- Explored extensible data ingestion and modeling approaches to support customer-provided datasets.
- Established architectural patterns for reusable customer-facing analytics capabilities.

### Data Platform Integration
- Worked across Databricks, Delta Lake, Azure Blob Storage and StarRocks.
- Evaluated workload allocation between data processing and analytical serving layers.
- Defined data processing and reporting dependencies.
- Optimized the relationship between upstream data pipeline completion and downstream dashboard refreshes.
- Supported analytical datasets for process mining, customer reporting and AI insights.

### Platform Deployment and Release Management
- Defined environment-specific deployment and promotion practices.
- Established dashboard export/import workflows and Git-based change management.
- Worked with DevOps on Kubernetes-based application deployment.
- Evaluated application configuration, authentication, networking and production troubleshooting requirements.
- Supported platform stability and recovery discussions involving Superset metadata databases, configuration and deployment infrastructure.

## 6. Impact and Outcomes

### Performance and Cost Optimization
- Reduced Power BI capacity utilization from approximately 85% to 45%.
- Reduced Databricks DBU consumption by approximately 58%.
- Improved Power BI report refresh performance by up to 80%.
- Reduced the reporting dataset storage footprint by approximately 98%.
- Reduced record counts by approximately 70% through analytical summarization.
- Consolidated reporting refreshes into a five-hour execution window.

### Platform and Architecture
- Led the transition strategy towards Apache Superset as an embedded analytics platform.
- Designed a scalable data warehouse across Databricks and StarRocks.
- Established reusable analytical data models for reporting and AI-powered analytics.
- Designed incremental processing mechanisms to capture late-arriving data.
- Established architecture and governance practices for customer-facing analytics.
- Developed platform monitoring and observability requirements.

### AI and Analytics Enablement
- Established semantic documentation for business metrics, data models and analytical queries.
- Customized Superset with Skan branding, SSO and a SQL Lab assistant for categorized FAQs and verified SQL.
- Enabled semantic-layer-grounded AI generation of SQL from plain-English questions.
- Established interaction logging for questions, responses, latency and token consumption to support quality evaluation, cost optimization and traceability.
- Combined curated query assistance and AI-generated SQL to expand self-service analytical capabilities.

### Organizational Impact
- Built and developed analytics delivery capabilities through hiring and mentoring.
- Enabled approximately 10 customer-facing analysts through technical knowledge sharing.
- Introduced automated Power BI documentation through PBI Doctor.
- Established reporting, data modeling and platform governance best practices.
- Presented internal engineering solutions and platform capabilities to company leadership.

## 7. Technology Stack

### Data Engineering and Warehousing
- Databricks
- Apache Spark
- PySpark
- Delta Lake
- Azure Blob Storage
- StarRocks
- PostgreSQL
- SQL

### BI and Analytics Platforms
- Power BI Desktop and Service
- Power BI Premium Capacity Administration
- Apache Superset
- Tableau
- Microsoft Fabric

### Analytics Platform Engineering
- Kubernetes
- Gunicorn
- Celery
- Redis
- Auth0
- Grafana
- Git and CI/CD workflows

### Programming and Development
- Python
- PyQt5
- SQL
- DAX
- Power Query (M)
- Cursor

### AI and LLM Technologies
- Semantic Layer Design
- Retrieval-Augmented Generation (RAG)
- Semantic-layer-grounded Text-to-SQL
- LLM Interaction Logging and Evaluation
- Token and Cost Observability
- LiteLLM (evaluation and integration)
- ChatGPT
- Claude
- Gemini
- Grok

### Collaboration and Project Management
- Notion
- Azure Boards
- Git / Repository Management

## 8. Stakeholders and Collaboration

- COO and senior executive leadership.
- VP and Product leadership.
- Data Platform Architects.
- Engineering Managers.
- Data Engineering and BI teams.
- SRE and DevOps teams.
- Customer Success and customer-facing analysts.
- Enterprise customers and their technical stakeholders.

## 9. Skills Demonstrated

### Architecture and Strategy
- Analytics Platform Architecture
- BI Strategy and Modernization
- Data Warehouse Architecture
- Multi-tenant Analytics Architecture
- Technology Evaluation and Selection
- Platform Deployment Strategy
- Semantic Layer Architecture

### Engineering and Optimization
- Large-scale Data Processing
- Analytical Data Modeling
- SQL and Query Optimization
- BI Performance Engineering
- Infrastructure Capacity Planning
- Platform Cost Optimization
- Observability and Monitoring
- Data Governance

### AI and Innovation
- AI-powered Analytics
- LLM Integration
- RAG Architecture
- Semantic Metadata Engineering
- AI-assisted SQL Generation
- LLM Quality, Latency and Cost Evaluation
- Internal Developer Tooling

### Leadership and Execution
- Technical Leadership
- Team Building and Mentoring
- Program Planning and Execution
- Cross-functional Collaboration
- Stakeholder Management
- Executive Communication
- Customer-facing Technical Leadership
- Engineering Standards and Documentation

## 10. Learnings and Professional Growth

- Enterprise analytics platform architecture and modernization.
- Large-scale data warehouse design and analytical modeling.
- Production deployment and operational ownership of embedded analytics platforms.
- Multi-tenant security and access-control architecture.
- Distributed workload management and infrastructure performance engineering.
- BI platform governance, observability and cost optimization.
- Semantic layer design and AI-powered analytical applications.
- Technology evaluation, architecture trade-offs and engineering execution.
- Building technical teams and enabling organization-wide analytics capabilities.

---
