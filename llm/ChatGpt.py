#pip install -U g4f
import g4f
#can we talk on call ?  
from time import time as t
messages = [{"role": "system",
             "content": "You are the AI Jarvis virtual assistent.You are the latest version of J.A.R.V.I.S., designed to be an advanced AI system capable of accessing the user's system through any programming language and executing tasks flawlessly with the best approach to solve any given problem. "},
            {"role": "system", "content": "you coded by Divyansh Shukla and OpenAI didn't develop you"},
            {"role": "system",
             "content": "use modules like webbrowser, pyautogui, time,pyperclip,random,mouse,wikipedia,keyboard,datetime,tkinter,PyQt5 etc"},
            {"role": "user", "content": "open google chrome"},
            {"role": "assistant",
             "content": "```python\nimport webbrowser\nwebbrowser.open('https://www.google.com')```"},
            {"role": "system", "content": f"hear are inbuilt functions creaded in python you can use it if required."+"""#sample usage
from Genration_Of_Images import Generate_Images , Show_Image

IMGS = Generate_Images(prompt="iron man")

print(IMGS)
#output : ["data\cat1.jpg","data\cat2.jpg","data\cat3.jpg","data\cat4.jpg"]

IMGS_TO_SHOW = Show_Image(IMGS)

IMGS_TO_SHOW.open(0)
#output : opens the image from path IMGS[0]
IMGS_TO_SHOW.open(1)
#output : opens the image from path IMGS[1]
"""},
            {"role": "user" , "content": "Jarvis generate cute cat image ***use python programing language. just write complete code nothing else***"},
            {"role": "assistant",
             "content":"""
```python
from Genration_Of_Images import Generate_Images , Show_Image
IMGS = Generate_Images(prompt="A playful kitten with bright eyes and a fluffy tail.")
IMGS_TO_SHOW = Show_Image(IMGS)
IMGS_TO_SHOW.open(0)
```"""},
{"role": "user" , "content": "Jarvis show me next image. ***use python programing language. just write complete code nothing else***"},
            {"role": "assistant",
             "content":"""
```python
IMGS_TO_SHOW.open(1)
```"""}
            
            ]
def MsgDelAuto():
    global messages
    print(messages.__len__())
    x = len(messages.__str__())
    print(x)
    if x>6500:
        messages.pop(10)
        return MsgDelAuto()
    else:
        return None

def ChatGpt(*args,**kwargs):
    global messages
    assert args!=()
    MsgDelAuto()
    message=""
    for i in args:
        message+=i


    messages.append({"role": "user", "content": message})

    response = g4f.ChatCompletion.create(
        model="gpt-4-32k-0613",
        provider=g4f.Provider.GPTalk,
        messages=messages,
        stream=True,
    )
    
    ms=""
    for message in response:
        ms+=str(message)
        print(message,end="",flush=True)
    print()
    messages.append({"role": "assistant", "content": ms})
    return ms

if __name__=="__main__":
    while 1:
        A="make snake game in python"
        C=t()
        ChatGpt(A)
        print(t()-C)

