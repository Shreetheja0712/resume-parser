from openai import OpenAI
import os
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Optional

load_dotenv()

class Experience(BaseModel):
    company: str
    role: str
    duration: str


class Education(BaseModel):
    institution: str
    degree: str
    year: str


class Project(BaseModel):
    name: str
    description: str


class ResumeParser(BaseModel):
    name: str
    email: str | None = None
    phone: str | None = None
    skills: list[str] = Field(default_factory=list)
    experience: list[Experience] = Field(default_factory=list)
    education: list[Education] = Field(default_factory=list)
    projects: list[Project] = Field(default_factory=list)

client = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",
    api_key= os.getenv("GEMINI_API_KEY")
)

file_path = "resume.txt"
try:
    with open(file_path, "r" , encoding="utf-8") as f:
            resume_text = f.read()
except Exception as e:
    print(f"An error occurred while reading the file: {e}")

try:
    response = client.chat.completions.parse(
        model = "gemini-3.5-flash-lite",
        messages = [{
            "role": "system", 
            "content": """ 
                You are a helpful assistant that extracts structured information from resumes.
                Please extract the following information from the provided resume:
                - Name
                - Email
                - Phone
                - Skills (as a list)
                - Experience (as a list of dictionaries with keys: company, role, duration)
                - Education (as a list of dictionaries with keys: institution, degree, year)
                in the format of a JSON object that matches the ResumeParser model.
            """
            },
            {
                "role": "user", 
                "content": resume_text 
            }
        ],
        response_format = ResumeParser
    )
    result: ResumeParser = response.choices[0].message.parsed

except Exception as e:
    print(f"An error occurred: {e}")

for field, value in result.model_dump().items():
    print(f"{field}: {value}")