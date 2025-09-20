"""
Logging utilities for the English School MCP Server
"""
import logging


class ColoredFormatter(logging.Formatter):
    """Custom formatter to add colors to log levels"""
    
    # Color codes
    COLORS = {
        'DEBUG': '\033[36m',     # Cyan
        'INFO': '\033[32m',      # Green
        'WARNING': '\033[33m',   # Yellow
        'ERROR': '\033[31m',     # Red
        'CRITICAL': '\033[35m',  # Magenta
    }
    RESET = '\033[0m'  # Reset color
    
    def format(self, record):
        # Get the color for the log level
        color = self.COLORS.get(record.levelname, self.RESET)
        
        # Create colored log level
        colored_levelname = f"{color}{record.levelname}{self.RESET}"
        
        # Replace the levelname with colored version
        record.levelname = colored_levelname
        
        # Format the message
        return super().format(record)


def setup_colored_logging(log_level: str = "INFO") -> None:
    """
    Setup colored logging for the application
    
    Args:
        log_level (str): The logging level to use
    """
    # Configure logging with colored output
    logger = logging.getLogger()
    logger.setLevel(getattr(logging, log_level.upper(), logging.INFO))
    
    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(getattr(logging, log_level.upper(), logging.INFO))
    
    # Create colored formatter
    colored_formatter = ColoredFormatter(
        '%(levelname)s: %(asctime)s - %(message)s'
    )
    console_handler.setFormatter(colored_formatter)
    
    # Add handler to logger
    logger.handlers.clear()  # Clear any existing handlers
    logger.addHandler(console_handler)