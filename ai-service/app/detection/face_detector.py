import cv2
import logging


logger = logging.getLogger(__name__)


class FaceDetector:
    """Detect faces in video frames using a Haar Cascade."""

    def __init__(
        self,
        scale_factor: float = 1.1,
        min_neighbors: int = 5,
        min_size: tuple[int, int] = (50, 50),
    ):
        self.cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades
            + "haarcascade_frontalface_default.xml"
        )

        if self.cascade.empty():
            raise RuntimeError("Could not load face detection model.")

        self.scale_factor = scale_factor
        self.min_neighbors = min_neighbors
        self.min_size = min_size

        logger.info("Face detector initialized.")

    def detect(self, frame):
        """Detect faces in a BGR video frame."""

        if frame is None:
            raise ValueError("Frame cannot be None.")

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = self.cascade.detectMultiScale(
            gray,
            scaleFactor=self.scale_factor,
            minNeighbors=self.min_neighbors,
            minSize=self.min_size,
        )

        return faces
