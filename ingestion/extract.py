from pathlib import Path
from pypdf import PdfReader


def extract_pdf(pdf_path):
    reader = PdfReader(pdf_path)

    pages = []

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text() or ""

        pages.append({
            "text": text,
            "page": page_number,
            "source": Path(pdf_path).name
        })

    return pages