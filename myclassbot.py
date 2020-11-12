import time
import json
import random
import keyboard
import pyautogui
from pyautogui import *
from selenium import webdriver
import win32api
import win32con


class MyClassBot:
    def __init__ (self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://myclass.lpu.in")
        time.sleep(3)
        self.driver.find_element_by_xpath("//input[@name=\"i\"]").send_keys('regnohere')
        self.driver.find_element_by_xpath("//input[@name=\"p\"]").send_keys('passwordhere')        
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(3)
        self.driver.find_element_by_link_text('View Classes/Meetings').click()
        self.flag=0
        time.sleep(3)

    def Click(self,x,y):
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        time.sleep(0.1)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
    def Join(self):
        self.pic=pyautogui.screenshot(region=(100,300,1900,600))
        self.pic.save('file.jpg')
        self.width,self.height=self.pic.size
        for x in range(0,self.width,5):
            for y in range(0,self.height,5):
                self.r,self.g,self.b = self.pic.getpixel((x,y))
           
                if(self.r==0):
                    if(self.g==128 and self.b==0):
                        self.Click(x+100,y+300)
                        self.flag=1
                        break
            if(self.flag):
                break
        time.sleep(3)
        self.driver.find_element_by_link_text('Join').click()
        time.sleep(12)
        #for listen mode
        self.Click(1035,616) #1035, 616
        
        # ----------------------------for mic------------------------------------#
        #self.driver.find_element(By.CSS_SELECTOR, ".icon-bbb-unmute").click()
        #time.sleep(2)
        #self.driver.find_element(By.CSS_SELECTOR, ".icon-bbb-thumbs_up").click()



Bot=MyClassBot()
Bot.Join()

time.sleep(3000)


