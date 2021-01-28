text = list(input("введите текст: "))
key = input("введите ключ: ")

for symbol in range(len(text)):
    try: 
        text[symbol] = chr(ord(text[symbol]) ^ int(key))
    except ValueError:
         text[symbol] = chr(ord(text[symbol]) ^ ord(key))
print("зашифрованный ответ:","".join(text))
text = list(input("введите зашифрованный ответ для расшифровки:"))
key = input("введите повторный ключ: ")

for symbol in range(len(text)):
    try: 
        text[symbol] = chr(ord(text[symbol]) ^ int(key))
    except ValueError:
         text[symbol] = chr(ord(text[symbol]) ^ ord(key))
print("расшифрованный ответ:","".join(text))
