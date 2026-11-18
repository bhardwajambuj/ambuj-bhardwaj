---
type: project
name: PBI Doctor – Power BI Metadata and Documentation Utility
timeframe: 2025–present (confirm initial build date)
organization: Skan AI
project_type: internal developer productivity tool
domains:
  - Power BI Engineering
  - Metadata Extraction
  - DAX Dependency Analysis
  - Technical Documentation
  - Developer Productivity
tools:
  - Python
  - PyQt5
  - PBIP
  - TMDL
  - Power BI report JSON
  - DAX
  - Power Query (M)
  - Excel
role: independent builder / product owner
visibility_level: BI team and company-wide town hall
status: built; used to support documentation and analysis
---

## Quick Answer

I independently built PBI Doctor, a Python-based desktop application for Windows that analyzes Power BI project files and generates technical documentation. The tool reads PBIP project structures, report JSON and TMDL metadata to extract tables, columns, measures, calculated columns, relationships and Power Query definitions. It also analyzes DAX dependencies and identifies where model objects are referenced across measures, relationships and report visuals. The application helped standardize documentation of customer and internal dashboards, support handovers and identify opportunities to simplify models. I presented the tool and its use cases at a company-wide town hall.

## What Business Problem Did the Project Solve?

Power BI models can become difficult to maintain as reports accumulate measures, calculated columns, relationships and visual dependencies. Technical documentation is often incomplete or becomes outdated as the model changes.

This creates several recurring problems:

- Engineers need to inspect project files manually to understand the model.
- Dependencies between measures, columns and tables are difficult to trace.
- Unused or redundant fields increase model complexity.
- Knowledge transfer depends heavily on the original report developer.
- Documentation takes time and is often inconsistent across reports.

## What Was the Objective?

1. Automate extraction of Power BI project metadata.
2. Produce a structured technical inventory of model objects.
3. Identify DAX dependencies and object usage.
4. Help distinguish regular and calculated tables and columns.
5. Generate documentation that can be shared with BI developers and report owners.
6. Support model optimization, handover and change-impact analysis.

## What Did I Own?

- Defined the application workflow and metadata inventory.
- Built the desktop GUI using Python and PyQt5.
- Implemented parsing of PBIP project structure, report JSON and TMDL files.
- Extracted table, column, measure, calculated-column and relationship metadata.
- Captured Power Query/M definitions and DAX expressions.
- Developed dependency parsing to identify references between model objects.
- Analyzed object usage across DAX, relationships and report visuals.
- Built export functionality for technical documentation and Excel-based analysis.
- Demonstrated the application and its organizational use cases in a company-wide town hall.

## How Did the Application Work?

1. The user selects a Power BI project folder.
2. The application reads the PBIP project structure and relevant report/model metadata files.
3. It parses TMDL and report JSON definitions.
4. It classifies model objects, including regular and calculated tables/columns.
5. It extracts DAX measures, calculated columns, relationships and Power Query definitions.
6. It analyzes dependencies and usage references.
7. It presents the metadata through the GUI and exports structured documentation to Excel.

## Important Design Decisions and Trade-offs

### Analyze project files rather than require a live Power BI connection

Reading project artifacts made the utility useful for offline review and repeatable documentation. The trade-off is that supported file formats and metadata structures must be kept compatible with evolving Power BI project conventions.

### Distinguish metadata extraction from semantic interpretation

The tool can identify expressions and references, but a dependency does not automatically prove that a model object is unnecessary. Recommendations to remove fields still require developer review and regression testing.

### Provide both a GUI and exportable output

The GUI supports interactive inspection, while Excel exports make the output easier to review, share and incorporate into existing documentation processes.

## What Was the Outcome?

- Created a repeatable way to generate technical inventories for Power BI projects.
- Improved documentation and handover for standard and customer-specific dashboards.
- Helped identify unused or weakly used model objects for potential simplification.
- Reduced reliance on manual inspection of large Power BI models.
- Demonstrated an internally developed engineering solution to the wider organization through a town hall presentation.

The exact number of projects analyzed, hours saved and models simplified has not been quantified in the retained project record.

## What Artifacts Were Produced?

- Windows desktop application built with Python and PyQt5.
- PBIP/TMDL/report JSON parsing workflow.
- Metadata inventory for model tables, columns, measures and relationships.
- DAX expression and dependency analysis.
- Excel documentation exports.
- Internal usage and demonstration material.

The tool and customer project metadata may contain proprietary information and should not be distributed externally without approval.

## What Would I Improve Next?

- Add compatibility tests for newer PBIP/TMDL structures.
- Improve DAX parsing for complex expressions and edge cases.
- Add visual-level lineage and impact analysis.
- Compare metadata snapshots to identify model changes between releases.
- Add automated detection of unused fields with confidence levels.
- Generate a standardized documentation pack for architecture reviews and release handovers.
- Track time saved and number of models analyzed.

## What Did I Learn?

- Internal developer tools can remove recurring operational friction and improve engineering consistency.
- Metadata extraction and dependency analysis are powerful foundations for BI governance.
- Static analysis should inform human decisions, not automatically delete model objects.
- A useful engineering tool needs both a practical workflow and outputs that fit existing team processes.

## Frequently Asked Questions

### What formats did the tool analyze?

PBIP project structures, report JSON and TMDL metadata.

### What information did it extract?

Tables, columns, measures, calculated columns, relationships, Power Query definitions, DAX expressions and usage/dependency information.

### Did it automatically remove unused columns or measures?

No. It helped identify potential unused objects; removal required developer validation.

### Who benefited from the tool?

BI developers and report owners responsible for documenting, maintaining and optimizing standard and customer-specific Power BI dashboards.
