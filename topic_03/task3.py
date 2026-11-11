slovnik = {"ім'я": "Леша", "вік": 20, "місто": "Дніпро"}
print(f"Початковий словник: {slovnik}")

slovnik.update({"професія": "програміст", "вік": 21})
print(f"Після update(): {slovnik}")

print(f"Метод keys(): {slovnik.keys()}")

print(f"Метод values(): {slovnik.values()}")

print(f"Метод items(): {slovnik.items()}")

del slovnik["місто"]
print(f"Після del slovnik['місто']: {slovnik}")

slovnik.clear()
print(f"Після clear(): {slovnik}")