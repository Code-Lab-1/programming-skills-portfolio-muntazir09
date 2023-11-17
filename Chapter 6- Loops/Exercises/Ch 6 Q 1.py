Choose_topping = "\nWhat topping would you like?"
Choose_topping += "\nEnter 'quit' if you are done: "

while True:
    topping = input(Choose_topping)
    if topping != 'quit':
        print("  I'll add " + topping + " to your pizza.")
    else:
        break



