import requests

allowed = ["EUR", "USD", "PNL"]

currency = input("Введіть валюту (EUR, USD, PLN): ").upper()

if currency not in allowed:
    print("Помилка: підтримуються лише валюти EUR, USD та PLN")
else:
    try:
        amount = float(input(f"Введіть суму в {currency}: "))
        if amount < 0:
            print("Помилка: сума не може бути від'ємною")
        else:
            url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={currency}&json"
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            data = response.json()
            rate = data[0]["rate"]
            result = amount * rate

            print(f"Курс НБУ: 1 {currency} = {rate:.2f} UAH")
            print(f"Результат: {amount:.2f} {currency} = {result:.2f} UAH")

    except ValueError:
        print("Помилка: введіть коректне число")
    except requests.RequestException as e:
        print(f"Помилка при запиті до API НБУ: {e}")