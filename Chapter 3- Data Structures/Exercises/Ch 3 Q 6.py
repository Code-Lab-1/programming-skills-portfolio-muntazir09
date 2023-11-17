## Exercise 6: Shrinking Guest List

Friends = ['Ayaz ', 'Mahdi ', 'Danish ', 'Hadi ']
print("Hello guys only two people can be invited for the dinner.")
print(Friends[2] + "I am really sorry I can't invite for the dinner.")
Friends.pop(2)
print(Friends)

print(Friends[1] + "I am really sorry I can't invite for the dinner.")
Friends.pop(1)
print(Friends)

print(Friends[0] + "You are still welcome at the dinner.")
print(Friends[3] + "You are still welcome at the dinner.")

del Friends[:]
print('Friends: ', Friends)
