# method STARTSWITH

text = "hello world"
text2 = "world hello"

lst = [text, text2]

print(text.startswith("he")) # перевірили чи наш рядок починається з заданих ел-ів (he) - True

for text in lst:
    print(text.startswith(("he", "wo"))) #перевірили входження символів послідовно
    
    
    # endwith зворотній метод до startswith, тобто перевіряє входження символу з кінця рядка
    