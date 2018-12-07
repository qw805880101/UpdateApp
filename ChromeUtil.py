# -*- coding:utf-8 -*-
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

__author__ = 'Tianc'

profile_dir = 'C:\\Users\\tc\\AppData\\Local\\Google\\Chrome\\User Data'  # 对应你的chrome的用户数据存放路径
chrome_options = Options()
chrome_options.add_argument("user-data-dir=" + os.path.abspath(profile_dir))
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
prefs = {
    "profile.managed_default_content_settings.images": 1,
    "profile.content_settings.plugin_whitelist.adobe-flash-player": 1,
    "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 1,

}

chrome_options.add_experimental_option('prefs', prefs)
# chrome_options.add_argument('--headless')
try:
    browser = webdriver.Chrome(executable_path=r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe',
                               chrome_options=chrome_options)
except Exception as e:
    print(e)
    print('请关闭所有浏览器~')

# browser = webdriver.Chrome()
# browser.maximize_window()


def set_url(channel_url):
    browser.get(channel_url)
    return browser
