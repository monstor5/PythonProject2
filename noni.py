from gtts import gTTS
from playsound import playsound
txt = f'{str(input())}'
print('1. "en" Английский язык.     2. "ru" Русский язык"')
language = f'{str(input())}'

obj = gTTS(text = txt, lang = language, slow = False)

obj.save("test.mp3")
playsound("test.mp3")