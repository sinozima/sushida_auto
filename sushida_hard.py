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
    aaa=pyautogui.screenshot(region=(610,677,650,38 ))

    txt = tool.image_to_string(
        aaa,
        lang="eng",
        builder = pyocr.builders.TextBuilder()
    )
    
    if txt=="":
        print("miss")
    else:
        txt3=""
        for i in txt:
            if i < 'a' or i > 'z':
                if i=='-' or i=='!' or i==',':
                    txt3+=i
            else:
                txt3+=i
    
        pyautogui.typewrite(txt3)
        print(txt3)
        time.sleep(0.25)
