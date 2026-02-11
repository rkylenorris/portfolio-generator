import json
import os
from datetime import datetime
from urllib.request import urlopen
from jinja2 import Template
from pathlib import Path


def get_report_forge_json() -> dict | None:
    RAW_JSON_URL = "https://raw.githubusercontent.com/rkylenorris/ReportForge/main/reportforge_status.json"
    try:
        with urlopen(RAW_JSON_URL) as response:
            if response.getcode() == 200:
                data = json.loads(response.read().decode("utf-8"))
                return data
            else:
                raise Exception(f"Failed to fetch data: {response.getcode()}")
    except Exception as e:
        print(f"Error fetching JSON data: {e}")
        return None


def generate_report_forge_page():
    # 1. Load the JSON data
    data = get_report_forge_json()
    if not data:
        print("No data to process. Exiting.")
        return

    # 2. Calculate Progress
    all_steps = [step for section in data['sections']
                 for step in section['steps']]
    total_steps = len(all_steps)
    completed_steps = len([s for s in all_steps if s['status'] == 'Complete'])
    progress_pct = int((completed_steps / total_steps)
                       * 100) if total_steps > 0 else 0

    # 3. Sort Sections
    sections = sorted(data['sections'], key=lambda x: x['order'])

    # 3. Read the Template File
    template_path = Path('templates/report_forge_template.md')
    if not template_path.exists():
        raise FileNotFoundError(f"Template file not found: {template_path}")

    with template_path.open('rb') as f:
        template_content = f.read()

    # 4. Render with Jinja2
    template = Template(template_content.decode('utf-8'))
    rendered_md = template.render(
        last_updated=data['last_updated'],
        version=data['version'],
        stack="C#, PowerShell, SQL Server, ClosedXML",
        summary="A production-grade reporting orchestration tool bridging .NET 10 and PowerShell.",
        progress_pct=progress_pct,
        sections=sections
    )

    # 5. Save to Content
    save_as_path = Path('content/pages/report_forge.md')
    if save_as_path.exists():
        os.remove(save_as_path)
    with save_as_path.open('wb') as f:
        f.write(rendered_md.encode('utf-8'))

    print(
        f"Successfully injected {progress_pct}% progress into report_forge.md")


if __name__ == "__main__":
    generate_report_forge_page()
