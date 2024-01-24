#Import necessary modules
from forex_python.converter import CurrencyRates #Online currency rates
import tkinter as tk
from tkinter import ttk

def convert_currency():
    try:
        amount = float(amount_entry.get())
    except ValueError:
        result_label.config(text="Please enter a valid numeric amount")
        return #Prevents user from entering anything else than numbers

    from_currency = from_currency_combobox.get().split(" - ")[0]
    to_currency = to_currency_combobox.get().split(" - ")[0]

    if from_currency not in currency_names or to_currency not in currency_names:
        result_label.config(text="Please select valid currency codes")
        return #Prevents user from entering non-valid currencies 
    
    c = CurrencyRates()
    exchange_rate = c.get_rate(from_currency, to_currency)
    converted_amount = amount * exchange_rate

    # Shows the result of conversion
    result_label.config(text=f"{amount} {currency_names[from_currency]} is equal to {converted_amount:.2f} {currency_names[to_currency]}")

# Create the main window
window = tk.Tk()
window.geometry("400x200")
window.title("Currency Exchange Program")

# Currency dictionary
currency_names = {
    "EUR": "Euro",
    "USD": "United States dollar",
    "AUD": "Australian dollar",
    "JPY": "Japanese yen",
    "GBP": "British pound",
    "NZD": "New Zealand dollar",
    "ZAR": "South African rand",
    "DKK": "Danish krone",
    "RUB": "Russian rouble",
    "INR": "Indian rupee",
    "HKD": "Hong Kong dollar",
    "CHF": "Swiss franc",
    "CAD": "Canadian dollar",
    "NOK": "Norwegian krone",
    "ILS": "Israeli new shekel"    
}


# Currency codes and names for dropdowns
currency_options = [f"{code} - {name}" for code, name in currency_names.items()]

# Amount entry
amount_label = tk.Label(window, text="Enter the amount:")
amount_label.pack()
amount_entry = tk.Entry(window)
amount_entry.pack()

# From currency dropdown menu
from_currency_label = tk.Label(window, text="From currency:")
from_currency_label.pack()
from_currency_combobox = ttk.Combobox(window, values=currency_options, state="readonly")
from_currency_combobox.set("USD")
from_currency_combobox.pack()

# To currency dropdown menu
to_currency_label = tk.Label(window, text="To currency:")
to_currency_label.pack()
to_currency_combobox = ttk.Combobox(window, values=currency_options, state="readonly")
to_currency_combobox.set("EUR")
to_currency_combobox.pack()

# Convert button
convert_button = tk.Button(window, text="Convert", command=convert_currency)
convert_button.pack()

# Result label
result_label = tk.Label(window, text="")
result_label.pack()

# Run the program
window.mainloop()