cup = {}
menu = {'Americano':1800,'Cafe latte': 2200, 'Cafe Mocha': 2800}
num = 0

def print_menu():
    print("========Sookmyung Cafe========\n1. Select coffee menu\n2. Check your order")
    print("3. Pay total price\n4. Get change\n")

def print_coffeeMenu():
    print("[Cafe Menu]\nAmericano 1800won\nCafe latte 2200won\nCafe Mocha 2800won")

def select_menu():
    selectMenu = input("Select Menu : ")
    while selectMenu not in menu:
        print("You selected wrong menu..")
        selectMenu = input("Select Menu : ")
    cups = int(input("How many cups ? "))
    cup[selectMenu] = cups

def check_oreder():
    for (key,value) in cup.items():
        print("%s \t %d cups"%(key, value))

totalPrice = 0
money = 0
def calculate_price():
    for key,value in cup.items():
        global totalPrice
        totalPrice += menu[key]*value
    global money
    money = int(input("Pay money: "))
    while totalPrice > money:
        print("Too small..")
        money = int(input("Pay money:"))

def get_change():
    change = money-totalPrice
    print("Your change is %d won.\n================================"%change)
    print("5000 won : %d"%(change//5000))
    change-=5000*(change//5000)
    print("1000 won : %d"%(change//1000))
    change-=1000*(change//1000)
    print("500 won : %d"%(change//500))
    change-=500*(change//500)
    print("100 won : %d\n"%(change//100))
    print("Thank you for using our machine")

while True:
    print_menu()
    num = int(input("choose : "))
    if num == 1:
        print_coffeeMenu()
        select_menu()
        print(cup)
    elif num ==2:
        check_oreder()
    elif num==3:
        calculate_price()
    elif num==4:
        get_change()
        break
