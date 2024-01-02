from concurrent.futures import ProcessPoolExecutor 
from services.crawling_dynamic_web import CrawlingDataDynamicWeb
from config.service_config import URL, SAVED_DOWNLOAD_PATH

def main():
    CDW = CrawlingDataDynamicWeb()

    if URL is not None: 
        urls = CDW.craw_data(URL)

        with ProcessPoolExecutor(max_workers= 4) as executor:
            for index, url in enumerate(urls, start= 1):
                executor.submit(CDW.download,url, SAVED_DOWNLOAD_PATH, index)

if __name__ == "__main__":
    main()