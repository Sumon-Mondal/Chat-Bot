import os
import pygame

def Speak(data):
    command = f'edge-tts --voice "en-CA-LiamNeural" --pitch=+5Hz --rate=+22% --text "{data}" --write-media "temp/data.mp3" '
    os.system(command)
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(r"temp/data.mp3")
    try:
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    except Exception as e:
        print(e)
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()

if __name__=="__main__":
    Speak("hii my name is jarvis")