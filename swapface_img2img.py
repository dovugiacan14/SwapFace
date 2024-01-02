import os 
import logging 
from concurrent.futures import ProcessPoolExecutor
from helpers.get_params import GETPARAMS
from helpers.base64_convert import pil_to_base64 
from config.service_config import * 
from services.swapface import SwapFaceProcessing 

def preprocessing(image_file):
    source_image = pil_to_base64(SOURCE_IMAGE) 
    try:
        # get payload params 
        swap_image_file = os.path.join(SWAP_IMAGE_PATH, image_file)
        params = GETPARAMS(swap_image_file, MODEL_PATH, REACTOR_PARAMS)
        payload = params.parse_payload_params(PAYLOAD_PARAMS)
        swapface = SwapFaceProcessing(payload) 

        # create output_file to save image after swapping 
        output_file_name = image_file.replace((".jpg", ".jpeg", ".png"), "_reactor_img2img.png") 
        saved_path = os.path.join(SAVED_PATH_IMG2IMG, output_file_name)

        # swap face for image to image 
        swapface.swap_face_img2img(source_image, 1, saved_path)

    except Exception as e:
        logging.error(f"Error occured when preprocessing image {image_file}: {e}")
        return None

if __name__ == "__main__":
    image_files = [image_file 
                   for image_file in os.listdir(SWAP_IMAGE_PATH) 
                   if image_file.endswith(('.jpg', 'jpeg', '.png', '.gif'))]
    
    with ProcessPoolExecutor(max_workers=4) as executor:
        executor.map(preprocessing, image_files)
