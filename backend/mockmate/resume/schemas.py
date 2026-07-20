from typing import List

from pydantic import BaseModel, ConfigDict, Field, HttpUrl


class PersonalInfo(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str
    location: str | None = None
    linkedin: HttpUrl | None = None
    github: HttpUrl | None = None
    portfolio: HttpUrl | None = None


class Education(BaseModel):
    model_config = ConfigDict(extra="forbid")

    degree: str
    institution: str
    cgpa: float | None = None
    start_year: int | None = None
    end_year: int | None = None


class Experience(BaseModel):
    model_config = ConfigDict(extra="forbid")

    job_title: str
    company: str
    description: str | None = None
    technologies: List[str] = Field(default_factory=list)
    start_date: str | None = None
    end_date: str | None = None


class Skills(BaseModel):
    model_config = ConfigDict(extra="forbid")

    languages: List[str] = Field(default_factory=list)
    frameworks: List[str] = Field(default_factory=list)
    databases: List[str] = Field(default_factory=list)
    cloud: List[str] = Field(default_factory=list)
    ai_ml: List[str] = Field(default_factory=list)
    devops: List[str] = Field(default_factory=list)
    tools: List[str] = Field(default_factory=list)


class Project(BaseModel):
    model_config = ConfigDict(extra="forbid")

    title: str
    description: str
    technologies: List[str] = Field(default_factory=list)

    project_type: str | None = None

    github_urls: List[HttpUrl] = Field(default_factory=list)
    live_urls: List[HttpUrl] = Field(default_factory=list)


class Certification(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str
    issuer: str
    issue_date: str | None = None
    credential_id: str | None = None
    credential_url: HttpUrl | None = None


class Achievement(BaseModel):
    model_config = ConfigDict(extra="forbid")

    title: str
    description: str | None = None


class Resume(BaseModel):
    model_config = ConfigDict(extra="forbid")

    personal_info: PersonalInfo

    education: List[Education] = Field(default_factory=list)
    experience: List[Experience] = Field(default_factory=list)

    skills: Skills = Field(default_factory=Skills)

    projects: List[Project] = Field(default_factory=list)
    certifications: List[Certification] = Field(default_factory=list)
    achievements: List[Achievement] = Field(default_factory=list)
