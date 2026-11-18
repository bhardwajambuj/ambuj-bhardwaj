---
type: project
name: Semantic Layer and AI-Assisted Analytics Enablement
timeframe: 2025–present (confirm rollout dates)
organization: Skan AI
project_type: AI and analytics enablement
domains:
  - Semantic Modeling
  - Self-Service Analytics
  - LLM-assisted Analytics
  - Knowledge Engineering
  - SQL Generation
tools:
  - Apache Superset
  - SQL
  - Databricks
  - StarRocks
  - LiteLLM (evaluation / integration direction)
  - LLMs
  - Semantic Documentation
role: semantic-layer and analytics architecture lead
visibility_level: customer-facing teams, Product and business leadership
status: semantic foundation, SQL Lab assistant and AI text-to-SQL implemented; continuous improvement ongoing
---

## Quick Answer

I helped establish a semantic documentation layer that makes Skan's analytical datasets, business metrics, SQL logic and use cases easier for non-data teams to understand and use. This foundation now supports a custom SQL Lab widget with categorized FAQs, verified SQL that can be inserted into the editor, and an AI agent that converts plain-English questions into SQL grounded in the semantic layer. The implementation also records questions, model responses, latency and token consumption to support quality evaluation, cost optimization, traceability and continuous improvement.

## What Business Problem Did the Project Solve?

Skan's analytical data contains domain-specific concepts, process-mining entities, metric definitions and aggregation rules. Even when data is available, customer-facing teams and non-data analysts may not know:

- Which dataset should answer a business question.
- What a metric means and at what grain it is calculated.
- Which filters or joins are valid.
- Which SQL pattern represents the approved business definition.
- How to interpret the output correctly.

Without shared semantic definitions, users depend on analysts for routine questions and may produce inconsistent SQL or conflicting metric interpretations.

## What Was the Objective?

1. Make analytical knowledge accessible beyond the data team.
2. Document business metrics, dataset grain, SQL definitions and analytical use cases.
3. Enable AI-assisted SQL generation grounded in documented semantics.
4. Improve consistency across BI dashboards and ad hoc analysis.
5. Create a foundation for natural-language analytics and more flexible question answering.

## What Did I Own or Contribute?

- Structured semantic documentation around datasets, metrics, definitions and use cases.
- Documented warehouse SQL, granularity, relationships and business context.
- Helped establish metadata conventions that can be consumed by an AI assistant.
- Supported the semantic-layer rollout for everyday analytics.
- Designed the categorized FAQ and verified-SQL experience within a custom Superset SQL Lab widget.
- Enabled users to insert approved queries directly into the SQL editor.
- Integrated plain-English-to-SQL assistance grounded in semantic documentation.
- Designed logging for user questions, AI responses, generated SQL, timestamps, latency and token usage.
- Established an evaluation loop for improving response quality, performance, cost and traceability.
- Prepared the value proposition and demonstration narrative for business leadership.

## How Does the Semantic-Assisted Workflow Work?

1. A user opens the custom assistant from Superset SQL Lab.
2. The user either browses categories and subcategories to select a known FAQ or asks a question in plain English.
3. For a known FAQ, the widget retrieves reviewed SQL and inserts it directly into the SQL editor.
4. For a new question, the AI agent uses semantic documentation to identify the relevant business terms, datasets, grain, relationships and metric definitions.
5. The model returns a SQL query for review in the SQL Lab workflow.
6. The framework records the question, response, generated SQL, timestamps, latency, token consumption and traceability metadata.
7. The collected evidence supports continuous improvement of the semantic layer, prompts, verified-query library, model performance and cost.

## What Is Implemented Versus Evolving?

### Established foundation

