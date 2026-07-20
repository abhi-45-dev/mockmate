from pathlib import Path

from mockmate.resume.parser import ResumeParser
from mockmate.resume.schemas import Resume


class ResumeService:
    def __init__(self) -> None:
        self.parser = ResumeParser()

    def parse_resume(self, pdf_path: str | Path) -> Resume:
        return self.parser.parse(pdf_path)
