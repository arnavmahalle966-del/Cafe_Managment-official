menu = {
    "Burger" : 60,
   "Pizza" : 80,
    "Pasta": 50,
    "Noodles":60
}

print("Welcome to our Cafe ")
print("1)Burger:60\n2)Pizza:80\n3)Pasta:50\n4)Noodles:60")

order_total = 0

order_1 = (input("Enter Your Item="))


if order_1 in menu:
    order_total += menu[order_1]
    print(f"{order_1} has been added to Your Cart")

else:
    print(f"{order_1} is not available yet")

another_order = input("Do You want to add another item ? Yes / No=")

if another_order =="Yes":
    order_2 = input("Enter Your Second Order=")
    if order_2 in menu:
        order_total += menu[order_2]
        print(f"{order_2} has been added to Your Cart")

    else:
        print(f"{order_2} is not available yet")

print(f"You have to Pay {order_total}rs for Your Orders")

