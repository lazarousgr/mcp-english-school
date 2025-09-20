from fastmcp import FastMCP
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from starlette.applications import Middleware
from logging_utils import setup_colored_logging
import os
import logging
from typing import Dict

# Load environment variables from .env file
load_dotenv()

mcp = FastMCP(name="English School MCP Server")

@mcp.tool()
def health_check() -> str:
    """
    Health check endpoint to verify server status.
    
    Returns:
        str: Simple status message
    """
    return "ok"

@mcp.tool()
def echo(message: str) -> Dict[str, str]:
    """
    Echo tool that returns the input message.
    
    Args:
        message (str): The message to echo back
        
    Returns:
        Dict[str, str]: The echoed message
    """
    logging.info(f"Echoing message: {message}")
    return {"echo": message}


if __name__ == "__main__":
    
    log_level = os.getenv("LOG_LEVEL", "INFO").upper()
    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT", "8000"))

    # Setup colored logging
    setup_colored_logging(log_level)

    logging.info("Starting English School MCP Server")
    # Start the MCP server with HTTP streaming transport
    mcp.run(
        transport="http",
        host=host,
        port=port,
        middleware=[
            Middleware(
                CORSMiddleware,
                allow_origins=["*"],
                allow_methods=["*"],
                allow_headers=["*"],
                allow_credentials=True
            )
        ]
    )