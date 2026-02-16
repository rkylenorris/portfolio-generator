Title: ReportForge
Date: 2026-02-10T12:00:00Z
Category: Projects
Stack: C#, PowerShell, SQL Server, ClosedXML
Project_Status: 1.0 (16% Complete)
Summary: A production-grade reporting orchestration tool bridging .NET 10 and PowerShell.
Authors: R. Kyle Norris
Summary: Project Highlight: ReportForge
Sort_order: 2

### Project Status: 16% Complete

<progress max="100" value="16"></progress>

#### Engineering Roadmap



##### System Architecture


✅ **Directory Structure Setup**: Establish strict separation between source code and build artifacts.

✅ **Technology Stack Initialization**: Initialize .NET 10 solution and PowerShell 7+ orchestration layer.



##### Functional Requirements


⏳ **Public Command Interface**: Develop core cmdlets: Invoke-ReportForgeRun, Test-ReportForgeConfig, and developer utility commands.

⏳ **Configuration & Secrets System**: Implement YAML-based config parsing with ${VAR_NAME} environment interpolation.

⚪ **SQL Ingestion Pipeline**: Execute SQL queries and capture row counts and execution metrics.

⚪ **Excel Engine (ClosedXML)**: Map DataTables to Excel anchors while preserving formulas/styles.

⚪ **Parquet Export Engine**: Implement Parquet.Net for stable schema exports to Power BI.

⚪ **Artifact Generation**: Automatic generation of manifest.json and data_dictionary.csv.



##### Technical Implementation


⏳ **C# DTO Contract**: Define RawConfig and ResolvedConfig classes for clean interop.

⚪ **Build System (build.ps1)**: Automation of dotnet build, DLL copying, and manifest updates.



##### Release Criteria


⚪ **Unit & Integration Testing**: Achieve validation through Pester and .NET testing suites[cite: 6].

⚪ **CI/CD Pipeline**: Establish GitHub Actions for automated testing and publishing[cite: 6].



### Project Overview

ReportForge is designed to generate repeatable, production-grade business reports. It orchestrates SQL execution, populates Excel templates using **ClosedXML**, and exports **Parquet** datasets.

#### System Design

The project follows a strict separation of concerns to ensure CI/CD compatibility:

* **Root Module:** `ReportForge.psd1` handles the manifest and loading.
* **Src/DotNet:** Contains the C# solution for Core, Excel, and Parquet logic.
* **Src/PowerShell:** Contains the public cmdlets like `Invoke-ReportForgeRun`.