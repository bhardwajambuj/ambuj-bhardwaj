---
type: project
name: Apache Superset Platform Transformation and Production Architecture
timeframe: 2024–present
organization: Skan AI
project_type: analytics platform modernization
domains:
  - Analytics Platform Architecture
  - Embedded Analytics
  - Platform Engineering
  - BI Governance
  - Production Operations
tools:
  - Apache Superset
  - Angular
  - Auth0
  - Kubernetes
  - PostgreSQL
  - Redis
  - Celery
  - Gunicorn
  - StarRocks
  - Git
  - LLMs
  - Semantic Documentation
role: platform strategy and architecture lead
visibility_level: product, engineering, DevOps and leadership
status: phased rollout and continuing platform evolution
---

## Quick Answer

I led the strategy and architecture work to transition Skan's customer-facing analytics capability towards Apache Superset. The initiative covered technology evaluation, embedded analytics, Angular integration, Skan branding, Auth0-based SSO, role-based access, Kubernetes deployment environments, release management, data modeling standards and production performance engineering. I also helped turn SQL Lab into an assisted analytics experience through a custom FAQ and verified-query widget, semantic-layer-grounded AI text-to-SQL, and interaction logging for quality, latency, token usage, cost and traceability. The goal was to establish an extensible analytics platform and product experience rather than simply replace one dashboard tool with another.

## What Business Problem Did the Project Solve?

Skan needed an analytics platform that could be embedded into its web product, support customer-facing use cases and accommodate different customer deployment requirements, including on-premises environments for highly regulated organizations.

A conventional BI deployment model did not fully address the product requirements around integrated user experience, customer-specific data access, release control and deployment flexibility. The organization needed a platform architecture spanning the BI application, web product, identity provider, analytical database and deployment infrastructure.

## What Was the Objective?

1. Evaluate Superset as an alternative and complement to the existing BI stack.
2. Define a phased migration and implementation roadmap.
3. Embed dashboards into the Skan web application.
4. Establish authentication, authorization and governance patterns.
5. Define Kubernetes deployment and environment-promotion practices.
6. Establish scalable query execution and operational patterns.
7. Support cloud and on-premises customer requirements.

## What Did I Own?

- Platform evaluation and migration roadmap.
- Target architecture and implementation sequencing.
- Collaboration with Product Managers on customer and product requirements.
- Collaboration with Engineering Managers on Angular embedding and SSO integration.
- Requirements for Skan branding and a consistent product-integrated Superset experience.
- Product and architecture design for the custom SQL Lab FAQ and verified-query widget.
- Semantic-layer-grounded AI text-to-SQL integration and evaluation telemetry.
- Collaboration with DevOps on Kubernetes deployments and environment configuration.
- Dataset, dashboard and visualization governance standards.
- Operational design and troubleshooting across web, worker, cache and database components.
- Delivery-capability development through hiring a full-time Analyst, a Data Engineer and a Superset Consultant.

## How Did the Platform Architecture Work?

The architecture connected the Skan web application to embedded Superset dashboards, with Auth0 involved in the authentication flow and Superset responsible for dashboard, dataset and query experiences. StarRocks served analytical workloads for the Superset reporting layer, while PostgreSQL held Superset metadata. Kubernetes provided the deployment model across development, QA, performance testing, premaster and production environments.

The platform design also considered:

- Web application and embedded dashboard integration.
- User authentication and identity propagation.
- Skan branding and user-experience customization.
- Superset roles, permissions, datasets and dashboard access.
- Database connection and query execution behavior.
- Categorized FAQs and verified SQL insertion within SQL Lab.
- Plain-English-to-SQL generation grounded in semantic documentation.
- Logging of questions, responses, latency and token consumption for evaluation and traceability.
- Redis and Celery for asynchronous/background execution patterns.
- Environment-specific configuration and release promotion.
- Operational monitoring and performance testing.

## Delivery and Governance Approach

- Defined a phased implementation roadmap rather than treating migration as a one-time cutover.
- Established visualization and data modeling standards for customer-facing dashboards.
- Worked on dashboard export/import workflows to promote content between environments.
- Used Git and repository-based workflows to support controlled changes and collaboration.
- Considered role-based access for embedded and guest users.
- Evaluated platform features against customer requirements and known differences from Power BI, including cross-filtering, multi-dataset charting and certain calculations.

