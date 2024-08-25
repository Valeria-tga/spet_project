# Вставляет текст из буфера обмена - pyperclip.paste()
# Выполняет над текстом некоторые действия
# копирует новый текст в буфер обмена - pyperclip.copy()

import pyperclip as pc

pc.copy('First line \nSecond line \nThree line')

text = pc.paste()
# print(text)


lines = text.split('\n')
for i in range(len(lines)):
    # print(lines[i])
    lines[i] = '* ' + lines[i]
    # print(lines[i])

text = '\n'.join(lines)
print(text)

pc.copy(text)

