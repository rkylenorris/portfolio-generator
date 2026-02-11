# Build-Site.ps1

# 1. Run the Python Pre-processor
# This fetches the JSON from GitHub and updates your Markdown templates
Write-Host "--- Fetching Remote Data & Injecting Templates ---" -ForegroundColor Cyan
uv run main.py

# 2. Run Pelican to generate the static HTML
# This takes your /content folder and /theme and outputs to /output
Write-Host "--- Generating Static HTML with Pelican ---" -ForegroundColor Yellow
$ErrorActionPreference = "Stop"
pelican content -o output -s pelicanconf.py
# TODO: Fix navigation issue with Pelican           

Write-Host "--- Build Complete! Check the /output folder ---" -ForegroundColor Green