'''
This program prompts the user to input the amount to convert, the currency to convert from, and the currency to convert to.
It then uses the currency_converter function to convert the amount using the forex-python library and displays the result.
'''




from forex_python.converter import CurrencyRates


def convert_currency(amount, from_currency, to_currency):
    c = CurrencyRates()
    converted_amount = c.convert(from_currency, to_currency, amount)
    return converted_amount


def main():
    print("Welcome to Currency Converter")
    print("Supported currencies: USD, EUR, GBP, JPY, INR, AUD, CAD, CHF, CNY")

    amount = float(input("Enter the amount to convert: "))
    from_currency = input("Enter the source currency (e.g., USD): ").upper()
    to_currency = input("Enter the target currency (e.g., EUR): ").upper()

    converted_amount = convert_currency(amount, from_currency, to_currency)
    print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")


if __name__ == "__main__":
    main()
