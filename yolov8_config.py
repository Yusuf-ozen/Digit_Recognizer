from pathlib import Path
import sys

# Get the absolute path of the current file
FILE = Path(__file__).resolve()
# Get the parent directory of the current file
ROOT = FILE.parent
# Add the root path to the sys.path list if it is not already there
if ROOT not in sys.path:
    sys.path.append(str(ROOT))
# Get the relative path of the root directory with respect to the current working directory
ROOT = ROOT.relative_to(Path.cwd())

# Sources
IMAGE = 'Image'
WEBCAM = 'Webcam'
YOUTUBE = 'YouTube'
SOURCES_LIST = [IMAGE, WEBCAM, YOUTUBE]

# Images config
IMAGES_DIR = ROOT / 'assets/images'
DEFAULT_IMAGE = IMAGES_DIR / 'num_856.jpeg'
DEFAULT_DETECT_IMAGE = IMAGES_DIR / 'num_detected.jpg'

# ML Model config
MODEL_DIR = ROOT / 'models'
DETECTION_MODEL = MODEL_DIR / 'best_yolov8.pt'


#SEGMENTATION_MODEL = MODEL_DIR / 'yolov8n-seg.pt'

# Webcam
WEBCAM_PATH = 0