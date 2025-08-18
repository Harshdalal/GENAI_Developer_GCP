# ================================================================
# __main__.py - Main Server Application
# ================================================================
# PURPOSE: Sets up and runs the A2A server with multi-skill agent
#
# FUNCTIONALITY:
# - Defines two skills: Greeting and Quote
# - Creates agent card advertising both skills
# - Configures DefaultRequestHandler with MultiSkillAgentExecutor
# - Starts Uvicorn server on port 9999
#
# USAGE: uv run . 
# ================================================================
import uvicorn
from a2a.server.apps import A2AStarletteApplication
from a2a.server.request_handlers import DefaultRequestHandler
from a2a.server.tasks import InMemoryTaskStore
from a2a.types import AgentCapabilities, AgentCard, AgentSkill
from agent_executor import MultiSkillAgentExecutor


def main():
    # Define both skills
    greeting_skill = AgentSkill(
        id="hello_world",
        name="Greet",
        description="Return a friendly greeting",
        tags=["greeting", "hello", "world"],
        examples=["Hey", "Hello", "Hi"],
    )
    
    quote_skill = AgentSkill(
        id="quote", 
        name="Get Quote",
        description="Return a motivational quote",
        tags=["quote", "motivation", "inspiration"],
        examples=["Inspire me", "Give me a quote", "Motivate me"],
    )

    agent_card = AgentCard(
        name="Multi-Skill Agent",
        description="An agent that can greet and provide motivational quotes",
        url="http://localhost:9999/",
        defaultInputModes=["text"],
        defaultOutputModes=["text"],
        skills=[greeting_skill, quote_skill],  # Both skills in one agent
        version="1.0.0",
        capabilities=AgentCapabilities(),
    )

    request_handler = DefaultRequestHandler(
        agent_executor=MultiSkillAgentExecutor(),  # Single executor handles both
        task_store=InMemoryTaskStore(),
    )

    server = A2AStarletteApplication(
        http_handler=request_handler,
        agent_card=agent_card,
    )

    print("Starting Multi-Skill Agent with skills:")
    for skill in agent_card.skills:
        print(f"  - {skill.name} (id: {skill.id})")

    uvicorn.run(server.build(), host="0.0.0.0", port=9999)


if __name__ == "__main__":
    main()