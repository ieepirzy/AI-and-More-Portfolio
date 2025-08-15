import mcp
import datetime
import os
import asyncio
import json
import sys
from datetime import datetime, timezone
from typing import Any, Dict

"""
The purpose of this code and excersice is to provide practice with the MCP (Model-Context-Protocol) protocol.
The main challenge I foresee is correct usage of the MCP protocol. 

I will be referring to this URL for the MCP documentation on server implementation: https://modelcontextprotocol.io/quickstart/server
"""

# For a basic MCP server, you typically need:
# 1. Handle initialization
# 2. List available tools  
# 3. Execute tool calls
# 4. Return structured responses


class MCPDatetimetoolserver:
    def __init__(self):
        #on initialization, this tells the server what tools it has available...
        self.tools={
            "get_current_datetime": {
                "description": "Returns the current date and time in ISO 8601 format.",
                "input-schema":{ #Schema for what should be included in the call-request
                    "input-type": "void",                   
                },
                "output-schema":{ #Schema for what the output is expected to be like
                    "type": "datetime-object",
                    "format": "ISO-8601",
                }
            }
        }
        

    def get_current_datetime(self):
        return datetime.datetime.now().isoformat()
    

    def handle_tool_call(self, toolname):
        if toolname == "get_current_datetime":
            return self.get_current_datetime()
        else:
            raise ValueError(f"Tool '{toolname}' not found.")
        

        

"""
Normally I would like to use a library such as httpx here to allow requests outside the local network.
However, for this exercise, we will keep it simple and run the server and AI model locally.
"""


async def main():
    # Create an MCP server instance
    server = mcp.Server()
    await server.run()

   