- Semantic documentation for everyday analytics.
- Business definitions, SQL examples, metadata and dataset-use-case descriptions.
- A custom Superset SQL Lab widget with categories, subcategories and verified SQL.
- Direct insertion of approved SQL into the editor.
- Semantic-layer-grounded AI generation of SQL from plain-English questions.
- Logging of questions, responses, latency and token consumption.
- A customer-facing and non-data-user workflow for obtaining SQL assistance without prior data-model knowledge.

### Evolving / next-stage direction

- Improved grounding, validation and feedback loops for generated SQL.
- Broader automated evaluation of SQL correctness and semantic adherence.
- Expansion of FAQ coverage based on observed user questions.
- Continued model, latency and token-cost optimization.
- More advanced retrieval and orchestration patterns as the semantic corpus grows.

## Important Architecture Decisions and Trade-offs

### Ground SQL generation in business semantics

A language model may generate syntactically valid SQL that is still semantically incorrect. Metric definitions, table grain, join rules and approved query patterns provide grounding that generic prompting cannot replace.

### Separate knowledge from application code

Semantic documents need an ownership and versioning model. Keeping knowledge external to application code can simplify updates, but requires reliable retrieval, access control and version compatibility. Packaging documents into an application image may simplify deployment but can make content updates dependent on image releases.

### Start with known questions, then expand

A FAQ/playbook foundation provides a controlled starting point. RAG can broaden question coverage, but increases the need for retrieval evaluation, SQL validation and safe execution controls.

### Treat generated SQL as a governed artifact

The assistant should operate within user permissions, approved datasets and query limits. Generated SQL should not bypass the same data-access controls used by ordinary analytics users.

## What Was the Outcome?

- Established a semantic documentation foundation for everyday analytics.
- Enabled categorized FAQs and direct reuse of verified SQL in Superset SQL Lab.
- Enabled semantic-layer-grounded AI text-to-SQL for customer-facing and non-data teams.
- Improved discoverability of business definitions, SQL patterns and dataset context.
- Reduced the need to understand the underlying data model before starting an analysis.
- Established interaction-level traceability and telemetry for AI quality, latency, token usage and cost optimization.
- Connected data warehouse documentation with the AI analytics roadmap.

## What Artifacts Were Produced?

- Semantic documentation and metadata definitions.
- Business metric and KPI descriptions.
- Dataset-grain and relationship documentation.
- SQL examples and approved analytical query patterns.
- SQL Lab FAQ categories, subcategories and verified-query content.
- Custom query-insertion and AI text-to-SQL workflow.
- Interaction logging and evaluation framework.
- Leadership demonstration and value-proposition materials.

## What Would I Measure Next?

- Number of metrics and datasets covered by semantic documentation.
- Percentage of common analytical questions supported.
- SQL generation execution success rate.
- Semantic correctness, not just SQL syntax validity.
- Response latency.
- Input and output token consumption.
- Estimated cost per interaction and use case.
- Traceability and recurring failure patterns.
- User adoption and reduction in routine analyst requests.
- Percentage of AI questions converted into verified FAQ content.

## What Did I Learn?

- AI-assisted analytics depends heavily on the quality of the underlying semantic model.
- Business definitions and data grain are essential context for SQL generation.
- RAG is useful only when retrieval quality and source governance are strong.
- SQL correctness and business correctness are separate evaluation problems.
- A gradual rollout from known use cases to flexible natural-language analytics reduces risk.

## Frequently Asked Questions

### Is this a generic chatbot?

No. The intention is to ground analytics assistance in Skan's business definitions, semantic documentation, datasets and SQL patterns.

### What does the semantic layer contain?

Business metrics, KPI definitions, dataset granularity, relationships, SQL examples and use-case documentation.

### Is AI-assisted SQL implemented?

Yes. Users can ask questions in plain English and receive SQL generated using semantic-layer documentation as grounding context. Broader retrieval and orchestration enhancements remain part of continuous improvement.

### Why is semantic documentation important for AI?

It provides the business meaning and data constraints needed to generate queries that are not merely syntactically valid but also aligned with approved analytical definitions.
