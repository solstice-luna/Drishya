import logging

import cv2


logger = logging.getLogger(__name__)


class CameraStream:
    def __init__(self, url: str):
        self.url = url
        self.capture = None

    def connect(self):
        """Connect to the camera stream."""
        if self.capture is not None:
            self.release()

        self.capture = cv2.VideoCapture(self.url)

        if not self.capture.isOpened():
            self.capture = None
            raise RuntimeError("Could not connect to camera stream.")

        logger.info("Camera connected.")
        return self

    def read(self):
        """Read the next frame from the camera."""
        if self.capture is None:
            raise RuntimeError("Camera is not connected.")

        success, frame = self.capture.read()

        if not success:
            logger.warning("Failed to read frame from camera.")
            return False, None

        return True, frame

    def release(self):
        """Release the camera stream."""
        if self.capture is not None:
            self.capture.release()
            self.capture = None

        logger.info("Camera released.")
