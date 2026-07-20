from pathlib import Path

from mockmate.resume.extractor import PDFExtractor
from mockmate.resume.schemas import (
    Achievement,
    Certification,
    Education,
    Experience,
    PersonalInfo,
    Project,
    Resume,
    Skills,
)
from mockmate.resume.section_detector import SectionDetector


class ResumeParser:
    def __init__(self) -> None:
        self.extractor = PDFExtractor()
        self.section_detector = SectionDetector()

    def parse(self, pdf_path: str | Path) -> Resume:
        text = self.extractor.extract_text(pdf_path)

        sections = self.section_detector.detect_sections(text)

        personal_info = self.parse_personal_info(
            sections.get("personal_info", "")
        )

        education = self.parse_education(
            sections.get("education", "")
        )

        experience = self.parse_experience(
            sections.get("experience", "")
        )

        skills = self.parse_skills(
            sections.get("skills", "")
        )

        projects = self.parse_projects(
            sections.get("projects", "")
        )

        certifications = self.parse_certifications(
            sections.get("certifications", "")
        )

        achievements = self.parse_achievements(
            sections.get("achievements", "")
        )

        return Resume(
            personal_info=personal_info,
            education=education,
            experience=experience,
            skills=skills,
            projects=projects,
            certifications=certifications,
            achievements=achievements,
        )

    def parse_personal_info(self, text: str) -> PersonalInfo:
        raise NotImplementedError

    def parse_education(self, text: str) -> list[Education]:
        raise NotImplementedError

    def parse_experience(self, text: str) -> list[Experience]:
        raise NotImplementedError

    def parse_skills(self, text: str) -> Skills:
        raise NotImplementedError

    def parse_projects(self, text: str) -> list[Project]:
        raise NotImplementedError

    def parse_certifications(self, text: str) -> list[Certification]:
        raise NotImplementedError

    def parse_achievements(self, text: str) -> list[Achievement]:
        raise NotImplementedError
