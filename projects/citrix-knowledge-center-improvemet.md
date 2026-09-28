---
type: project
name: Knowledge Center Governance and Self-Service Content Improvement
timeframe: 1.5 years
organization: Citrix
project_type: internal
domains:
  - Knowledge Management
  - Content Governance
  - Support Analytics
  - Self-Service Support
tools:
  - Salesforce
  - SQL Server
role: owner
visibility_level: org
status: completed
---

## Quick Answer

At Citrix, I led the data and analytics work for a 1.5-year program to improve a knowledge library containing more than 35,000 internal and public articles. I developed rules for identifying stale or incomplete content, used historical support-case associations to improve article tagging, and built a dashboard to monitor review progress. The program archived approximately 10,000 low-value articles and categorized about 7,000 articles for easier reuse and discovery.

## What Business Problem Did the Project Solve?

Citrix maintained more than 35,000 knowledge assets, including product documentation, root-cause analyses, release notes, known issues, and support procedures. The library contained a mixture of public and internal-only content.

Over time, the library accumulated duplicate, blank, incomplete, outdated, and poorly categorized articles. Support teams struggled to determine:

- Which articles were still relevant to current product versions.
- Which content should remain internal or could be published.
- Which articles should be updated, merged, or archived.
- How articles should be categorized by product and issue type.
- Whether engineers were reusing existing knowledge when resolving similar cases.

Poor knowledge quality increased search effort, encouraged teams to recreate troubleshooting steps, and limited opportunities for customers to resolve known issues through self-service.

## What Were the Objectives?

The program aimed to:

1. Identify outdated articles associated with unsupported or older product versions.
2. Detect blank, incomplete, duplicate, or low-value content.
3. Categorize articles by product line and technical issue.
4. Encourage engineers to update or create knowledge while resolving cases.
5. Identify content that could be safely published for customer self-service.
6. Establish a measurable, continuous content-review process.

## What Did I Own?

I owned the technical and data work for the program:

- Extracted article metadata and support-case associations from Salesforce.
- Moved relevant data into SQL Server for analysis and repeatable querying.
- Defined data rules for archival and deprecation candidates.
- Identified blank, incomplete, stale, and low-usage articles.
- Designed a tagging approach based on historical article-to-case usage.
- Built a dashboard to monitor article review and improvement by product, team, and product version.
- Worked with Knowledge Center, Technical Support, and Engineering teams throughout the improvement program.

Content owners and technical teams made the final decisions to update, publish, or archive individual articles.

## What Data Was Used?

The analysis combined:

- Knowledge article metadata from Salesforce.
- Public versus internal visibility status.
- Product and product-version associations.
- Article creation and update dates.
- Historical links between support cases and knowledge articles.
- Technical issue types associated with those cases.
- Article completeness and usage indicators.

## How Did the Content-Governance Process Work?

The workflow was:

1. Extract article and case metadata from Salesforce.
2. Load the relevant data into SQL Server.
3. Profile the library for missing, stale, incomplete, and low-value content.
4. Flag archival and deprecation candidates using agreed rules.
5. Analyze historical article-to-case associations.
6. Assign primary and secondary product and issue tags based on usage patterns.
7. Route flagged articles to the appropriate technical owners for review.
8. Track review, update, publication, and archival progress through a dashboard.

## How Were Articles Categorized?

An article could be linked to multiple technical issue types. Instead of relying only on manually entered labels, I used historical support-case associations to identify the issue categories most frequently connected with each article.

High-frequency associations informed the primary category, while other relevant associations could be retained as secondary tags. This made the taxonomy more representative of how support teams actually used the content.

## What Decisions and Trade-offs Were Important?

### Use evidence to prioritize review

The team could not manually inspect more than 35,000 articles at once. Metadata, content completeness, product relevance, and historical usage were used to prioritize human review.

### Keep publication decisions human-controlled

Data rules identified potential public or archival candidates, but technical owners retained responsibility for checking accuracy, confidentiality, and product relevance before publication.

### Favor continuous governance over one-time cleanup

The program included monitoring and ownership workflows so that the library would not immediately return to its previous state.

### Use historical behavior to improve taxonomy

Case associations provided a scalable tagging signal, but historical usage could reinforce existing classification errors. Technical review remained necessary for ambiguous articles.

## What Was the Business Outcome?

- Reviewed and governed a library of more than 35,000 knowledge assets.
- Archived approximately 10,000 articles containing outdated, incomplete, or low-value information.
- Categorized approximately 7,000 articles using historical support usage.
- Established visibility into review progress by product, team, and product version.
- Improved the reuse of existing troubleshooting knowledge across support and engineering teams.
- Created a cleaner content foundation for public self-service and chatbot-based knowledge discovery.

The improved knowledge foundation contributed to broader self-service and chat-support initiatives. It should not be interpreted as the sole cause of changes in support-channel adoption or case volume.

## How Did This Support Later AI and Chatbot Initiatives?

Large language models and search systems depend on current, well-structured, accurately classified source content. The cleanup and taxonomy work reduced stale material and improved the organization of the knowledge corpus.

This made the library better suited for later chatbot and LLM-based retrieval initiatives. Those integrations were subsequent uses of the improved content foundation rather than the original scope of this analytics project.

## What Artifacts Were Produced?

- Article metadata and usage dataset in SQL Server.
- Archival and deprecation candidate rules.
- Product and issue-type tagging logic.
- Dashboard for monitoring review and remediation progress.
- Prioritized worklists for content and technical owners.

The underlying knowledge content, support-case data, dashboards, and internal governance rules are confidential and are not published publicly.

## What Would I Measure in a Future Version?

The retained project record does not include a directly attributable case-deflection or cost-reduction percentage. A future implementation should track:

- Search success and zero-result search rate.
- Article reuse during case resolution.
- Article helpfulness and customer feedback.
- Self-service case-deflection rate.
- Time to resolution with and without linked knowledge.
- Percentage of content reviewed within its governance schedule.
- Retrieval precision for chatbot or LLM responses.

## What Did I Learn?

- Content volume is not the same as knowledge quality.
- Automated rules are effective for prioritization, but domain experts must make final content decisions.
- Historical usage provides valuable taxonomy signals when manually entered metadata is inconsistent.
- Knowledge governance must have owners, review cycles, and monitoring to remain effective.
- AI-based retrieval cannot compensate for stale, incomplete, or poorly classified source content.

## Frequently Asked Questions

### How large was the knowledge library?

It contained more than 35,000 internal and public knowledge assets.

### How many articles were archived?

Approximately 10,000 outdated, incomplete, or low-value articles were archived.

### How many articles were categorized?

Approximately 7,000 articles were tagged using their historical associations with support cases.

### Which systems were used?

Salesforce supplied knowledge and support-case metadata, and SQL Server supported analysis, tagging, and repeatable queries.

### Did the project use an LLM?

No. The original project focused on content governance, cleanup, classification, and monitoring. The improved content foundation later supported chatbot and LLM-based knowledge-retrieval initiatives.

### Did the project reduce support cases?

The work was designed to strengthen self-service and reduce avoidable support demand, but the retained project record does not contain a directly attributable case-deflection percentage.
