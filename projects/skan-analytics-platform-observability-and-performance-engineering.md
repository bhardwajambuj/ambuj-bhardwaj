---
type: project
name: Analytics Platform Observability and Performance Engineering
timeframe: 2025–present
organization: Skan AI
project_type: platform reliability and performance engineering
domains:
  - Observability
  - SRE Collaboration
  - Load and Concurrency Testing
  - Analytics Infrastructure
  - Query Performance
tools:
  - Grafana
  - Apache Superset
  - StarRocks
  - Kubernetes
  - Gunicorn
  - Celery
  - Redis
  - SQL
role: analytics platform architecture and performance lead
visibility_level: Data Platform, SRE, DevOps and Engineering
status: ongoing
---

## Quick Answer

I worked with SRE and DevOps to establish observability and performance-engineering practices for Skan's analytics platform, particularly Superset and StarRocks. The work covered monitoring requirements, Grafana visibility, load testing, concurrent dashboard execution and investigation of bottlenecks across web pods, background workers, Redis and analytical compute. The objective was to move from testing whether a dashboard worked for a single user to understanding whether the complete platform could support expected customer concurrency and production workloads.

## What Business Problem Did the Project Solve?

A dashboard might load quickly for one user but degrade when multiple users interact with several charts simultaneously. In a production embedded analytics platform, latency can originate at different layers:

- Browser and application request handling.
- Superset web workers and Gunicorn configuration.
- Query queueing and Celery worker distribution.
- Redis and asynchronous query coordination.
- StarRocks query execution and compute capacity.
- Kubernetes resource limits and scheduling.

Without end-to-end monitoring and repeatable load tests, teams risk changing the wrong component or scaling infrastructure that is not the actual bottleneck.

## What Was the Objective?

1. Establish visibility into analytics application and database performance.
2. Define key metrics for Superset, StarRocks and supporting services.
3. Test realistic concurrent dashboard workloads.
4. Identify bottlenecks across web, worker, queue and database layers.
5. Inform infrastructure sizing and configuration decisions.
6. Improve production readiness and incident diagnosis.

## What Did I Own or Contribute?

- Defined analytics platform observability requirements with SRE.
- Worked on Grafana-based monitoring for platform components, including StarRocks.
- Investigated Superset web pod, Gunicorn, Celery and Redis behavior.
- Evaluated asynchronous query execution and worker task distribution.
- Analyzed the relationship between concurrent dashboard requests and database query execution.
- Conducted or coordinated load and concurrency testing.
- Used test observations to guide configuration and capacity discussions with DevOps and platform teams.

## How Did the Performance Investigation Work?

1. Establish a baseline for a dashboard and its individual chart queries under a single-user workload.
2. Increase concurrent users and repeat representative interactions.
3. Observe request handling at the Superset web tier.
4. Inspect query scheduling and asynchronous task processing where enabled.
5. Compare application and worker utilization with StarRocks compute utilization.
6. Identify whether latency comes from request queues, worker saturation, query execution or infrastructure limits.
7. Repeat tests after configuration or capacity changes.

A key observation from testing was that a workload that executed in under two seconds for a single user did not necessarily maintain that performance at 25 concurrent users. This highlighted the need to evaluate the complete request path rather than infer capacity from isolated query timings.

## Observability Areas

### Superset application

- Web pod CPU and memory utilization.
- Request rate, response time and error rate.
- Gunicorn worker and thread behavior.
- Dashboard and chart-data request latency.

### Background execution

- Celery worker availability and task throughput.
- Active, reserved and queued task counts where applicable.
- Task failures and execution duration.
- Redis connectivity and queue health.

### StarRocks

- Query latency and concurrency.
- Compute node resource utilization.
- Query failures, slow queries and workload saturation.
- Resource headroom under representative dashboard activity.

### Kubernetes and infrastructure

- Pod restarts and readiness.
- CPU and memory requests versus actual usage.
- Resource throttling and saturation.
- Service-to-service connectivity and storage dependencies.

## Important Decisions and Trade-offs

### Measure the complete request lifecycle

A single SQL execution time does not represent end-to-end chart latency. Queueing, application processing, serialization and network transfer can all contribute.

### Scale the constrained tier, not every tier

Adding web pods does not solve a database bottleneck. Increasing Celery concurrency does not help if StarRocks is saturated or tasks are not routed correctly. Observability must identify the limiting resource before scaling.

### Async execution requires a functioning system

Asynchronous query execution depends on coordinated application configuration, a message broker, workers and result handling. A feature flag by itself is not evidence that the worker pipeline is healthy.

### Test realistic dashboard behavior

A dashboard with multiple charts can trigger several queries per interaction. Testing one isolated SQL query is insufficient to model the user experience.

## What Was the Outcome?

- Established a more complete observability model for Superset and StarRocks.
- Identified performance differences between single-user and concurrent-user workloads.
- Improved understanding of the interaction between web pods, Celery workers, Redis and database compute.
- Created a basis for evidence-driven infrastructure sizing and production performance tuning.
- Strengthened collaboration between analytics engineering, SRE and DevOps.

This project record does not claim a specific production latency improvement or availability percentage because a final measured before-and-after result has not been provided.

## What Artifacts Were Produced or Should Be Retained?

- Grafana dashboard requirements and panels.
- Load-testing scenarios and test results.
- Superset and StarRocks performance baselines.
- Configuration and bottleneck investigation notes.
- Infrastructure sizing assumptions.
- Production readiness and alerting recommendations.

## What Would I Measure Next?

- P50/P95/P99 dashboard and chart-data latency.
- Successful query throughput under target concurrency.
- Query queue wait time versus database execution time.
- Celery task wait and execution duration.
- Web pod and worker saturation.
- StarRocks CPU, memory, query concurrency and slow-query rate.
- Error rate, timeout rate and dashboard availability.

## What Did I Learn?

- Performance engineering is an end-to-end discipline across application, queue, database and infrastructure layers.
- Single-user benchmarks are not representative of production concurrency.
- Increasing worker counts or pod counts can worsen contention if the real bottleneck is elsewhere.
- Observability should support diagnosis and capacity decisions, not just display infrastructure metrics.

## Frequently Asked Questions

### Why was a dashboard fast for one user but slower under concurrency?

Concurrent users create overlapping requests and queries. The bottleneck may be in Superset request handling, worker queues, database execution or infrastructure resources.

### Why monitor Celery and Redis?

They are part of the asynchronous/background execution path. A healthy web tier does not guarantee that queued work is being processed correctly.

### Why use Grafana?

It provides a shared operational view across application and infrastructure metrics and supports collaboration between analytics engineering and SRE.
