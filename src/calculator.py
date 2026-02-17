from typing import List
from fastmcp import FastMCP

calc_mcp = FastMCP(name="calculator")


@calc_mcp.tool(
    name="Addition", description="Add two numbers.", tags=["arithmetic", "addition"]
)
def add(a: float, b: float) -> float:
    """
    Add two numbers and return the result.

    :param a: A number to be added.
    :type a: float
    :param b: Another number to be added.
    :type b: float
    :return: The sum of a and b.
    :rtype: float

    Example usage:
    >>> add(2, 3)
    5.0
    """
    return a + b


@calc_mcp.tool(
    name="Multiply",
    description="Multiply two numbers.",
    tags=["arithmetic", "multiplication"],
)
def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers and return the result.

    :param a: A number to be multiplied.
    :type a: float
    :param b: Another number to be multiplied.
    :type b: float
    :return: The product of a and b.
    :rtype: float

    Example usage:
    >>> multiply(2, 3)
    6.0
    """
    return a * b


@calc_mcp.tool(
    name="Subtract",
    description="Subtract two numbers.",
    tags=["arithmetic", "subtraction"],
)
def subtract(a: float, b: float) -> float:
    """
    Subtract two numbers and return the result.

    :param a: A number to be subtracted from.
    :type a: float
    :param b: Another number to be subtracted.
    :type b: float
    :return: The difference of a and b.
    :rtype: float

    Example usage:
    >>> subtract(5, 2)
    3.0
    """
    return a - b


@calc_mcp.tool(
    name="Add_Multiple_Numbers",
    description="Add multiple numbers together.",
    tags=["arithmetic", "addition"],
)
def add_multiple_numbers(L: List[float]) -> float:
    """
    Add multiple numbers in a list and return the result.

    :param L: A list of numbers to be added.
    :type L: List[float]
    :return: The sum of all the numbers.
    :rtype: float

    Example usage:
    >>> add_multiple_numbers(1, 2, 3, 4)
    10.0
    """
    return sum(L)
