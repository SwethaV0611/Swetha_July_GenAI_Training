# -----------------------------
# Part A - Spot the Bug
# -----------------------------

def add_item(item, cart=[]):
    cart.append(item)
    return cart


print("Part A - Bug Demonstration")
print(add_item("apple"))
print(add_item("banana"))
print(add_item("milk", cart=["bread"]))
print(add_item("eggs"))

# Explanation:
# The default list (cart=[]) is created only once.
# So the same list is reused every time the function is called
# without providing the 'cart' argument.


# -----------------------------
# Part B - Fix the Bug
# -----------------------------

def add_item_fixed(item, cart=None):
    if cart is None:
        cart = []      # Create a new list every function call

    cart.append(item)
    return cart


print("\nPart B - Correct Function")
print(add_item_fixed("apple"))
print(add_item_fixed("banana"))


# -----------------------------
# Part C - Shopping Cart Program
# -----------------------------

# Create a shopping cart
def create_cart(owner, discount=0):
    return {
        "owner": owner,
        "items": [],
        "discount": discount
    }


# Add item to cart
def add_to_cart(cart, name, price, qty=1):
    item = {
        "name": name,
        "price": price,
        "qty": qty
    }
    cart["items"].append(item)


# Attempt to modify a tuple
def update_price(price_tuple, new_price):
    try:
        price_tuple[0] = new_price
    except TypeError:
        print("\nTypeError: Tuples are immutable and cannot be modified.")


# Calculate total amount
def calculate_total(cart):
    total = 0

    for item in cart["items"]:
        total += item["price"] * item["qty"]

    discount = total * cart["discount"] / 100
    final_total = total - discount

    return final_total


# -----------------------------
# Main Program
# -----------------------------

# Create carts for two customers
cart1 = create_cart("Swetha", 10)
cart2 = create_cart("Harini", 5)

# Add items to first cart
add_to_cart(cart1, "Laptop", 50000, 1)
add_to_cart(cart1, "Mouse", 700, 2)

# Add items to second cart
add_to_cart(cart2, "Mobile", 25000, 1)
add_to_cart(cart2, "Headphones", 1500, 1)

# Display carts
print("\nCustomer 1 Cart")
print(cart1)

print("\nCustomer 2 Cart")
print(cart2)

# Display totals
print("\nTotal for Customer 1:", calculate_total(cart1))
print("Total for Customer 2:", calculate_total(cart2))

# Tuple demonstration
price = (500,)
update_price(price, 600)


# -----------------------------
# Discussion Answers
# -----------------------------

# 1. Why is discount=0 safe but cart=[] dangerous?
# Answer:
# discount=0 is safe because integers are immutable.
# cart=[] is dangerous because lists are mutable and the same list
# is reused across multiple function calls.

# 2. What is the difference between rebinding and mutating?
# Answer:
# Rebinding means assigning a variable to a new object.
# Mutating means changing the contents of an existing object.

# 3. Which of these are mutable?
# Mutable   : list, dict, set
# Immutable : tuple, str, int

# 4. When you pass a list into a function and modify it, do changes
# reflect outside? Why?
# Answer:
# Yes. Lists are mutable, so a function modifies the original list.
# Therefore, the changes are visible outside the function.