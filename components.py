# CLASSES AND METHODS
class Store():
    def __init__(self, name):
        """
        Initializes a new store with a name.
        """
        # your code goes here!
        self.name = name
        self.products = []

    def add_product(self, product):
        """
        Adds a product to the list of products in this store.
        """
        # your code goes here!
        self.products.append(product)


    def print_products(self):
        """
        Prints all the products of this store in a nice readable format.
        """
        # your code goes here!
        print("------------------------------")
        print("%s" % (self.name))
        for item in self.products:
            print(item)
            print()


class Product():
    def __init__(self, name, description, price):
        """
        Initializes a new product with a name, a description, and a price.
        """
        # your code goes here!
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        # your code goes here!
        return ("\tProduct Name: %s\n\tDescription: %s\n\tPrice: %s" % (self.name, self.description, self.price))


class Cart():
    def __init__(self):
        """
        Initializes a new cart with an empty list of products.
        """
        # your code goes here! 
        self.shoping_cart = []

    def add_to_cart(self, product):
        """
        Adds a product to this cart.
        """
        # your code goes here!
        self.shoping_cart.append(product)

    def get_total_price(self):
        """
        Returns the total price of all the products in this cart.
        """
        # your code goes here!
        total = 0
        for product in self.shoping_cart:
            total += product.price
        return total

    def print_receipt(self):
        """
        Prints the receipt in a nice readable format.
        """
        # your code goes here!
        print("------------------------------")
        print("Here's your receipt:")
        for product in self.shoping_cart:
            print(product)
            print()

        print("Your total is: %s KWD" % (self.get_total_price()))

    def checkout(self):
        """
        Does the checkout.
        """
        # your code goes here!
        self.print_receipt()
        user_in = input("Confirm?(yes/no): ")

        while True:
            if user_in.lower() == "yes" or user_in == "y":
                print("Your order has been placed.")
                self.shoping_cart = []
                break

            elif user_in.lower() == "no" or user_in.lower() == "n":
                print("Order has been canceled")
                break

            else:
                print("Thats not a valid input!")
                user_in = input("Confirm?(yes/no): ")