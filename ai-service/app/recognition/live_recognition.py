import cv2
import face_recognition

from app.recognition.known_faces import KnownFaceLoader
from app.recognition.matcher import FaceMatcher


class LiveFaceRecognizer:
    def __init__(self, known_faces_dir: str):
        self.known_faces = self._load_known_faces(known_faces_dir)
        self.matcher = FaceMatcher(tolerance=0.5)

    def _load_known_faces(self, known_faces_dir: str):
        known_faces = []

        for category in ["students", "teachers"]:
            directory = f"{known_faces_dir}/{category}"

            loader = KnownFaceLoader(directory)
            known_faces.extend(loader.load())

        return known_faces

    def recognize(self, frame):
        # OpenCV uses BGR; face_recognition expects RGB.
        rgb_frame = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB,
        )

        face_locations = face_recognition.face_locations(
            rgb_frame
        )

        face_encodings = face_recognition.face_encodings(
            rgb_frame,
            face_locations,
        )

        results = []

        for face_location, face_encoding in zip(
            face_locations,
            face_encodings,
        ):
            matched_person = self.matcher.match(
                face_encoding,
                self.known_faces,
            )

            results.append(
                {
                    "location": face_location,
                    "person": matched_person,
                }
            )

        return results