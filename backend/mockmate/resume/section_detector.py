import re


class SectionDetector:
    SECTION_HEADERS = {
        "education": [
            "education",
            "academic background",
            "academic qualifications",
        ],
        "experience": [
            "experience",
            "work experience",
            "professional experience",
            "employment",
        ],
        "projects": [
            "projects",
            "personal projects",
            "academic projects",
        ],
        "skills": [
            "skills",
            "technical skills",
            "technical expertise",
        ],
        "certifications": [
            "certifications",
            "certificates",
            "licenses",
        ],
        "achievements": [
            "achievements",
            "awards",
            "honors",
        ],
    }

    def detect_sections(self, text: str) -> dict[str, str]:
        lines = text.splitlines()

        sections = {}
        current_section = "personal_info"
        current_content = []

        for line in lines:
            stripped = line.strip()

            matched = self._match_section(stripped)

            if matched:
                sections[current_section] = "\n".join(current_content).strip()
                current_section = matched
                current_content = []
            else:
                current_content.append(line)

        sections[current_section] = "\n".join(current_content).strip()

        return sections

    def _match_section(self, line: str) -> str | None:
        normalized = re.sub(r"[^a-z ]", "", line.lower()).strip()

        for section, headers in self.SECTION_HEADERS.items():
            if normalized in headers:
                return section

        return None
