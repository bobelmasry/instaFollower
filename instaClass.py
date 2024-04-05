import pydirectinput
from PIL import Image, ImageGrab
import time
import random
import pyautogui
from datetime import datetime

BLUE = (0,149,246)

class Page:
    def __init__(self, BoxX, BoxY, width, totalHeight, individualHeight, pageVar):
        self.BoxX = BoxX
        self.BoxY = BoxY
        self.width = width
        self.totalHeight = totalHeight
        self.individualHeight = individualHeight
        self.pageVar = pageVar
    
    def hasFollow(self, imagePath):
        im = Image.open(imagePath)
        pix = im.load()
        for y in range(int(self.BoxY), int(self.BoxY + self.totalHeight)):
            for x in range(int(self.BoxX), int(self.BoxX + self.width)):
                value = pix[x, y]
                if value == BLUE:
                    return [True, (x,y)]
    
        return [False, value]
    
    def clickFollow(self, x, y):
        pyautogui.moveTo(x, y)
        pyautogui.click()
        time_sleepRand = round(random.uniform(5, 7), 2)
        time.sleep(time_sleepRand)
        screenshot = ImageGrab.grab()
        screenshot.save(f'insta-image{self.pageVar}.png', 'PNG')
    
    def scrollDown(self):
        pydirectinput.press('down')
        pydirectinput.press('down')
        pydirectinput.press('down')

    def completeFollow(self):
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        followCount = 0
        screenshot = ImageGrab.grab()
        screenshot.save(f'insta-image{self.pageVar}.png', 'PNG')
        time_sleepRand = round(random.uniform(5, 7), 2)
        time.sleep(time_sleepRand)
        random_follow = random.randint(6, 8)
        while followCount < random_follow:
            if self.hasFollow(f'insta-image{self.pageVar}.png')[0]:
                self.clickFollow(self.hasFollow(f'insta-image{self.pageVar}.png')[1][0], self.hasFollow(f'insta-image{self.pageVar}.png')[1][1]) # x and y coordinates
                followCount += 1
                screenshot = ImageGrab.grab()
                screenshot.save(f'insta-image{self.pageVar}.png', 'PNG')
            else:
                self.scrollDown()
                screenshot = ImageGrab.grab()
                screenshot.save(f'insta-image{self.pageVar}.png', 'PNG')
        print(f"followed {followCount} people by: {current_time} in page {self.pageVar}")

page1 = Page(550, 240, 120, 300, 40, 1)
page2 = Page(1520, 240, 120, 300, 40, 2)

while True:
    random_time = random.randint(2600,3200)
    page1.completeFollow()
    time.sleep(200)
    #page2.completeFollow()
    time.sleep(random_time)