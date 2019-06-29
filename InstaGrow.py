
import time
import keyboard  
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-notifications")
options.add_argument('user-data-dir= selenium')
browser = webdriver.Chrome(chrome_options=options, executable_path=r'chromedriver.exe')



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

def FindAndClickFirstPicture():
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

def ClickFollowingAndIndex():
  try: 
    browser.find_element_by_xpath("/html/body/span/section/main/div/header/section/ul/li[3]/a").click()
    time.sleep(5)
    a=browser.find_elements_by_tag_name('a')

    names=[]
    for element in a:
        title=element.get_attribute("title")
        if title!="":
            names.append(title)
    return names
  except Exception:
      relay=True
      
def ClickLikeButton():
  try:  
    spans=browser.find_elements_by_tag_name("span")
    for element in spans:
        if element.get_attribute("aria-label")=="Like":
            element.click()
  except Exception:
       relay=True

#seed=input("Enter the seed account")
browser.get("https://www.instagram.com/syed_zeerak_hussain_gillani")#("https://www.instagram.com/"+seed)
time.sleep(10) 


links=[]
titles=ClickFollowingAndIndex()
for element in titles:
    links.append("https://www.instagram.com/"+element)

print(links)

f=0
while f<100:
    print(f)
    browser.get(links[f])
    relay=False
    while relay==False:
     if keyboard.is_pressed("down"):
        relay=True
        #findAndClickFollow()
        FindAndClickFirstPicture()
        time.sleep(3)
        ClickLikeButton()
        time.sleep(3)
        browser.get(links[f])
        time.sleep(3)
        temp=ClickFollowingAndIndex()
        try:
            for element in temp:
                links.append("https://www.instagram.com/"+element)
        except Exception:
            continue
        time.sleep(random.randint(5,11))
        f+=1
     if keyboard.is_pressed("right"):
        relay=True
        f+=1

 
 

    

