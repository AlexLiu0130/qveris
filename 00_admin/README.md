# QVeris AI Stock Product Workspace

This workspace is for daily work tracking, product research, requirements, analysis, and deliverables related to QVeris US stock AI products.

## Folder Map

### 00_admin
Workspace rules, templates, naming conventions, and process notes.

### 01_daily
Daily work logs. One file per working day.

Naming:

```text
YYYY-MM-DD.md
```

Suggested path:

```text
01_daily/YYYY/MM/YYYY-MM-DD.md
```

### 02_meetings
Meeting notes, interview notes, internal sync notes, and follow-up action items.

Naming:

```text
YYYY-MM-DD_topic.md
```

### 03_research
Research materials and notes.

- `market`: US stock market, AI investing products, users, trends
- `company`: QVeris company, product, capabilities, pricing, positioning
- `competitors`: competitors, substitutes, benchmark products

### 04_product
Product work artifacts.

- `requirements`: raw requirements, user stories, problem statements
- `prd`: formal PRDs and product specs
- `roadmap`: milestones, release plans, prioritization

### 05_data
Data-related work.

- `inputs`: original data files or exported source files
- `analysis`: analysis notes, notebooks, SQL, scripts
- `outputs`: charts, tables, cleaned results, summaries

### 06_deliverables
Final or shareable outputs, such as reports, presentations, product briefs, and stakeholder-ready docs.

### 07_archive
Old, replaced, or inactive files. Move files here instead of deleting them when the history may matter.

## Daily Work Rule

Every workday should have one daily log covering:

1. What was done
2. Key decisions
3. Important findings
4. Files created or updated
5. Open questions
6. Tomorrow's priorities

The daily log is the source of truth for daily work traceability.

## Research Deliverable Visual Standard

Important research deliverables should include visual summary assets by default, especially when the topic involves data categories, capability coverage, product architecture, workflows, or prioritization.

For QVeris US stock AI product research, each major report should include at least one of the following:

1. Capability landscape matrix
2. Data-to-product workflow map
3. Layered ecosystem / universe diagram
4. Priority roadmap visual

Visuals should follow these standards:

- Use a clean white background, restrained lines, and high information density.
- Include Chinese primary labels and short English secondary labels where useful.
- Use consistent status colors:
  - Green: publicly confirmed / available
  - Blue: partially confirmed
  - Gray: pending Inspect / unknown
  - Gold: public gap / missing in public materials
- Show not only data fields, but also trust infrastructure, data quality, provider coverage, and Agent workflow usage.
- Avoid purely decorative charts. Every visual should help readers understand structure, priority, coverage, or next action.
- Store reusable visual assets under `05_data/outputs/visuals`.
- Insert final visuals into stakeholder-facing reports in `06_deliverables`.

## Naming Rules

Use lowercase English for folders and stable filenames where possible.

Use dates for time-sensitive files:

```text
YYYY-MM-DD_topic.md
```

Use version suffixes for formal deliverables:

```text
topic_v0.1.md
topic_v1.0.md
```

Avoid ambiguous names such as:

```text
final.md
new.md
temp.md
copy.md
```

## File Status Tags

Use these tags near the top of important documents:

```text
Status: Draft
Status: In Review
Status: Final
Status: Archived
```
