# UTILS AND FUNCTIONALITY
from data import stores
from components import Cart

site_name = "Cadabra.com"  # Give your site a name

def welcome():
    print("Welcome to %s\nFeel free to shop throughout the stores we have, and only checkout once!" % site_name)

def print_stores():
    """
    prints the list of stores in a nice readable format.
    """
    # your code goes here!
    for store in stores:
        print( "- %s" % (store.name))

def get_store(store_name):
    """
    receives a name for a store, and returns the store object with that name.
    """
    # your code goes here!
    for store in stores:
        if store.name.lower() == store_name.lower():
            return store


def pick_store():
    """
    prints list of stores and prompts user to pick a store.
    """
    # your code goes here!

    while True:
        
        print_stores()
        store_name = input("Pick a store by typing it's name. or type \"checkout\" to pay your bills and say your goodbyes.\n")
        
        if store_name == "checkout":
            return False
        
        for store in stores:
            if store.name.lower() == store_name.lower():
                #print("store found")
                return store
        print("Sorry, thats not a store on our site.") 


def pick_products(cart, picked_store):
    """
    prints list of products and prompts user to add products to card.
    """
    # your code goes here!
    picked_store.print_products()

    print("Pick a prodect to add to the cart or enter \"back\" to go back to the store list.\nPlease use exact spelling: ")
    user_in=input()
    while True:
        
        product_found_flag = False

        if user_in.lower() == "back":
            return True

        else:
            for product in picked_store.products:
                if product.name.lower() == user_in.lower():
                    cart.add_to_cart(product)
                    print("%s added to cart\n" % product.name)
                    product_found_flag = True

            if product_found_flag == True:
                user_in = input("Anything else? type 'back' to go back\n")
            elif product_found_flag == False:
                user_in = input("Sorry that product doesn't exist!\n")

def shop():
    """
    The main shopping functionality
    """
    cart = Cart()
    # your code goes here!
    picked_store = pick_store()
    while True:
        if picked_store == False:
            break
        back = pick_products(cart, picked_store)
        if (back):
            picked_store = pick_store()

    cart.checkout()


def thank_you():
    print("Thank you for shopping with us at %s" % site_name)
