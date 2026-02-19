import feedparser
from typing import List, Dict
from fastmcp import FastMCP

mcp = FastMCP(
    name="Fee Search MCP",
)


@mcp.tool()
def fcc_feed_search(query: str, max_results: int = 3) -> List[Dict[str, str]]:
    """
    Search the FCC feed via RSS for news articles related to the given query.

    Args:
        query (str): The search query.
    Returns:
        list: A list of dictionaries containing the title, description.
    """
    feed_url: str = "https://www.freecodecamp.org/news/rss"
    feed = feedparser.parse(feed_url)
    results: List[Dict[str, str]] = []
    query_: str = query.lower()
    for entry in feed.entries:
        title: str = entry.get("title", "").lower()
        description: str = entry.get("description", "").lower()
        if query_ in title or query_ in description:
            results.append({"title": title, "description": description})
        if len(results) >= max_results:
            break

    return results
