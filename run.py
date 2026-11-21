import argparse
import os
import sys

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def main():
    from app.config.settings import settings

    parser = argparse.ArgumentParser(description="Run the iOS Bridge server")
    parser.add_argument("--host", default=settings.HOST)
    parser.add_argument("--port", type=int, default=settings.PORT)
    args = parser.parse_args()

    import uvicorn
    from app.main import app

    uvicorn.run(app, host=args.host, port=args.port, log_level=settings.LOG_LEVEL.lower())


if __name__ == "__main__":
    main()
