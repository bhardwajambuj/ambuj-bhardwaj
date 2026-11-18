---
type: project
name: VBA-Based Search Engine for Aircraft Manufacturing Documents
timeframe: 2 months
organization: TCS
project_type: internal
domains:
  - Aerospace
  - Manufacturing Quality
  - Information Retrieval
  - Process Automation
tools:
  - Excel
  - VBA
  - Term-Frequency Indexing
role: owner
visibility_level: team
status: completed
---

## Quick Answer

At TCS, I built a document search engine entirely in Excel and VBA for an eight-person aerospace team working across 118 aircraft-manufacturing files. The utility indexed historical documents, ranked the 3–5 most relevant results for a user's query, opened the selected workbook, and highlighted matching terms. It replaced a manual process that required opening 5–8 files and was estimated to save up to 32 minutes per search.

## What Business Problem Did the Project Solve?

The team created and maintained aircraft-engine assembly and quality documents, including assembly control plans and Process Failure Mode and Effects Analysis (PFMEA) records.

To prepare a new or revised document, engineers needed to reference earlier releases and related assembly records. The source material was distributed across 118 Excel files covering more than five document variants.

Users had no centralized search capability. They manually opened files one by one, searched for relevant terms, and compared prior content. A typical query required reviewing 5–8 workbooks, making the process slow and inconsistent.

## What Was the Objective?

The objective was to create a single search interface that would:

1. Find relevant information across historical Excel documents.
2. Rank the best-matching files instead of returning an unfiltered list.
3. Open the selected source document directly.
4. Highlight matching terms so users could locate evidence quickly.
5. Operate within the team's existing Excel-and-VBA environment.

## What Constraints Shaped the Solution?

The team worked in a restricted technology environment where Excel and VBA were the available implementation tools. Introducing a separate search platform, Python service, or database-backed application was not practical.

The solution therefore needed to:

- Run locally in Microsoft Excel.
- Search existing workbooks without changing their source format.
- Remain understandable and maintainable by the team.
- Avoid requiring new infrastructure or software installation.

## What Did I Own?

I worked directly with the engineering team in an embedded, consultative role similar to a Forward Deployed Engineer:

- Observed the document-authoring and reference workflow.
- Identified the repeated manual-search bottleneck.
- Designed the indexing and retrieval approach.
- Built the VBA application end to end.
- Created the result-ranking and document-linking workflow.
- Implemented term highlighting in the selected workbook.
- Delivered the utility within the team's existing operating environment.

## How Did the Search Engine Work?

The application used a term-frequency-based information-retrieval workflow:

1. Read and parse content from the historical Excel workbooks.
2. Create a searchable index of documents and terms.
3. Build a term-frequency matrix representing term usage by document.
4. Convert a user's query into a comparable search representation.
5. Calculate similarity between the query and indexed documents.
6. Return the 3–5 highest-ranked results.
7. Provide a hyperlink to open each source workbook.
8. Highlight cells containing query terms in the selected document.

The result score represented search relevance, not a statistical probability that the document was correct.

## Why Pre-Index the Documents?

Searching all 118 workbooks during every query would have repeated the most expensive processing step and produced a poor user experience. Creating an index allowed the utility to compare a query against a prepared representation of the document collection.

This design reduced repeated file scanning and made ranked retrieval practical within VBA.

## What Decisions and Trade-offs Were Important?

### Use lexical matching instead of a complex language model

Term-frequency matching was feasible in VBA, explainable to users, and compatible with the available environment. It did not require external libraries or services.

The trade-off was that lexical search could miss synonyms, abbreviations, and conceptually related phrases that did not share the same terms.

### Return a small ranked result set

Returning only the top 3–5 documents reduced the review burden while still allowing users to compare multiple likely sources.

### Preserve the source-document workflow

The application linked directly to the original workbook rather than copying content into a new system. This maintained traceability to the controlled source document.

### Highlight query terms

Opening the correct file was not sufficient if users still needed to scan every sheet and cell. Highlighting matching terms directed attention to likely relevant passages.

## What Was the Outcome?

- Replaced manual searches across 118 files with one VBA-enabled Excel utility.
- Reduced the typical review set from 5–8 manually opened files to 3–5 ranked results.
- Provided direct links to source workbooks.
- Highlighted matching cells within the selected document.
- Supported an eight-person aircraft-documentation team.
- Was estimated to save up to 32 minutes per query when compared with opening and reviewing eight files manually.

The time-saving estimate used an observed average of approximately four minutes per manually reviewed file. It was a productivity estimate rather than a controlled time-and-motion study.

## What Artifacts Were Produced?

- VBA-enabled Excel search application.
- Parsed document and term index.
- Term-frequency matrix.
- Ranked search-results interface.
- Hyperlinks to source workbooks.
- Query-term highlighting workflow.

The source documents and VBA application contain internal aerospace-process information and are not publicly available.

## What Were the Technical Limitations?

- Search quality depended on exact or closely related terms.
- Synonyms and domain abbreviations required shared vocabulary to match reliably.
- The index needed to be refreshed when source documents changed.
- Ranking quality was not evaluated with a labeled relevance test set.
- Excel and VBA constrained performance and maintainability as the document collection grew.

## What Would I Improve Today?

For a modern implementation, I would:

- Add domain-specific synonym and abbreviation dictionaries.
- Track click-through and selected-result behavior.
- Evaluate ranking using precision at K and mean reciprocal rank.
- Add incremental indexing for changed documents.
- Compare lexical retrieval with semantic embeddings.
- Preserve source citations and access controls in any AI-assisted search experience.

## What Did I Learn?

- Understanding the user's workflow was more important than selecting a fashionable technology.
- A constrained toolset can still support useful information retrieval when the indexing model is kept simple.
- Ranked results are more useful than an exhaustive list when users need to act quickly.
- Search tools must preserve traceability to controlled source documents in quality-sensitive environments.
- Productivity claims should be documented with repeatable measurement methods.

## Frequently Asked Questions

### Was this a generative AI application?

No. It was a term-frequency-based document search and ranking application built in Excel and VBA. It used information-retrieval concepts associated with natural language processing but did not generate content.

### How many files did it search?

The indexed collection contained 118 Excel files covering more than five document variants.

### What did the user receive for each query?

The utility returned the 3–5 highest-ranked documents with links to the source files. When a document was opened, cells containing query terms were highlighted.

### Why was the solution built in VBA?

Excel and VBA were the tools available in the team's restricted environment. The application therefore worked within the existing workflow without requiring additional infrastructure.

### How much time did it save?

The estimated saving was up to 32 minutes per query when compared with manually opening and reviewing eight files at approximately four minutes per file.