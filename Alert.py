import pyautogui

pyautogui.alert("selam sana...",button="sana da selam...")

pyautogui.confirm("devam etmek ister misin?",buttons=["evet","hayır"])

name=pyautogui.prompt("adınızı giriniz...")

print(name)

pyautogui.password("{0}şifrenizi giriniz : ",name)

