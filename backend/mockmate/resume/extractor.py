from pathlib import Path

import fitz


class ResumeExtractionError(Exception):
    """Raised when resume text extraction fails."""


class PDFExtractor:
    def __init__(self) -> None:
        pass

    def extract_text(self, pdf_path: str | Path) -> str:
        pdf_path = Path(pdf_path)

        if not pdf_path.exists():
            raise ResumeExtractionError(
                f"Resume file not found: {pdf_path}"
            )

        if pdf_path.suffix.lower() != ".pdf":
            raise ResumeExtractionError(
                "Only PDF resumes are currently supported."
            )

        try:
            document = fitz.open(pdf_path)

            pages = []

            for page in document:
                text = page.get_text()

                if text:
                    pages.append(text)

            document.close()

        except Exception as exc:
            raise ResumeExtractionError(
                f"Failed to read PDF: {exc}"
            ) from exc

        if not pages:
            raise ResumeExtractionError(
                "No readable text found in the PDF. The resume may be scanned or image-based."
            )

        return self._clean_text("\n".join(pages))

    def _clean_text(self, text: str) -> str:
        lines = []

        for line in text.splitlines():
            cleaned = " ".join(line.split())

            if cleaned:
                lines.append(cleaned)

        return "\n".join(lines)
