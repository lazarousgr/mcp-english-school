# English School MCP Server

An MCP (Model Context Protocol) server designed to consume custom REST services for data preparation in educational contexts. Project is intended for educational purpose only.

## Overview

This MCP server acts as a bridge between Claude AI and various REST services, enabling efficient data preparation and processing workflows for English school application. The server provides tools that can be consumed by Claude through the MCP protocol, allowing for seamless integration of external services and data sources.

## Features

- **REST Service Integration**: Consumes and integrates with custom REST APIs
- **Data Preparation Tools**: Specialized tools for educational data processing
- **FastMCP Framework**: Built on FastMCP for robust and scalable service delivery

## Prerequisites

- Python 3.8 or higher
- uv (Python package manager)
- ngrok (for exposing local server)
- Claude CLI

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd mcp-english-school
   ```

2. **Initialize UV and install dependencies**:
   ```bash
   uv init
   uv add fastmcp python-dotenv starlette
   ```

3. **Set up environment variables**:
   ```bash
   cp .env.example .env
   # Edit .env file with your configuration
   ```

## Configuration

The server uses environment variables for configuration. Create a `.env` file in the project root:

```properties
LOG_LEVEL=INFO
HOST=127.0.0.1
PORT=8000
```

### Environment Variables

- `LOG_LEVEL`: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- `HOST`: Server host address (default: 127.0.0.1)
- `PORT`: Server port (default: 8000)

## Running the MCP Server

### Local Development

1. **Start the MCP server**:
   ```bash
   uv run main.py
   ```

2. **Verify the server is running**:
   The server will start on `http://127.0.0.1:8000` by default.

## Setting up ngrok (Linux)

### Installation

1. **Using npm** (Recommended if you have Node.js):
   ```bash
    npm install -g ngrok
    ```

### Running ngrok

1. **Expose your local MCP server**:
   ```bash
   ngrok http 8000
   ```

2. **Note the public URL**:
   ngrok will display a public URL (e.g., `https://abc123.ngrok.io`) that forwards to your local server.

## Connecting Claude CLI to MCP Server

### Installation of Claude CLI

1. **Install Claude CLI**:
   ```bash
   npm install -g @anthropic-ai/claude-cli
   ```


### MCP Server Configuration

1. **Create MCP configuration file** (`~/.config/claude/mcp_servers.json`):
   ```bash
   claude mcp add --transport http mcp_name ngrok_url/mcp
   ```

## Available Tools

### Core Tools

- **health_check**: Verify server status
- **echo**: Echo back input messages for testing



## Development

### Project Structure

```
mcp-english-school/
├── main.py              # Main MCP server application
├── logging_utils.py     # Colored logging utilities
├── .env                 # Environment configuration
├── .env.example         # Example environment file
├── README.md           # This file
└── requirements.txt    # Python dependencies (if using pip)
```