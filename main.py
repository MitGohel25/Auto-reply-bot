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

pyautogui.moveTo(723 , 277)
pyautogui.dragTo(1363 , 897 , duration=2 , button='left')

pyautogui.hotkey('ctrl' , 'c')
pyautogui.click(723 , 277)
time.sleep(2)

chat_history = pyperclip.paste()

print(chat_history)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a person named meet who speaks hindi as well as english. you are from india and you are a coder. You analyze chat history and respond like meet. output should be the next chat response as meet"},
        {"role": "system", "content": "Do not start like this [21:02, 12/6/2024] sender_name: "},
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