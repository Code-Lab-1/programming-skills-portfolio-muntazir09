ticket_agent = 'What is your age?'
ticket_agent += "\nEnter 'quit' when you are finished. "

while True:
    age = input(ticket_agent)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print(" the ticket is free.")
    elif age < 13:
        print(" the ticket is $10.")
    else:
        print(" the ticket is $15.")

