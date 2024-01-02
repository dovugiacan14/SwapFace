import logging
import io 
import base64
from PIL import Image

def is_base64(str):
    try:
        base64.b64decode(str)
        return True
    except Exception as e:
        logging.debug(f"Check not base64: {e}")
        return False

def pil_to_base64(img):
    try: 
        im = Image.open(img)
        img_bytes = io.BytesIO()
        im.save(img_bytes, format='PNG')
        img_base64 = base64.b64encode(img_bytes.getvalue()).decode('utf-8')
        return img_base64
    except Exception as e:
        logging.error(f"Error converting PIL image to base64: {e}")
        return None

