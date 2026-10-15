import face_recognition
import numpy as np


class FaceEncoder:
    """Generate a face encoding from an image containing one face."""

    def encode_image(self, image_path: str) -> np.ndarray:
        """Load an image and return the encoding of its single face."""

        image = face_recognition.load_image_file(image_path)

        face_locations = face_recognition.face_locations(image)

        if not face_locations:
            raise ValueError(
                f"No face found in image: {image_path}"
            )

        if len(face_locations) > 1:
            raise ValueError(
                f"Multiple faces found in image: {image_path}. "
                "Use an image containing only one person."
            )

        encodings = face_recognition.face_encodings(
            image,
            face_locations,
        )

        if not encodings:
            raise ValueError(
                f"Could not encode face: {image_path}"
            )

        return encodings[0]