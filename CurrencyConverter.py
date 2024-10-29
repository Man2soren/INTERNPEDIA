import requests

# Function to fetch live exchange rates
def get_exchange_rate(api_key, source_currency, target_currency):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{source_currency}/{target_currency}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        data = response.json()
        if data['result'] == 'success':
            return data['conversion_rate']
        else:
            print("Error fetching exchange rate:", data.get('error-type', 'Unknown error'))
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: Unable to retrieve data. {e}")
        return None

# Function for converting currency
def convert_currency(api_key, amount, source_currency, target_currency):
    rate = get_exchange_rate(api_key, source_currency, target_currency)
    if rate:
        converted_amount = amount * rate
        return converted_amount
    else:
        return None

# Function to get user input and handle multiple conversions
def currency_converter():
    api_key = "aabbd3d42a5f6014d162da5e"  
    currencies = ['INR', 'USD', 'EUR', 'GBP', 'JPY', 'AUD', 'CAD']  # List of supported currencies
    
    while True:
        print("\nAvailable currencies:", ", ".join(currencies))
        
        source_currency = input("Enter source currency: ").upper()
        if source_currency not in currencies:
            print(f"Invalid currency. Choose from {currencies}")
            continue
        
        target_currency = input("Enter target currency: ").upper()
        if target_currency not in currencies:
            print(f"Invalid currency. Choose from {currencies}")
            continue
        
        try:
            amount = float(input("Enter amount to convert: "))
        except ValueError:
            print("Invalid amount. Please enter a valid number.")
            continue
        
        converted_amount = convert_currency(api_key, amount, source_currency, target_currency)
        
        if converted_amount:
            print(f"{amount} {source_currency} is equal to {converted_amount:.2f} {target_currency}")
        else:
            print("Conversion failed.")
        
        # Ask if the user wants to do another conversion
        repeat = input("\nDo you want to perform another conversion? (y/n): ").lower()
        if repeat != 'y':
            print("Exiting the converter. Thank you!")
            break

# Main entry point for the program
if __name__ == "__main__":
    currency_converter()
