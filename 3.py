sentence = input("Введіть речення: ")

words = sentence.split()

count = 0
for word in words:
    if word.endswith("р") or word.endswith("р."):
        count += 1

print(f"Кількість слів, які закінчуються на літеру 'р': {count}")
