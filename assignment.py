products = ["apple", "banana", "orange", "grapes", "mango"]
prices = [1.00, 0.50, 0.80, 2.00, 1.50]
shopping_cart = [] #this stays empty at first since the user has not added any products to the cart yet
checkout = False #this variable is used to control the "main loop" of the program, which will keep running until the user chooses to checkout


def display_products():
    print("======= Available Products =======")
    if products == []:
        print("No products available.")
    else:
        for i, product in enumerate(products):
            print(f"- {product} - ${float(prices[i]):.2f}") #the float() function is used to convert the price to a float, and the :.2f format specifier is used to display the price with two decimal places
            print(" ")


def add_product():
    print("======= Add Product to Cart =======")
    if products == []: #this is if there is nothing in the products list
        print("No products available to add to cart.")

    else:

        for i, product in enumerate(products, start=1): #for each product in the products list, the enumerate() function is used to get the index of the product, starting from 1. The index is then used to display the product number to the user.
            print(f"{i}. {product} - ${float(prices[i - 1]):.2f}") 
            print(" ")
        product_num = int(input("Enter the number of the product: "))

        while product_num < 1 or product_num > len(products):# this is a while loop that will keep asking the user for a valid product number until they enter one. The condition checks if the product number is less than 1 or greater than the length of the products list. If it is, the user is prompted to enter a valid product number.
            if product_num < 1 or product_num > len(products): #im not quite sure if i need this if statement but imma keep here for now since it works
                print("Invalid product number.")
                product_num = int(input("Enter the number of the product: "))

        product = products[product_num - 1] #this gets the product from the products list based on the user's choice
        shopping_cart.append(product)
        print(f"{product} has been added to cart.")


def display_cart():
    for i, item in enumerate(shopping_cart, start=1): #this is a for loop that will display each item in the shopping cart, along with its index (starting from 1)
        print(f"{i}. {item} - ${float(prices[products.index(item)]):.2f}")
        print(" ")


def remove_product():
    removed = input("Do you want to remove an item from the cart? (y/n): ")

    if removed == "y":
        removed_item = int(input("Enter the number of the item to remove: "))
        while removed_item < 1 or removed_item > len(shopping_cart): #this is a while loop that will keep asking the user for a valid item number until they enter one. The condition checks if the item number is less than 1 or greater than the length of the shopping cart. If it is, the user is prompted to enter a valid item number.
            print("Invalid item number.")
            removed_item = int(input("Enter the number of the item to remove: "))
        removed_product = shopping_cart.pop(removed_item - 1)#this removes the item from the shopping cart based on the user's choice and stores it in a variable called removed_product
        print(f"{removed_product} has been removed from the cart.")
    else:
        print("No items removed from the cart.")


def calculate_total():
    total = 0
    for item in shopping_cart: #this is a for loop that will go through each item in the shopping cart
        spot = products.index(item) #this gets the index of the item in the products list, which is then used to get the price of the item from the prices list
        total = total + prices[spot]
    return total


def calculate_discount(total):
    discount = 0
    if total > 10 and total <= 20: #this is an if statement that checks if the total is greater than 10 and less than or equal to 20. If it is, a discount of 5% is applied to the total. The discount is then subtracted from the total and printed to the user.
        discount = total * 0.05
        total = total - discount
        print(f"Discount: ${discount:.2f}") #this prints the discount amount
        print(f"Total after discount: ${total:.2f}")

    elif total > 20 and total <= 40:
        discount = total * 0.10
        total = total - discount
        print(f"Discount: ${discount:.2f}")
        print(f"Total after discount: ${total:.2f}")

    elif total > 40:
        discount = total * 0.15
        total = total - discount
        print(f"Discount: ${discount:.2f}")
        print(f"Total after discount: ${total:.2f}")

    return discount


while checkout == False: #this is a while loop that will keep running until the user chooses to checkout. The condition checks if the checkout variable is False. If it is, the loop will continue to run. If it is True, the loop will stop and the program will end.
    print("======= Welcome to the store! =======")
    print("1. View available products")
    print("2. Add product to cart")
    print("3. View current cart")
    print("4. View current total")
    print("5. Checkout")
    choice = int(input("Enter your choice: "))


    if choice == 1:
        display_products()


    elif choice == 2:
        add_product()


    elif choice == 3:
        print("======= Current Cart =======")
        if shopping_cart == []:
            print("Your cart is empty.")

        else:

            display_cart()
            remove_product()


    elif choice == 4:
        print("======= Current Total =======")
        if shopping_cart == []: #this if statement checks if the shopping cart is empty
            print("Your cart is empty.")

        else:

            display_cart()

            total = calculate_total()
            print(f"Total Items: {len(shopping_cart)}") #this prints the total number of items in the cart using the len() to get the full length of the list
            print(f"Subtotal: ${total:.2f}")


    elif choice == 5:
        print("======= Checkout =======")
        if shopping_cart == []:
            print("Your cart is empty.")

        else:

            total = calculate_total()
            print(f"Total Items: {len(shopping_cart)}")
            print(f"Subtotal: ${total:.2f}")

            discount = calculate_discount(total)


            maybe_checkout = input("Do you want to proceed to checkout? (y/n): ")
            if maybe_checkout == "y": #this if statement checks if the user wants to checkout and if they do then it stops the program
                checkout = True
                print("Thank you for shopping with us!")