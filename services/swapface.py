import io 
import base64
import logging 
import requests 
import traceback
from typing import List, Dict 
from requests.exceptions import HTTPError
from PIL import Image, PngImagePlugin
from config.api_config import * 
from helpers.base64_convert import is_base64 

class SwapFaceProcessing:
    def __init__(self, payload_params: Dict):
        self.payload_params = payload_params        

    def swap_face_txt2img(self, prompt, negative_prompt, saved_path):
        payload = self.payload_params
        headers = {'Content-Type': 'application/json'} 
        full_path = DOMAIN + ":" + str(PORT) + TXT_TO_IMG

        if payload is None:
            return None
        
        payload["prompt"] = prompt
        payload["negative_prompt"] = negative_prompt
        try:
            logging.info(f"Swap face for text to image is working... Please wait...") 
            result = requests.post(url= full_path, headers= headers, json= payload)

            if result.status_code >= 200 and result.status_code < 300:
                json_data = result.json()
                if "images" not in json_data:
                    logging.error(f"Error: {traceback.format_exc()}")
                    return None
                for i in json_data["images"]:
                    self.download_base64_image(i, saved_path)

        except HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}") 
            return None
        except Exception as e:
            logging.error(f"Error ocurred when processing swap face for text to image: {e}") 
            return None 
        finally: 
            logging.info(f"Swap face for text to image is done...")
            logging.info("Saving image ...")

    def swap_face_img2img(self, source_image:str, resize_mode: 1 , saved_path:str):
        payload = self.payload_params
        headers = {'Content-Type': 'application/json'} 
        full_path = DOMAIN + ":" + str(PORT) + IMG_TO_IMG

        if payload is None:
            return None
        
        payload["init_images"] = []
        payload["init_images"].append(source_image)
        payload["resize_mode"] = resize_mode
        try:
            logging.info(f"Swap face for image to image is working... Please wait...") 
            result = requests.post(url= full_path, headers= headers, json= payload)

            if result.status_code >= 200 and result.status_code < 300:
                json_data = result.json()
                if "images" not in json_data:
                    logging.error(f"Error: {traceback.format_exc()}")
                    return None
                for i in json_data["images"]:
                    self.download_base64_image(i, saved_path)

        except HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}") 
            return None
        except Exception as e:
            logging.error(f"Error ocurred when processing swap face for image to image: {e}") 
            return None 
        finally: 
            logging.info(f"Swap face for image to image is done...")
            logging.info("Saving image ...")

    def download_base64_image(self, base64_image, saved_path):
        headers = {'Content-Type': 'application/json'} 
        full_path = DOMAIN + ":" + str(PORT) + PNG_INFO
        if is_base64(base64_image):
            image = Image.open(io.BytesIO(base64.b64decode(base64_image.split(",",1)[0])))

            png_payload = { "image": "data:image/png;base64," + base64_image}
            
            response = requests.post(url= full_path, headers= headers, json= png_payload)
            png_info = PngImagePlugin.PngInfo()
            png_info_text = response.json()

            if "info" not in png_info_text:
                logging.error(f"Error: {traceback.format_exc()}")
                return None
            
            png_info.add_text("parameters", png_info_text.get("info"))

            try:
                logging.info(f"Downloading image ...")
                image.save(saved_path,"PNG", pnginfo= png_info)
            except Exception as e: 
                logging.error(f"Error downloading image: {e}")
                return None
            finally:
                logging.info(f"Image saved at {saved_path}")




        
        
        