import json
import os
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from app.events.event_manager import RecognitionEventManager


BACKEND_URL = os.getenv(
    "BACKEND_URL",
    "http://127.0.0.1:3000",
).rstrip("/")
AI_SERVICE_TOKEN = os.getenv("AI_SERVICE_TOKEN")


def send_event(event: dict) -> dict:
    if not AI_SERVICE_TOKEN:
        raise RuntimeError("AI_SERVICE_TOKEN must be set before running this test.")

    request = Request(
        f"{BACKEND_URL}/api/v1/recognition-events",
        data=json.dumps(event).encode(),
        headers={
            "Content-Type": "application/json",
            "x-ai-service-token": AI_SERVICE_TOKEN,
        },
        method="POST",
    )

    try:
        with urlopen(request, timeout=5) as response:
            return json.loads(response.read())
    except HTTPError as error:
        body = error.read().decode()
        raise RuntimeError(
            f"Backend rejected recognition event ({error.code}): {body}"
        ) from error
    except URLError as error:
        raise RuntimeError(f"Could not reach backend at {BACKEND_URL}.") from error


def main() -> None:
    manager = RecognitionEventManager(cooldown_seconds=5)
    event = manager.create_event(
        person_type="student",
        person_identifier="student_001",
        camera="hallway",
    )

    if event is None:
        raise RuntimeError("The recognition event was unexpectedly suppressed.")

    response = send_event(event.to_dict())
    assert response["success"] is True
    assert response["event"] == event.to_dict()
    print("Backend accepted recognition event:", response)


if __name__ == "__main__":
    main()
