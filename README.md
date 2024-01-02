# Stable Diffiusion - Swap Face Extension 

## **OVERVIEW**
In this repository, we provide a souce code that perform face swapping feature, leveraging the cutting-edge text-to-image and image-to-image capabilities of Stable Diffusion through a streamlined API intergration. 

## **FEATURES**

* **Effortless face swapping:** seamless integration of Stable Diffusion'API for effortless face manupilation. 

* **Text-to-image face swapping:** edit faces or backgrouds in existing images based on descriptive text. 

* **Image-to-image face swapping:** edit existing images with precision face swaps.

* **Crawl data from dynamic web:** we provide an example code that helps to crawl images data in dynamic web. 

## **PRE-REQUISITS** 
You must have a GPU with CUDA support in order to run the code. 

First, you start Stable Diffusion Web Ui and install **ReActor Extension** following URL:  ```https://github.com/Gourieff/sd-webui-reactor```. The instructions for installing the extension can be found at [**here**](https://www.nextdiffusion.ai/tutorials/how-to-face-swap-in-stable-diffusion-with-reactor-extension).

If any of these packages are not installed on your computer, you can install them using the supplied requirements.txt file: 
>        pip install -r requirements.txt

Then, download the pre-trained model at [inswapper_128.onnx
](https://huggingface.co/ezioruan/inswapper_128.onnx/tree/main). For a quick model download, run this command in your terminal:  
>        wget https://huggingface.co/ezioruan/inswapper_128.onnx

Remember to set the `MODEL_PATH` variable correctly in `config\service_config.py` for the application to find and use the model.

## **DEMO** 
### Crawl Image Data
1. Set the site you want to crawl data in `URL` variable correctly in `config\service_config.py`.

2. Ensure you have installed `chromedriver` in `\usr\local\bin` on Linux or MacOS, or in `C:\Windows\System32` on Window. 

3. Ensure `chromedriver` version that you installed have to be compatible with your `Chrome Browser` version in your system. 

4. **Run:**
>       python crawling.py

### Text-to-Image Face Swapping
1. Point the `SWAP_IMAGE_PATH` variable in `config/service_config.py` to the folder containing the images you'd like to face-swap.

2. Enter **prompt** and **negative prompt** in `PROMPT` and `NEGATIVE_PROMPT` variable correctly, in order that in `config\service_config.py`.

3. Set the `SAVED_PATH_TXT2IMG` variable in `config/service_config.py` to the location where you want to save your face-swapped images.

4. **Run:** 
>       python swapface_txt2img.py

### Image-to-Image Face Swapping 
1. Point the `SWAP_IMAGE_PATH` variable in `config/service_config.py` to the folder containing the images you'd like to face-swap.

2. Set the `SOURCE_IMAGE` variable to the folder holding the face you wish to transplant.

3. Set the `SAVED_PATH_IMG2IMG` variable in `config/service_config.py` to the location where you want to save your face-swapped images.

4. **Run:** 
>       python swapface_img2img.py




