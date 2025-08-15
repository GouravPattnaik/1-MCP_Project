# MCP_Project1

## Overview

MCP_Project1 is a Python project that leverages LangChain, MCP, and LangGraph to build advanced AI workflows. It uses the `langchain-mcp-adapters` package to integrate MCP with LangChain.

## Features

- Multi-server MCP client integration
- LangChain and LangGraph support
- Modular and extensible architecture

## Requirements

- **Python 3.10** (required for `langchain-mcp-adapters`)
- See `requirements.txt` for all dependencies

## Installation

1. **Install Python 3.10**  
   Download from [python.org](https://www.python.org/downloads/release/python-3100/).

2. **Create and activate a virtual environment:**
   ```
   python3.10 -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the client:
```
python client.py
```

## Project Structure

```
e:\1-MCP\
│
├── client.py
├── requirements.txt
├── pyproject.toml
└── README.md
```

## Troubleshooting

- Ensure you are using Python 3.10.
- If you see `ModuleNotFoundError`, check your virtual environment and installed packages.