from fastapi import FastAPI
from fastapi_mcp import FastApiMCP

app = FastAPI(
    title="MCP Calculator API",
    description="API for calculating MCP values based on user input.",
)


@app.get("/")
def read_root():
    return {
        "message": "Welcome to the MCP Calculator API! Use the endpoints to perform calculations.",
        "available_endpoints": ["/add/", "/subtract/", "/multiply/", "/divide/"],
        "docs": "Access the API documentation at /docs",
    }


@app.post("/add/")
def add_numbers(a: float, b: float):
    """
    Add two numbers and return the result.

    :param a: A number to be added
    :type a: float
    :param b: Another number to be added
    :type b: float

    :return: The sum of the two numbers
    :rtype: dict
    """
    return {"result": a + b}


@app.post("/subtract/")
def subtract_numbers(a: float, b: float):
    """
    Subtract two numbers and return the result.

    :param a: A number to be subtracted from
    :type a: float
    :param b: Another number to subtract
    :type b: float

    :return: The difference of the two numbers
    :rtype: dict
    """
    return {"result": a - b}


@app.post("/multiply/")
def multiply_numbers(a: float, b: float):
    """
    Multiply two numbers and return the result.

    :param a: A number to be multiplied
    :type a: float
    :param b: Another number to be multiplied
    :type b: float

    :return: The product of the two numbers
    :rtype: dict
    """
    return {"result": a * b}


@app.post("/divide/")
def divide_numbers(a: float, b: float):
    """
    Divide two numbers and return the result.

    :param a: A number to be divided
    :type a: float
    :param b: Another number to divide by
    :type b: float

    :return: The quotient of the two numbers
    :rtype: dict
    """
    if b == 0:
        return {"error": "Division by zero is not allowed."}
    return {"result": a / b}


# Converting it to MCP
mcp = FastApiMCP(app, name="MCP Calculator")
mcp.mount_http()
