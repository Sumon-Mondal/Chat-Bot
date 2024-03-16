from func.Osrc.Chat import Chat
from func.Speak.SpeakOffline import Speak
from func.Listen.ListenJs import Listen
from func.Osrc.DataOnline import Online_Scraper
# from llm.online_chat import Chat

if __name__ == "__main__":
    while 1:
        Q = Listen()
        QL = Q.lower()
        GetChat = Chat(QL)
        GetData = Online_Scraper(Q)
        GetInfo = Chat(Q)
        # reply = ChatGpt(Q)
        # Speak(reply)
        if GetData != None:
            Speak(GetData)
        # elif GetChat != None:
        #     Speak(GetChat)
        else:
            Speak(GetChat)