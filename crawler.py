from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from os import walk
from copy import deepcopy
class Crawler():
    def __init__(self, base_url, sub_urls = []):
        self._base_url = base_url
        self._driver = webdriver.Chrome('crawl/chromedriver')
        self.sub_urls = deepcopy(sub_urls)
        self.x_paths = {}
        self._html = None
        self._paths = None

        self._driver.implicitly_wait(3)
    
    def get_url(self, sub_url_index=0):
        if sub_url_index >= len(self.sub_urls):
            print("No sub_url exists for index: {}".format(sub_url_index))
            return
        self._driver.get('{}{}'.format(self._base_url, \
            self.sub_urls[sub_url_index]))
    
    def save_xpath(self, key, path):
        self.x_paths[key] = path
    
    def retrieve_xpath(self, xpath_key):
        if xpath_key not in self.x_paths:
            print("No x_path key exists for key: {}".format(xpath_key))
            return
        self._path = self._driver.find_elements_by_xpath(self.x_paths[xpath_key])
        return self._paths

    def retrieve_html(self):
        page_source = self._driver.page_source
        self._html = BeautifulSoup(page_source, 'html.parser')
        return self._html
    
    def retrive_element(self, el):
        if not el:
            print("element key is empty")
            return
        return self._html.find_all(el)

    def get_current_html(self):
        return self._html
    
    def get_current_paths(self):
        return self._paths