from textwrap import dedent

print("""
**************************************
**  Welcome to the Snakes Cafe! **
**  Please see our menu below.  **

**  To quit at any time, type "quit"    **
**************************************
""")

def show_menu():
    print(dedent("""
    Appetizers
    ----------
    Wings
    Cookies
    Spring Rolls
    
    Entrees
    -------
    Salmon
    Steak
    Meat Tornado
    A Literal Garden
    
    Desserts
    --------
    Ice Cream
    Cake
    Pie
    
    Drinks
    ------
    Coffee
    Tea
    Unicorn Tears
    """))


current_order = {
}
def place_order():
    """
    Adds items to order
    """
    print(dedent("""
    ***********************************
    ** What would you like to order? **
    ***********************************
    """))
    new_order = input("> ")
    print(f"""** 1 order of {new_order} has been added to your meal **
    """)
    if new_order in current_order:
        current_order[new_order] = + 1
    else:
        current_order[new_order] = 1

    ask_again = True
    while ask_again:
        print("What else would you like to order? or type \"quit\" to finish")
        new_order = input("> ")
        if new_order == "quit":
            break
        if new_order in current_order:
            current_order[new_order] += 1
            print(f"""Added another order of {new_order} to your order
            """)
        else:
            current_order[new_order] = 1
            print(f"""Added {new_order} to your order
            """)

    print(f"""
    Your order consists of : {current_order} 
    thank you for your order, don't forget to tip your coder""")


if __name__ == "__main__":
    show_menu()
    place_order()