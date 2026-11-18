#!/usr/bin/env python3
"""Generate ATS-friendly DOCX and print-ready HTML files from resume Markdown."""

from __future__ import annotations

import html
import re
from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor


ROOT = Path(__file__).resolve().parents[1]
RESUME_DIR = ROOT / "resumes"
SOURCES = (
    "ambuj-bhardwaj-analytics-platform-architect.md",
    "ambuj-bhardwaj-senior-analytics-manager.md",
)

NAVY = "17365D"
SLATE = "44546A"
BLACK = "1F1F1F"


def parse_markdown(path: Path) -> list[tuple[str, str]]:
    blocks: list[tuple[str, str]] = []
    paragraph: list[str] = []

    def flush_paragraph() -> None:
        if paragraph:
            blocks.append(("paragraph", " ".join(paragraph)))
            paragraph.clear()

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line:
            flush_paragraph()
        elif line.startswith("### "):
            flush_paragraph()
            blocks.append(("role", line[4:]))
        elif line.startswith("## "):
            flush_paragraph()
            blocks.append(("h2", line[3:]))
        elif line.startswith("# "):
            flush_paragraph()
            blocks.append(("name", line[2:]))
        elif line.startswith("- "):
            flush_paragraph()
            blocks.append(("bullet", line[2:]))
        else:
            paragraph.append(line)
    flush_paragraph()
    return blocks


def set_cell_free_border(paragraph, color: str = NAVY) -> None:
    p_pr = paragraph._p.get_or_add_pPr()
    p_bdr = p_pr.find(qn("w:pBdr"))
    if p_bdr is None:
        p_bdr = OxmlElement("w:pBdr")
        p_pr.append(p_bdr)
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "8")
    bottom.set(qn("w:space"), "2")
    bottom.set(qn("w:color"), color)
    p_bdr.append(bottom)


def set_run_font(run, size: float, bold: bool = False, italic: bool = False, color: str = BLACK) -> None:
    run.font.name = "Arial"
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = RGBColor.from_string(color)
    run._element.rPr.rFonts.set(qn("w:eastAsia"), "Arial")


def add_inline_runs(paragraph, text: str, size: float = 9.0) -> None:
    pieces = re.split(r"(\*\*.*?\*\*)", text)
    for piece in pieces:
        if not piece:
            continue
        bold = piece.startswith("**") and piece.endswith("**")
        value = piece[2:-2] if bold else piece
        set_run_font(paragraph.add_run(value), size=size, bold=bold)


def configure_document(document: Document, title: str) -> None:
    section = document.sections[0]
    section.page_width = Inches(8.27)
    section.page_height = Inches(11.69)
    section.top_margin = Inches(0.48)
    section.bottom_margin = Inches(0.48)
    section.left_margin = Inches(0.58)
    section.right_margin = Inches(0.58)
    section.header_distance = Inches(0.2)
    section.footer_distance = Inches(0.2)

    normal = document.styles["Normal"]
    normal.font.name = "Arial"
    normal.font.size = Pt(9)
    normal.font.color.rgb = RGBColor.from_string(BLACK)
    normal._element.rPr.rFonts.set(qn("w:eastAsia"), "Arial")
    normal.paragraph_format.space_after = Pt(1.5)
    normal.paragraph_format.line_spacing = 1.0

    document.core_properties.title = title
    document.core_properties.author = "Ambuj Bhardwaj"
    document.core_properties.subject = "Professional resume"
    document.core_properties.keywords = "analytics, business intelligence, data platform, leadership"


