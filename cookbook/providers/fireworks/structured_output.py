from typing import List
from rich.pretty import pprint  # noqa
from pydantic import BaseModel, Field
from phi.agent import Agent, RunResponse  # noqa
from phi.model.fireworks import Fireworks


class MovieScript(BaseModel):
    setting: str = Field(..., description="Provide a nice setting for a blockbuster movie.")
    ending: str = Field(..., description="Ending of the movie. If not available, provide a happy ending.")
    genre: str = Field(
        ..., description="Genre of the movie. If not available, select action, thriller or romantic comedy."
    )
    name: str = Field(..., description="Give a name to this movie")
    characters: List[str] = Field(..., description="Name of characters for this movie.")
    storyline: str = Field(..., description="3 sentence storyline for the movie. Make it exciting!")


# Agent that uses JSON mode
agent = Agent(
    model=Fireworks(id="accounts/fireworks/models/firefunction-v2"),
    description="You write movie scripts.",
    response_model=MovieScript,
)

# Get the response in a variable
# response: RunResponse = agent.run("New York")
# pprint(json_mode_response.content)

agent.print_response("New York")
