# join обернений до метода split, він поєднує ел-ти. Тобто він приймає обєкт (list або tuple) і потім ітерує цей обєкт.
# Обовязкова умова, що цей обєкт має бути рядком (str). 

lst = [1, 2, 3, 4]

print(",".join(str(i) for i in lst))    # в лапках "" ставимо ел-т яким розбиваємо наші обєкти - 1,2,3,4
print("".join(str(i) for i in lst))     # якщо в лапках нічого не ставимо - 1234


new_lst = []

for i in lst:
    new_lst.append(str(i))
    
print(", ".join(new_lst))    