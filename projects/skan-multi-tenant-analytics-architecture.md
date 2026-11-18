---
type: project
name: Multi-Tenant Access and Isolation Architecture for Embedded Analytics
timeframe: 2026 (design and validation; confirm start date)
organization: Skan AI
project_type: platform security and architecture
domains:
  - Multi-Tenant SaaS Architecture
  - Identity and Access Management
  - Embedded Analytics
  - Data Security
  - BI Governance
tools:
  - Apache Superset
  - Auth0
  - PostgreSQL
  - SQL Lab
  - Superset RBAC
  - Customer Database Connections
role: architecture contributor / design owner for analytics access model
visibility_level: Product, Engineering, Data Platform and security stakeholders
status: in progress – design and validation
---

## Quick Answer

I worked on the access-control architecture required to support multiple customer databases within a Superset analytics environment. The design considers how Auth0 identities map to Superset users and tenant-specific roles, and how those roles restrict access to the correct database connections, datasets, SQL Lab capabilities and dashboards. The central architectural concern is preventing cross-tenant data exposure while retaining a manageable customer-facing analytics experience. This work should be described as design and validation unless the isolation controls have been fully implemented and security-tested in production.

## What Business Problem Did the Project Solve?

Skan's customer-facing analytics requirements include the possibility of multiple customer databases being connected to the same Superset instance. In that model, users must be able to work with their own tenant's data without seeing or querying another customer's data.

Authentication alone is not sufficient. A successfully authenticated user could still be exposed to another tenant's database, dataset or dashboard if the authorization model is incomplete.

The platform therefore needs a tenant-aware access model across identity, roles, database connections, datasets, SQL Lab and dashboard access.

## What Was the Objective?

1. Map authenticated customer identities to the correct Superset user and role.
2. Restrict users to their own tenant's database connections.
3. Control access to SQL Lab and other data exploration capabilities.
4. Prevent cross-tenant access to datasets and dashboards.
5. Establish an approach that can be administered as the number of customers grows.
6. Validate the model through negative as well as positive access tests.

## What Did I Work On?

- Evaluated the interaction between Auth0 authentication and Superset authorization.
- Worked through tenant-specific database connection and role requirements.
- Considered a Gamma-based permission baseline with only the necessary SQL Lab permissions granted.
- Explored tenant-specific custom roles and the implications of database-level access restrictions.
- Assessed whether restricting database connections alone is sufficient to protect dashboards and datasets.
- Identified the need to test access paths through SQL Lab, datasets, chart APIs, dashboards and embedded views.

## How Should the Access Model Work?

1. **Authenticate:** Auth0 validates the user's identity through the Skan application flow.
2. **Resolve tenant:** The application or trusted identity context determines the user's tenant association.
3. **Map identity:** The authenticated identity is mapped to the corresponding Superset user.
4. **Assign role:** The user receives a tenant-appropriate role and permissions.
5. **Restrict data connections:** The role exposes only the database connection or approved datasets for that tenant.
6. **Restrict content:** Dashboard, chart and dataset permissions are aligned with the same tenant boundary.
7. **Test isolation:** Positive tests confirm a user can access permitted content; negative tests confirm that another tenant's resources cannot be accessed through UI or API paths.

## Key Design Questions and Trade-offs

### Is a shared Gamma role sufficient?

A broad built-in role may provide a useful baseline, but tenant isolation generally requires tenant-specific authorization and careful control of database, dataset and dashboard permissions. The exact permission set must be validated against the deployed Superset version and custom security configuration.

### Does restricting database connections isolate dashboards?

Not necessarily. Dashboards and charts also reference datasets and metadata objects. Access control must cover all relevant resources and API paths, not only the database connection picker or SQL Lab interface.

### Where should tenant identity be enforced?

The tenant mapping should come from a trusted application or identity context. It should not rely on a user-supplied tenant identifier that can be modified by the client.

### Shared instance or separate instances?

A shared instance can reduce operational overhead, but requires rigorous authorization, tenant-aware administration and security testing. Separate instances may provide stronger operational isolation at the cost of additional infrastructure and lifecycle management.

## Validation Scenarios

A production-ready design should include at least the following tests:

- Tenant A can see only its approved database connections.
- Tenant A cannot enumerate or query Tenant B datasets.
- Tenant A cannot open Tenant B dashboards by direct URL.
- Tenant A cannot retrieve Tenant B chart data by calling chart-data APIs directly.
- SQL Lab cannot be used to query a database outside the user's authorization scope.
- Export, download, drill-down and embedded dashboard paths do not bypass access controls.
- Role changes and user deactivation take effect as expected.
- Administrative and service accounts are separately governed and audited.

## What Was the Outcome So Far?

- Clarified that multi-tenant analytics requires coordinated identity and authorization design.
- Identified tenant-specific database access as one layer of the solution, not the complete isolation control.
- Established the need to test dashboards, datasets, SQL Lab and API access independently.
- Defined design considerations for Auth0 identity mapping and tenant-specific Superset roles.

This record intentionally does not claim that complete cross-tenant isolation has been deployed or certified. Update the status and outcomes once implementation and security validation are complete.

## What Artifacts Should Be Produced?

- Identity-to-tenant-to-role mapping specification.
- Superset role and permission matrix.
- Database and dataset access-control matrix.
- Tenant-aware dashboard ownership and sharing rules.
- Positive and negative security test cases.
- Audit and operational procedures for customer onboarding and offboarding.

## What Would I Measure or Validate Next?

- Number of tenants and users supported by the shared instance.
- Percentage of tenant-isolation test cases passing.
- Attempts to access unauthorized databases, datasets, charts and dashboards.
- Time to provision and revoke tenant access.
- Administrative effort per customer onboarding.
- Audit coverage for permission and role changes.

## What Did I Learn?

- Authentication and authorization solve different problems.
- Database connection restrictions alone do not prove end-to-end tenant isolation.
- Embedded analytics security must be tested at UI, API, dataset and database layers.
- Tenant identity must be derived from a trusted source and consistently enforced.
- Security architecture should include explicit negative tests that attempt to cross tenant boundaries.

## Frequently Asked Questions

### What problem was being addressed?

Supporting multiple customers and databases within a Superset instance without exposing one tenant's data or dashboards to another tenant.

### What was Auth0's role?

Auth0 was part of the authentication and identity flow. Superset roles and permissions were considered for authorization and resource access.

### Would a Gamma role alone guarantee tenant isolation?

No. The full permission model and access paths need to be evaluated, including databases, datasets, dashboards, SQL Lab and APIs.

### Is the project complete?

The record reflects design and validation work. Production implementation and security certification should be stated only after they are confirmed.
