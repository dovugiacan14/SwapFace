import logging 
import json
from base64_convert import pil_to_base64

class GETPARAMS:
    def __init__(self, swap_image_file, model_path, reactor_params):
        self.swap_image_file = swap_image_file
        self.model_path = model_path
        self.reactor_params = reactor_params

    def parse_payload_params(self, payload_params):
        try:
            params = json.load(open(payload_params)) 
            if self.parse_reactor_params is None: 
                return None 
            params["alwayson_scripts"] = {"reactor":{"args":self.parse_reactor_params()}}
            return params
        
        except Exception as e:
            logging.error(f"Error parsing payload params: {e}")
            return None
        
    def parse_reactor_params(self):
        try:
            params = json.load(open(self.reactor_params))
            
            data = []
            data.append(pil_to_base64(self.swap_image_file))
            if "enable_reactor" in params:
                data.append(params["enable_reactor"])
            if  "seperated_face_swap_source_image" in params:
                data.append(params["seperated_face_swap_source_image"])
            if "seperated_face_swap_target_image" in params:
                data.append(params["seperated_face_swap_target_image"])
            data.append(self.model_path)
            if "restore_face_mode" in params:
                if params["restore_face_mode"] in ("CodeFormer", "GFPGAN", None):
                    data.append(params["restore_face_mode"])
            if "restore_visibility_value" in params:
                data.append(params["restore_visibility_value"])
            if "restore_face" in params:
                data.append(params["restore_face"])
            if "upscaler" in params:
                data.append(params["upscaler"])
            if "upscaler_value" in params:
                upscaler_value = params["upscaler_value"] 
                if isinstance(upscaler_value, int) and upscaler_value >= 1 and upscaler_value <= 5:
                    data.append(params["upscaler_value"])
            data.append(1)
            if  "swap_in_source_image"  in params:
                data.append(params["swap_in_source_image"])
            if "swap_in_generated_image" in params:
                data.append(params["swap_in_generated_image"])
            data.append(1)
            if "in_gender_detection" in params: 
                in_gender_detection = params['in_gender_detection']
                if in_gender_detection == 0 or in_gender_detection == 1 or in_gender_detection == 2:
                    data.append(in_gender_detection)
            if "out_gender_detection" in params:
                out_gender_detection = params["out_gender_detection"]
                if out_gender_detection == 0 or out_gender_detection == 1 or out_gender_detection ==2:
                    data.append(out_gender_detection)
            if  "save_image_before_swapping" in params:
                data.append(params["save_image_before_swapping"])
            if "codeformer_weight" in params:
                codeformer_weight = params["codeformer_weight"]
                if codeformer_weight >= 0 and codeformer_weight <= 1:
                    data.append(params["codeformer_weight"])
            if "source_image_hash_check" in params:
                data.append(params["source_image_hash_check"])
            if "target_image_hash_check" in params:
                data.append(params["target_image_hash_check"])
            return data
        
        except Exception as e:
            logging.error(f"Error parsing reactor params: {e}")
            return None 


