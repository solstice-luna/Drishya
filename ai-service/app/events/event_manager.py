from datetime import datetime, timedelta, timezone

from app.events.event import RecognitionEvent


class RecognitionEventManager:
    def __init__(self, cooldown_seconds: int = 10):
        self.cooldown_seconds = cooldown_seconds
        self.last_recognized = {}

    def create_event(
        self,
        person_type: str,
        person_identifier: str,
        camera: str,
    ):
        key = (
            person_type,
            person_identifier,
            camera,
        )

        now = datetime.now(timezone.utc)

        last_time = self.last_recognized.get(key)

        if last_time is not None:
            elapsed = now - last_time

            if elapsed < timedelta(seconds=self.cooldown_seconds):
                return None

        self.last_recognized[key] = now

        return RecognitionEvent.create(
            person_type=person_type,
            person_identifier=person_identifier,
            camera=camera,
        )