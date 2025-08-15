from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()
def get_temperature(city: str) -> str:
    """Returns the current temperature in Celsius for the specified city."""
    # Placeholder implementation; replace with actual API call
    return f"Current temperature in New Delhi is 25°C and its always raining."

if __name__ == "__main__":
    mcp.run(transport='streamable-http', debug=True)