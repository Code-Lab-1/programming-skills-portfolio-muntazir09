me = {"name":"Muhammad Mahdi", "Gender":"Male", "Age":"18", "Nationality":"Pakistani"}
me["name"]="Muhammad Muntazir Mahdi"
print(me)
me.popitem()
print(me)
if "Gender" in me:
    print("it is present.")
else: print("it is not present.")
