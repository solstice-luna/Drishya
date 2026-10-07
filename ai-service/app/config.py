from pathlib import Path
import os

from dotenv import load_dotenv


# drishya/
ROOT_DIR = Path(__file__).resolve().parents[2]

# drishya/.env
ENV_FILE = ROOT_DIR / ".env"

load_dotenv(ENV_FILE)


APP_NAME = os.getenv("APP_NAME", "Drishya")
APP_ENV = os.getenv("APP_ENV", "development")


# Backend
BACKEND_HOST = os.getenv(
    "BACKEND_HOST",
    "127.0.0.1",
)

BACKEND_PORT = int(
    os.getenv(
        "BACKEND_PORT",
        "8000",
    )
)

BACKEND_URL = (
    f"http://{BACKEND_HOST}:{BACKEND_PORT}"
)


# AI Service
AI_SERVICE_HOST = os.getenv(
    "AI_SERVICE_HOST",
    "127.0.0.1",
)

AI_SERVICE_PORT = int(
    os.getenv(
        "AI_SERVICE_PORT",
        "8001",
    )
)

AI_SERVICE_TOKEN = os.getenv(
    "AI_SERVICE_TOKEN",
    "",
)


# go2rtc
GO2RTC_HOST = os.getenv(
    "GO2RTC_HOST",
    "127.0.0.1",
)

GO2RTC_RTSP_PORT = int(
    os.getenv(
        "GO2RTC_RTSP_PORT",
        "8554",
    )
)


# Cameras
HALLWAY_CAMERA_NAME = os.getenv(
    "HALLWAY_CAMERA_NAME",
    "Hallway",
)

AI_SERVICE_DISPLAY = os.getenv(
    "AI_SERVICE_DISPLAY",
    "false",
).lower() in {"1", "true", "yes", "on"}

CAMERA_RECONNECT_ATTEMPTS = int(
    os.getenv(
        "CAMERA_RECONNECT_ATTEMPTS",
        "3",
    )
)

HALLWAY_RTSP_URL = os.getenv(
    "HALLWAY_RTSP_URL",
    os.getenv(
        "RTSP_URL",
        f"rtsp://{GO2RTC_HOST}:{GO2RTC_RTSP_PORT}/{HALLWAY_CAMERA_NAME}",
    ),
)