def build_docx(source: Path) -> Path:
    blocks = parse_markdown(source)
    document = Document()
    configure_document(document, source.stem.replace("-", " ").title())
    first_h2 = True
    previous_kind = ""
    contact_next = False

    for kind, text in blocks:
        if kind == "name":
            paragraph = document.add_paragraph()
            paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
            paragraph.paragraph_format.space_after = Pt(0)
            set_run_font(paragraph.add_run(text), size=18, bold=True, color=NAVY)
        elif kind == "h2" and first_h2:
            paragraph = document.add_paragraph()
            paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
            paragraph.paragraph_format.space_after = Pt(2)
            set_run_font(paragraph.add_run(text), size=11, bold=True, color=SLATE)
            first_h2 = False
            contact_next = True
        elif kind == "h2":
            paragraph = document.add_paragraph()
            paragraph.paragraph_format.space_before = Pt(5)
            paragraph.paragraph_format.space_after = Pt(2)
            paragraph.paragraph_format.keep_with_next = True
            set_run_font(paragraph.add_run(text), size=10.2, bold=True, color=NAVY)
            set_cell_free_border(paragraph)
        elif kind == "role":
            paragraph = document.add_paragraph()
            paragraph.paragraph_format.space_before = Pt(3)
            paragraph.paragraph_format.space_after = Pt(0.5)
            paragraph.paragraph_format.keep_with_next = True
            set_run_font(paragraph.add_run(text), size=9.5, bold=True, color=NAVY)
        elif kind == "bullet":
            paragraph = document.add_paragraph(style="List Bullet")
            paragraph.paragraph_format.left_indent = Inches(0.16)
            paragraph.paragraph_format.first_line_indent = Inches(-0.14)
            paragraph.paragraph_format.right_indent = Inches(0)
            paragraph.paragraph_format.space_after = Pt(1.2)
            paragraph.paragraph_format.line_spacing = 1.0
            add_inline_runs(paragraph, text, size=8.8)
        else:
            paragraph = document.add_paragraph()
            if contact_next:
                paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
                contact_next = False
            paragraph.paragraph_format.space_after = Pt(2)
            is_title = text.startswith("**") and text.endswith("**")
            if is_title:
                paragraph.paragraph_format.keep_with_next = True
                set_run_font(paragraph.add_run(text[2:-2]), size=9.1, bold=True, italic=True, color=SLATE)
            else:
                add_inline_runs(paragraph, text, size=9.0)
        previous_kind = kind

    output = source.with_suffix(".docx")
    document.save(output)
    return output


def inline_html(text: str) -> str:
    escaped = html.escape(text)
    return re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", escaped)


def build_html(source: Path) -> Path:
    blocks = parse_markdown(source)
    parts: list[str] = []
    first_h2 = True
    in_list = False
    after_target = False

    def close_list() -> None:
        nonlocal in_list
        if in_list:
            parts.append("</ul>")
            in_list = False

    for kind, text in blocks:
        if kind != "bullet":
            close_list()
        if kind == "name":
            parts.append(f"<h1>{html.escape(text)}</h1>")
        elif kind == "h2" and first_h2:
            parts.append(f'<div class="target">{html.escape(text)}</div>')
            first_h2 = False
            after_target = True
        elif kind == "h2":
            parts.append(f"<h2>{html.escape(text)}</h2>")
            after_target = False
        elif kind == "role":
            parts.append(f"<h3>{html.escape(text)}</h3>")
            after_target = False
        elif kind == "bullet":
            if not in_list:
                parts.append("<ul>")
                in_list = True
            parts.append(f"<li>{inline_html(text)}</li>")
        else:
            css_class = ' class="contact"' if after_target else ""
            parts.append(f"<p{css_class}>{inline_html(text)}</p>")
            after_target = False
    close_list()

    css = """
@page { size: A4; margin: 0.44in 0.56in; }
* { box-sizing: border-box; }
body { margin: 0; color: #1f1f1f; font-family: Arial, Helvetica, sans-serif; font-size: 8.8pt; line-height: 1.16; }
h1 { margin: 0; color: #17365d; font-size: 18pt; line-height: 1; text-align: center; letter-spacing: 0.3pt; }
.target { margin: 2pt 0; color: #44546a; font-size: 11pt; font-weight: 700; text-align: center; }
.contact { margin: 2pt 0 5pt; color: #333; font-size: 8.5pt; text-align: center; }
h2 { margin: 5pt 0 2pt; padding-bottom: 1.5pt; border-bottom: 1.2pt solid #17365d; color: #17365d; font-size: 10.2pt; line-height: 1; page-break-after: avoid; }
h3 { margin: 4pt 0 1pt; color: #17365d; font-size: 9.5pt; line-height: 1.1; page-break-after: avoid; }
p { margin: 0 0 2.2pt; orphans: 2; widows: 2; }
p strong:only-child { color: #44546a; font-style: italic; }
ul { margin: 0 0 1pt 14pt; padding: 0; }
li { margin: 0 0 1.5pt; padding-left: 1pt; break-inside: avoid; }
strong { font-weight: 700; }
"""
    title = html.escape(source.stem.replace("-", " ").title())
    content = "\n".join(parts)
    output = source.with_suffix(".html")
    output.write_text(
        f"<!doctype html><html><head><meta charset=\"utf-8\"><title>{title}</title>"
        f"<style>{css}</style></head><body>{content}</body></html>",
        encoding="utf-8",
    )
    return output


def main() -> None:
    for filename in SOURCES:
        source = RESUME_DIR / filename
        docx_path = build_docx(source)
        html_path = build_html(source)
        print(f"Generated {docx_path.relative_to(ROOT)}")
        print(f"Generated {html_path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
