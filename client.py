from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv()
import os
import asyncio

async def main():
    client = MultiServerMCPClient(
        {
            "math": {
                "command":"python",
                "args": ["mathserver.py"],
                "transport": "stdio",
                },

            "weather": {
                "url": "http://localhost:8000/mcp",
                "transport": "streamable-http",
                }
        }
    )

    os.environ["GROQ_API_KEY"] = os.getenv('GROQ_API_KEY')
    tools = await client.get_tools()
    model = ChatGroq(model = 'qwen/qwen3-32b')
    agent = create_react_agent(
        model=model,
        tools=tools,
        verbose=True
    )

    math_response = await agent.invoke(
        {"messages": [{"role": "user", "content": "What is (5 X 3) + 15?"}]}
    )
    print("Math Response:", math_response['messages'][-1].content)

    weather_response = await agent.invoke(
        {"messages": [{"role": "user", "content": "What is the current temperature in New Delhi?"}]})
    
    print("Weather Response:", weather_response['messages'][-1].content)

asyncio.run(main())


