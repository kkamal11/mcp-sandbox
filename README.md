# Running the MCP Server with Inspector

## Starting the MCP Inspector

Below inspector can be used to monitor and debug your MCP server. To start the MCP Inspector, run the following command in your terminal:

```bash
npm install -g @modelcontextprotocol/inspector
mcp-inspector
```

This will launch the MCP Inspector in your default web browser.

## Running the MCP Server

In a separate terminal, navigate to the directory where your MCP server code is located and start the server:

```bash
source venv/bin/activate  # Activate your virtual environment if you have one
python3 main.py
```

## Connecting to the MCP Server

Once the MCP Inspector is running, you can connect to your MCP server as follows:

1. In the MCP Inspector, select Transport Type (by default STDIO)
2. In the Command field, enter the command to start your MCP server (e.g., `python3`).
3. In the Arguments field, enter the path to your MCP server script (e.g., `main.py`).
4. Click the "Connect" button to establish a connection between the MCP Inspector and your MCP server.

You should now see the MCP server's logs and interactions in the MCP Inspector interface, allowing you to monitor and debug your MCP server effectively.
