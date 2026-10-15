from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass
class RecognitionEvent:
    person_type: str
    person_identifier: str
    camera: str
    recognized_at: datetime

    @classmethod
    def create(
        cls,
        person_type: str,
        person_identifier: str,
        camera: str,
    ):
        return cls(
            person_type=person_type,
            person_identifier=person_identifier,
            camera=camera,
            recognized_at=datetime.now(timezone.utc),
        )

    def to_dict(self):
        return {
            "person_type": self.person_type,
            "person_identifier": self.person_identifier,
            "camera": self.camera,
            "recognized_at": self.recognized_at.isoformat(),
        }