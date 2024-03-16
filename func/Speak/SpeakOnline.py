#pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from time import sleep
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless=new')
chrome_options.headless = True
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
website = r"https://ttsmp3.com/text-to-speech/British2English/"
driver.get(website)
Buttonselection = Select(driver.find_element(by=By.ID, value='sprachwahl'))
Buttonselection.select_by_visible_text("British English / Brian")

def Speak(*args):
    Text=""
    for i in args:
        Text+=i
    lengthoftext = len(str(Text))
    if lengthoftext == 0:
        pass
    else:
        print("")
        print(Fore.CYAN+Text)
        print("")
        Data = str(Text)
        driver.find_element(By.ID, "voicetext").send_keys(Data)
        driver.find_element(By.ID, value="vorlesenbutton").click()
        driver.find_element(By.ID, "voicetext").clear()
        if lengthoftext >= 30:
            sleep(7)
        elif lengthoftext >= 40:
            sleep(8)
        elif lengthoftext >= 55:
            sleep(12)
        elif lengthoftext >= 70:
            sleep(14)
        elif lengthoftext >= 108:
            sleep(16)
        elif lengthoftext >= 120:
            sleep(18)
        else:
            sleep(2)
