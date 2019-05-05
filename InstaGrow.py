import time
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def tryy(x):
    relay=True
    while relay==True:
        try:
            x.click()
            relay=False
        except Exception:
            continue

def findAndClickFollow():
   g = 0
   try:
    realbut = []
    buttons = browser.find_elements_by_tag_name('button')
    for element in buttons:
        realbut.append(element.text)

    while g < len(realbut):
        if realbut[g] == 'Follow':
            buttons[g].click()
            g = len(realbut)
            time.sleep(2)
        else:
            g += 1
   except Exception:
       g += 1

def findAndClickFirstPicture():
    anchors = browser.find_elements_by_tag_name('a')
    g = 0
    while g < len(anchors):
        try:
            href = anchors[g].get_attribute('href')
            if '/p/' in href:
                anchors[g].click()
                g = len(anchors)
            else:
                g += 1
        except Exception:
            g += 1

def findAndClickLikeButton():
    try:
        spans = browser.find_elements_by_tag_name('span')
        for element in spans:
            if element.get_attribute('aria-label') == "Like":
                element.click()
    except Exception:
        relay=True

def findAndIndexNewPeople(ListToIndexTo):
  try:
    linka = browser.find_elements_by_tag_name('a')
    temp = []
    for element in linka:
        if (element.get_attribute('href') in temp) and ( element.get_attribute('href') not in ListToIndexTo) and '/p/' not in element.get_attribute('href'):
            ListToIndexTo.append(element.get_attribute('href'))
            print("Just Indexed "+element.get_attribute('href'))
        else:
            temp.append(element.get_attribute('href'))
  except Exception:
      relay=True
base=input("Enter The base account from which the automation will spread the \n Base Account should not be private and have followers and communitty \n similar to your target audience")
options = Options()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-notifications")
options.add_argument('user-data-dir= selenium')
browser = webdriver.Chrome(chrome_options=options, executable_path=r'chromedriver.exe')

links=[]
links.append('https://www.instagram.com/'+base)
done=[]
for element in links:
    if element not in done:
        browser.get(element)
        time.sleep(3)
        choiceToFollow=random.randint(0,100)
        if choiceToFollow>90:
            findAndClickFollow()
        findAndClickFirstPicture()
        time.sleep(2)
        findAndClickLikeButton()
        time.sleep(2)
        findAndIndexNewPeople(links)
        time.sleep(random.randint(15, 30))
        done.append(element)






