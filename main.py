def run_calc_mcp():
    from src.calc_stdio import calc_mcp

    calc_mcp.run()


def run_fastapi():
    import uvicorn
    from src.fastapi_mcp_calc import app

    uvicorn.run(app, host="127.0.0.1", port=8005)


def run_feed_mcp():
    from src.fee_search_mcp import feed_mcp

    feed_mcp.run()


def main():
    # run_calc_mcp()
    # run_fastapi()
    run_feed_mcp()


if __name__ == "__main__":
    main()
