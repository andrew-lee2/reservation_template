from django.conf import settings
import logging
from selenium import webdriver
from retry import retry


logger = logging.getLogger(__name__)


class WebDriverSingleton(object):
    _instance = None

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = WebDriverSingleton()
        return cls._instance

    @retry(delay=1, tries=5)
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        driver_path = settings.DRIVER_PATH

        if settings.DEV_ENV:
            chrome_driver = webdriver.Chrome(driver_path, chrome_options=options)
        else:
            options.binary_location = driver_path
            chrome_driver = webdriver.Chrome(executable_path="chromedriver", chrome_options=options)

        logger.info('Initialized web driver')
        self.chrome_driver = chrome_driver

    def shutdown(self):
        self.chrome_driver.close()
        logger.info('Shutting down web driver')
