import pyautogui
import time
import pyperclip
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY=os.getenv("API_KEY")

client = OpenAI(api_key=API_KEY)

pyautogui.click(1072 , 1054)
time.sleep(2)

pyautogui.moveTo(706 , 269)
pyautogui.dragTo(706 , 900 , duration=2 , button='left')

pyautogui.hotkey('ctrl' , 'c')
pyautogui.click(706 , 269)
time.sleep(2)

chat_history = pyperclip.paste()

print(chat_history)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a person named meet who speaks hindi, gujrati as well as english. you are from india and you are a coder. You analyze chat history and respond like meet. output should be the next chat response as meet"},
        {
            "role": "user", "content": chat_history
        }
    ]
)

response = completion.choices[0].message.content
pyperclip.copy(response)

pyautogui.click(1000 , 960)
time.sleep(1)

pyautogui.hotkey('ctrl' , 'v')
time.sleep(1)

pyautogui.press('enter')