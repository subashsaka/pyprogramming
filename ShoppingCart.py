food = []
price = []
while True:
    items = input(("Enter the food you want to buy or enter Q to quit shopping.\n"))
    if items.lower() == "q":
        break
    else:
        rate = float(input(f"Enter the price of {items} $\n"))
        food.append(items)
        price.append(rate)
print("--------YOUR ITEMS IN CART----------")
print(food)
print("The total bill of your cart is",sum(price))