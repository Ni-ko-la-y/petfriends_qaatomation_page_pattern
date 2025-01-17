import os
import pickle

from pages.base import WebPage


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://petfriends.skillfactory.ru/'

        super().__init__(web_driver, url)
        with open('my_cookies.txt', 'rb') as cookiesfile:
            cookies = pickle.load(cookiesfile)
            for cookie in cookies:
                web_driver.add_cookie(cookie)
            web_driver.refresh()
