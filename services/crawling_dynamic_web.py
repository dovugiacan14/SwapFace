import os 
import requests 
import re 
import logging 
import traceback
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CrawlingDataDynamicWeb:
    def __init__(self):
        pass  
    
    def craw_data(self, URL):
        try: 
            url_pattern = r'url\("([^"]+)"\)'

            driver = webdriver.Chrome() 
            
            track = 1 

            try: 
                driver.get(URL) 
                
                # wait maximum 10 seconds for the page to load
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "sc-dtInlm"))
                )

                # find all class starting with 'sc-dtInlm'
                elements = driver.find_elements(By.CLASS_NAME, "sc-dtInlm")

                urls = []
                for element in elements:
                    css_property = element.value_of_css_property("background")
                    match = re.search(url_pattern, css_property)
                    if match:
                        url = match.group(1)
                        urls.append(url)
                    else:
                        continue 

                    track += 1
                return urls 
            except Exception as e:
                raise Exception(e)
            finally:
                # close Chrome browser
                driver.quit()

        except TimeoutError as e: 
            logging.error(f"Error occured: The webpage {self.url} took too long to load")
            return None    
        except Exception as e:
            logging.error(f"Error occured when get image: {e}")
            return None
        
    def download(self, url, output_path, index):
        try: 
            response = requests.get(url) 
            if response.status_code >= 200 and response.status_code < 300:
                file_name = f"image_{index}.png"
                file_path = os.path.join(output_path, file_name)
                with open(file_path, "wb") as f:
                    f.write(response.content)
                logging.info(f"Downloaded image {index} successfully")
            else:
                logging.debug(f"save image {index} failed")
                traceback.format_exc()
                return None 

        except Exception as e:
            logging.error(f"Error occured when download image {index}: {e}")
            return None 
