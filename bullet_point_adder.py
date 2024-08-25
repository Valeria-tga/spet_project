# Вставляет текст из буфера обмена - pyperclip.paste()
# Выполняет над текстом некоторые действия
# копирует новый текст в буфер обмена - pyperclip.copy()

import pyperclip

text = pyperclip.paste()

#Делим строки и добавляем звездочки

pyperclip.copy(text)
print(pyperclip.copy(text))
