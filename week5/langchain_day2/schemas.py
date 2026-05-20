from pydantic import BaseModel, Field
from typing import List


class UserStory(BaseModel):

    title: str = Field(
        min_length=5,
        max_length=100
    )

    description: str = Field(
        min_length=10
    )


class Task(BaseModel):

    title: str = Field(
        min_length=5
    )

    priority: str = Field(
        pattern="^(High|Medium|Low)$"
    )


class RequirementAnalysis(BaseModel):

    project_name: str = Field(
        min_length=3
    )

    user_stories: List[UserStory]

    tasks: List[Task]

    risks: List[str]