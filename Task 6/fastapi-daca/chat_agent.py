# chat_agent.py
from agents import Agent, Runner

# Define a simple agent
agent = Agent(
    name="Time Agent",
    instructions="Provide the current time."
)

async def get_current_time():
    return await Runner.run(agent, "What time is it?")
