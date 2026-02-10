Title: ReportForge
Date: 2026-02-09
Category: Projects
Stack: C#, PowerShell, SQL Server, ClosedXML
Status: In-Progress
Summary: A production-grade reporting orchestration tool bridging .NET 10 and PowerShell.

## Project Overview

[cite_start]ReportForge is designed to generate repeatable, production-grade business reports[cite: 1]. [cite_start]It orchestrates SQL execution, populates Excel templates using **ClosedXML**, and exports **Parquet** datasets[cite: 1].

### Key Engineering Highlights

* **High-Performance Core:** Built with a C# (.NET 10) backend for performance-critical logic.
* **Fail-Fast Architecture:** Configuration and schema errors stop execution before data is written.
* **Security:** Employs environment variable interpolation (`${VAR_NAME}`) to ensure secrets never touch the disk in plain text.
* **Strict Tooling:** Uses a custom build system (`build.ps1`) to compile DLLs and package the PowerShell module.
