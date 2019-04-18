import time
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
input("Now The Browser window will open Login to instagram then close that browser"
      "window  \n  Press the enter button to Start")

options = Options()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-notifications")
options.add_argument('user-data-dir= selenium')
browser = webdriver.Chrome(chrome_options=options, executable_path=r'chromedriver.exe')

browser.get('https://www.instagram.com')