## Production Engineering and Performance Work

- Evaluated Gunicorn worker and thread configurations for web request handling.
- Worked through Celery worker configuration and task distribution.
- Investigated Redis integration and asynchronous query execution.
- Troubleshot cases where background tasks were not being consumed as expected.
- Evaluated concurrency across Superset web pods, worker pods and StarRocks compute nodes.
- Investigated the relationship between dashboard latency, query execution and available database resources.
- Worked with DevOps and SRE on deployment stability and production readiness.

Specific pod counts, worker concurrency values and environment sizes changed during testing and should be documented in a separate engineering runbook rather than treated as permanent architecture specifications in this career narrative.

## Important Architecture Decisions and Trade-offs

### Embedded analytics versus standalone BI

Embedding Superset created a more integrated customer experience, but introduced dependencies on application authentication, authorization, frontend behavior and release management.

### Open-source flexibility versus feature parity

Superset offered deployment flexibility and extensibility, but did not reproduce every Power BI capability in the same way. The team needed to establish supported visualization patterns and avoid promising one-to-one parity where the product behavior differed.

### Synchronous versus asynchronous query execution

Synchronous execution can be sufficient for simpler workloads, but longer-running or concurrent requests may benefit from asynchronous execution. That requires reliable worker orchestration, Redis configuration and operational monitoring; enabling a feature flag alone does not guarantee a working async pipeline.

### Shared platform versus customer-specific deployment

A shared instance can improve operational efficiency, but customer isolation and deployment requirements may require carefully designed database access, permissions or separate deployment patterns.

## What Was the Outcome?

- Established the architecture and phased roadmap for Superset as a customer-facing analytics platform.
- Defined the integration approach with the Skan web application and Angular frontend.
- Established authentication, authorization, deployment and content-promotion workstreams.
- Delivered a Skan-branded, SSO-integrated Superset experience.
- Added a custom SQL Lab assistant for categorized FAQs, verified SQL and semantic-layer-grounded AI text-to-SQL.
- Established interaction telemetry for AI quality evaluation, latency analysis, token tracking, cost optimization and traceability.
- Created a foundation for cloud and on-premises analytics deployments.
- Built delivery capacity across analytics, data engineering and Superset specialization.
- Identified and worked through key production bottlenecks across application, worker and analytical database layers.

Avoid describing every architecture component as fully deployed until each has been verified in the current production environment.

## What Artifacts Were Produced?

- Superset target architecture and phased roadmap.
- Deployment and environment strategy.
- Embedding and authentication integration requirements.
- Skan branding and user-experience customizations.
- SQL Lab FAQ taxonomy, verified-query library and direct editor-insertion workflow.
- Semantic-layer-grounded AI text-to-SQL integration.
- AI interaction logging and evaluation framework.
- RBAC and dataset-governance approach.
- Dashboard export/import and release process.
- Performance test findings and operational configuration guidance.
- Visualization and data modeling standards.

## What Would I Measure Next?

- Production customer and tenant adoption.
- Dashboard and chart counts.
- Concurrent-user test results.
- P50/P95 dashboard load times and query latency.
- Query failure and timeout rates.
- Availability and deployment success rate.
- Operational cost by deployment model.
- Time required to promote and roll back dashboard changes.

## What Did I Learn?

- Replacing a BI tool is a product and platform transformation, not only a visualization migration.
- Embedded analytics requires identity, authorization, frontend and data-platform decisions to work together.
- Asynchronous execution is an end-to-end system involving web servers, queues, workers, caches and databases.
- Open-source platform flexibility comes with responsibility for integration, operations and feature-gap management.
- Performance testing must isolate application, worker and database bottlenecks.

## Frequently Asked Questions

### Why was Superset selected?

It offered an open-source and deployable analytics foundation that could be embedded in the Skan product and adapted for different customer deployment requirements.

### Which components were involved?

Superset, Angular, Auth0, Kubernetes, PostgreSQL metadata storage, Redis, Celery, Gunicorn and StarRocks were among the technologies involved.

### Was the platform intended only for cloud deployment?

No. On-premises deployment was an important requirement for highly regulated customers.

### Was this just a dashboard migration?

No. The work included product embedding, authentication, authorization, data access, deployment, release management, performance and operational architecture.
