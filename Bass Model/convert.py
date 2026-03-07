import os
from markdown_pdf import MarkdownPdf, Section

base_dir = os.path.dirname(os.path.abspath(__file__))

md_path = os.path.join(base_dir, "report", "report.md")
pdf_path = os.path.join(base_dir, "report", "report.pdf")

pdf = MarkdownPdf()

with open(md_path, encoding="utf-8") as f:
    content = f.read()

pdf.add_section(Section(content))
pdf.save(pdf_path)