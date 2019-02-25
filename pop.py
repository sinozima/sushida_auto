from PIL import Image
import sys
import pyocr 
import pyocr.builders
import pyautogui
import time

tools = pyocr.get_available_tools()


tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))

langs = tool.get_available_languages()
print("Available languages: %s" % ", ".join(langs))

lang = langs[0]
print("Will use lang '%s'" % (lang))

txt2 = "kalejfap"

while True:
    txt = tool.image_to_string(
        pyautogui.screenshot(region=(400,810,900,50 )),
        lang="eng",
        builder = pyocr.builders.TextBuilder()
    )
    
   
    
    pyautogui.typewrite(txt)
    print(txt)