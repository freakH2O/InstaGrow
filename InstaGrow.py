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
    buttons=browser.find_elements_by_tag_name('button')
    for element in buttons:
        print(element.text)

def findAndClickUnfollow():
   g = 0
   try:
    realbut = []
    buttons = browser.find_elements_by_tag_name('button')
    for element in buttons:
        realbut.append(element.text)



    while g < len(realbut):
        if realbut[g] == 'Following':
            buttons[g].click()
            g = len(realbut)
            time.sleep(2)
        else:
            g += 1
   except Exception:
       g += 1

def findAndClickUnfollow2():
   g = 0
   try:
    realbut = []
    buttons = browser.find_elements_by_tag_name('button')
    for element in buttons:
        realbut.append(element.text)



    while g < len(realbut):
        if realbut[g] == 'Unfollow':
            buttons[g].click()
            g = len(realbut)
            time.sleep(2)
        else:
            g += 1
   except Exception:
       g += 1


def ClickAndIndexFollowing(ListToIndexTo):
    browser.find_element_by_xpath('/html/body/span/section/main/div/header/section/ul/li[3]/a').click()
    time.sleep(7)
    a=browser.find_elements_by_tag_name('a')
    hrefs=[]
    for element in a:
      try:
        if element.get_attribute('title') not in hrefs:
            hrefs.append((element.get_attribute('title')))
      except Exception:
          relay=True
    hrefs.pop(0)
    #print(hrefs)
    ListToIndexTo=hrefs 
    return ListToIndexTo
    


seed='meme____machine___'#input("Enter Seed          ")

browser.get("https://www.instagram.com/"+seed)
time.sleep(10)
lista=[]
FinalList=ClickAndIndexFollowing(lista)
FinalList.pop(0)
FinalList.pop(0)
FinalList.pop(0)
FinalList.pop(0)
FinalList.pop(0)
FinalList.pop(0)
FinalList.pop(0)
FinalList.pop(0)
FinalList.pop(0)
FinalList.pop(0)
FinalList.pop(0)
FinalList.pop(0)
FinalList.pop(0)
FinalList.pop(0)
FinalList.pop(0)
FinalList.pop(0)
FinalList.pop(0)
FinalList.pop(0)
FinalList.pop(0)
FinalList.pop(0)
FinalList.pop(0)


#print(FinalList)
RealFinalList=[]

for element in FinalList:
    browser.get("https://www.instagram.com/"+element)
    time.sleep(2)
    relay=True
    while relay== True:   
        if keyboard.is_pressed('right'):  
            relay=False
        elif keyboard.is_pressed('down'):
            RealFinalList.append("https://www.instagram.com/"+element)
            relay=False
print(RealFinalList)
g=0
for element in RealFinalList:
    browser.get(element)
    time.sleep(5)
    try:
        findAndClickFollow()
        time.sleep(3)
        findAndClickFirstPicture()
        time.sleep(3)
        findAndClickLikeButton()
        time.sleep(2)
        browser.get(element)
        time.sleep(3)
        ClickAndIndexFollowing(RealFinalList)
        g+=1
        time.sleep(randint.int(0,10))
        if g>2:
            break





    except:
        relay=True   
        g+=1


with open("array.txt","a") as file:
    for element in RealFinalList:
        file.write(element+'\n')

        

            
        
            
             

    




