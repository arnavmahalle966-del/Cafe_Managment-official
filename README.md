# Cafe_Managment-official
INTRODUCTION:
Nowadays as there are many Cafes are Getting opened , But Most of the Cafes are Working on Old Business Model . Like the Process of Billing , Taking Order from Coustomer and Also Providing a Menu to them . These all are very Old Techniques. I have Designed a Code which makes a Coustomer feels Comfortable and Convinient while ordering an items in a cafe. This Code is very Similar to the working model of a Vending Machine in which You Have to select what you want and at the End there will be the Total Sum of All the items which You have Purchased .In the modern food and beverage industry, efficiency and accuracy in order management are paramount. This project, the Basic Cafe Management System (BCMS), is a console-based application developed in Python. It is designed to simulate the fundamental process of taking customer orders in a cafe or restaurant. The system allows users to select items from a predefined menu, adds them to a virtual cart, and calculates the total bill. Its simplicity and clarity make it an excellent tool for small-scale food service establishments or as an educational prototype.
# Code :
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
