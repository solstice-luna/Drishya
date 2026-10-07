from app.cameras.stream import CameraStream
from app.config import HALLWAY_RTSP_URL


def create_hallway_camera() -> CameraStream:
    """Create the hallway camera stream."""
    return CameraStream(HALLWAY_RTSP_URL)
