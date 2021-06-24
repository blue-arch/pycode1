def make_pizza(size,*toppings):
    print("\nmaking a "+str(size)+" inch pizza with the following toppibngs")
    for topping in toppings:
        print("-"+topping)