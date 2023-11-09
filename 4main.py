n = int(input("Введіть n: "))
text = input("Введіть рядок: ")
upper_text = text[:n].upper() + text[n:]
print("Результат:", upper_text)
