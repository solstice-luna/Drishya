import logging
import time

import cv2

from app.cameras.hallway import create_hallway_camera
from app.config import AI_SERVICE_DISPLAY, CAMERA_RECONNECT_ATTEMPTS
from app.detection.face_detector import FaceDetector


logger = logging.getLogger(__name__)


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )

    camera = create_hallway_camera()
    detector = FaceDetector()

    logger.info("AI Service started.")
    logger.info("Camera: Hallway")
    frame_count = 0
    frame_count = 0

    try:
        camera.connect()

        while True:
            success, frame = camera.read()

            if not success:
                logger.warning("Failed to read camera frame.")

                camera.release()

                reconnected = False

                for attempt in range(1, CAMERA_RECONNECT_ATTEMPTS + 1):
                    try:
                        logger.info(
                            "Reconnecting to camera "
                            "(attempt %d/%d).",
                            attempt,
                            CAMERA_RECONNECT_ATTEMPTS,
                        )

                        camera.connect()
                        reconnected = True
                        break

                    except RuntimeError:
                        logger.warning(
                            "Camera reconnect attempt %d/%d failed.",
                            attempt,
                            CAMERA_RECONNECT_ATTEMPTS,
                        )

                        time.sleep(2)

                if not reconnected:
                    raise RuntimeError(
                        "Could not reconnect to the camera after "
                        f"{CAMERA_RECONNECT_ATTEMPTS} attempts."
                    )

                continue

            frame_count += 1

            # Run face detection every 5th frame.
            if frame_count % 5 == 0:
                faces = detector.detect(frame)

                for x, y, width, height in faces:
                    cv2.rectangle(
                        frame,
                        (x, y),
                        (x + width, y + height),
                        (0, 255, 0),
                        2,
                    )

                    cv2.putText(
                        frame,
                        "Face",
                        (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        (0, 255, 0),
                        2,
                    )

            if AI_SERVICE_DISPLAY:
                cv2.imshow("Drishya AI - Hallway", frame)

                if cv2.waitKey(1) & 0xFF == 27:
                    break

    finally:
        camera.release()

        if AI_SERVICE_DISPLAY:
            cv2.destroyAllWindows()


if __name__ == "__main__":
    main()