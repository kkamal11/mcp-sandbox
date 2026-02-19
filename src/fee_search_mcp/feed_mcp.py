import feedparser
from fastmcp import FastMCP

mcp = FastMCP(
    name="Fee Search MCP",
)


@mcp.tool()
def fcc_feed_search(query: str, max_results: int = 3) -> str:
    """
    Search the FCC feed via RSS for news articles related to the given query.

    Args:
        query (str): The search query.
    Returns:
        list: A list of dictionaries containing the title, description, and link of each relevant article.
    """
    feed_url: str = "https://www.freecodecamp.org/news/rss"
    feed = feedparser.parse(feed_url)
    results = []
    query = query.lower()
    for entry in feed.entries:
        title = entry.get("title", "").lower()
        description = entry.get("description", "").lower()
        if query in title or query in description:
            results.append(
                {
                    "title": title,
                    "description": description,
                    "link": entry.get("link", ""),
                }
            )
        if len(results) >= max_results:
            break

    if not results:
        return [{"message": "No results found for the query."}]
    return results
