sandwich_orders = ['Chicken', 'Egg', 'Seafood', 'Nutella']
finished_sandwiches = []
while sandwich_orders:
    ongoing_sandwich = sandwich_orders.pop()
    print(" I am making your " + ongoing_sandwich + " sandwich.")
    finished_sandwiches.append(ongoing_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print("I made your " + sandwich + " sandwich.")
