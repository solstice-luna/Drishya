from dataclasses import dataclass
from pathlib import Path

import numpy as np

from app.recognition.encoder import FaceEncoder


SUPPORTED_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
}


@dataclass
class KnownFace:
    """Represent a known person's face encoding."""

    person_type: str
    person_identifier: str
    encoding: np.ndarray


class KnownFaceLoader:
    """Load and encode known faces from a directory."""

    def __init__(self, directory: str):
        self.directory = Path(directory)
        self.encoder = FaceEncoder()

    def load(self) -> list[KnownFace]:
        """Load all supported face images from the directory."""

        if not self.directory.exists():
            raise FileNotFoundError(
                f"Known face directory does not exist: {self.directory}"
            )

        if not self.directory.is_dir():
            raise NotADirectoryError(
                f"Known face path is not a directory: {self.directory}"
            )

        known_faces = []

        for image_path in sorted(self.directory.rglob("*")):
            if not image_path.is_file():
                continue

            if image_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
                continue

            try:
                encoding = self.encoder.encode_image(
                    str(image_path)
                )
            except ValueError as error:
                raise ValueError(
                    f"Failed to process known face image "
                    f"'{image_path}': {error}"
                ) from error

            known_faces.append(
                KnownFace(
                    person_type=self.directory.name,
                    person_identifier=image_path.stem,
                    encoding=encoding,
                )
            )

        return known_faces