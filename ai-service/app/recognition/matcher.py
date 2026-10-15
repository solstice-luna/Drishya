import face_recognition


class FaceMatcher:
    """Match a face encoding against known face encodings."""

    def __init__(self, tolerance: float = 0.5):
        if not 0 < tolerance <= 1:
            raise ValueError("Tolerance must be between 0 and 1.")

        self.tolerance = tolerance

    def match(self, face_encoding, known_faces):
        """Return the best matching known face, or None."""

        if not known_faces:
            return None

        known_encodings = [
            known_face.encoding
            for known_face in known_faces
        ]

        distances = face_recognition.face_distance(
            known_encodings,
            face_encoding,
        )

        best_match_index = distances.argmin()

        if distances[best_match_index] > self.tolerance:
            return None

        return known_faces[best_match_index]