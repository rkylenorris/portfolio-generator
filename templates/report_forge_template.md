Title: ReportForge
Date: {{ last_updated }}
Category: Projects
Stack: {{ stack }}
Project_Status: {{ version }} ({{ progress_pct }}% Complete)
Summary: {{ summary }}
Authors: R. Kyle Norris
Summary: Project Highlight: ReportForge
Sort_order: 2

### Project Status: {{ progress_pct }}% Complete

#### Engineering Roadmap
{% for section in sections %}
##### {{ section.name }}
{% for step in section.steps %}
{% if step.status == "Complete" %}✅{% elif step.status == "InProgress" %}⏳{% else %}⚪{% endif %} **{{ step.name }}**: {{ step.description }}
{% endfor %}
{% endfor %}
### Project Overview

ReportForge is designed to generate repeatable, production-grade business reports. It orchestrates SQL execution, populates Excel templates using **ClosedXML**, and exports **Parquet** datasets.

#### System Design

The project follows a strict separation of concerns to ensure CI/CD compatibility:

* **Root Module:** `ReportForge.psd1` handles the manifest and loading.
* **Src/DotNet:** Contains the C# solution for Core, Excel, and Parquet logic.
* **Src/PowerShell:** Contains the public cmdlets like `Invoke-ReportForgeRun`.
