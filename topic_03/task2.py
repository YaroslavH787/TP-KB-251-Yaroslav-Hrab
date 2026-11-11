spisok = [10, 9, 2, 9, 0]

print(f"Початковий список: {spisok}")

spisok.append(15)
print(f"Після append(15): {spisok}")

spisok.extend([40, 50])
print(f"Після extend([40, 50]): {spisok}")

spisok.insert(2, 99)
print(f"Після insert(2, 99): {spisok}")

spisok.remove(9)
print(f"Після remove(8): {spisok}")

copied_spisok = spisok.copy()
print(f"Копія списку: {copied_spisok}")

spisok.sort()
print(f"Після sort(): {spisok}")

spisok.reverse()
print(f"Після reverse(): {spisok}")

spisok.clear()
print(f"Після clear(): {spisok}")

print(f"скопійований раніше список: {copied_spisok}")