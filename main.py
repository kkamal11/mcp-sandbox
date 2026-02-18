from src.calc_stdio import calc_mcp
from src.fastapi_mcp_calc import app


def run_calc_mcp():
    calc_mcp.run()


def run_fastapi():
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8005)


def main():
    # run_calc_mcp()
    run_fastapi()


if __name__ == "__main__":
    main()
