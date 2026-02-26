# ===============================
# ✅ LIST CONCEPTS IN ONE FILE
# ===============================

# -------------------------------
# 1. List Creation
# -------------------------------
numbers = [10, 20, 30, 40, 50]
print("Numbers List:", numbers)

numbers1 = [60, 70, 40, 10, 20, 30]
print("Numbers1 List:", numbers1)

# Tuple Example
my_list = (1, 2, 3, 4, "ABC")
print("Type of my_list:", type(my_list))

# -------------------------------
# 2. List Indexing & Slicing
# -------------------------------
names = ["Mubarak", "Naaz", "Raj"]

# Modify element
names[2] = "Jagan"

print("First Name:", names[0])
print("Second Last Name:", names[-2])
print("Slicing Example:", names[0::-1])
print("Updated Names List:", names)

# -------------------------------
# 3. List Methods
# -------------------------------

# Append()
fruit = ["Apple", "Banana"]
fruit.append("Mango")
fruit.append("Kiwi")
print("\nFruit List after append:", fruit)

# Extend()
news = ["Bharati", "Eenadu", "Andhra Jyothi"]
news.extend(["Today News", "Andhra Prabha"])
print("News List after extend:", news)

# Insert(), Remove(), Sort(), Pop()
num = [1, 2, 3, 5, 7]

num.sort(reverse=True)   # Sort descending
num.remove(7)            # Remove element

num.insert(2, 5000)      # Insert at index 2
num.insert(0, "Mubbu")   # Insert at beginning

item_removed = num.pop() # Remove last item

print("\nRemoved Item using pop():", item_removed)
print("Final num list:", num)

# -------------------------------
# 4. Nested List Example
# -------------------------------
nested = [200, 500, [2000, 5000], 10, 20, [200, 100], 10000]

# Delete 2000
del nested[2][0]
print("\nNested List after deletion:", nested)

# -------------------------------
# 5. Flatten Nested List
# -------------------------------
nested1 = [1, 2, [3, 4], [5, 6]]

flat = []

for item in nested1:
    if type(item) == list:
        for i in item:
            flat.append(i)
    else:
        flat.append(item)

print("Flatten List Output:", flat)

# -------------------------------
# 6. Mini Project: Shopping Cart
# -------------------------------

cart = []

while True:
    print("\n====== Shopping Cart System ======")
    print("1. Add Product")
    print("2. Remove Product")
    print("3. View Cart")
    print("4. Search Product")
    print("5. Sort Cart Items")
    print("6. Remove Last Item (Pop)")
    print("7. Clear Cart")
    print("8. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("❌ Please enter only numbers!")
        continue

    # 1. Add Product
    if choice == 1:
        product = input("Enter product name: ")
        cart.append(product)
        print("✅", product, "added to cart!")

    # 2. Remove Product
    elif choice == 2:
        product = input("Enter product name to remove: ")

        if product in cart:
            cart.remove(product)
            print("✅", product, "removed successfully!")
        else:
            print("❌ Product not found in cart!")

    # 3. View Cart
    elif choice == 3:
        if len(cart) == 0:
            print("🛒 Cart is empty!")
        else:
            print("\nYour Cart Items:")
            for item in cart:
                print("👉", item)

    # 4. Search Product
    elif choice == 4:
        product = input("Enter product name to search: ")

        if product in cart:
            print("✅", product, "is available in your cart!")
        else:
            print("❌", product, "not found!")

    # 5. Sort Cart Items
    elif choice == 5:
        cart.sort()
        print("✅ Cart sorted successfully!")
        print(cart)

    # 6. Remove Last Item using pop()
    elif choice == 6:
        if len(cart) == 0:
            print("❌ Cart is empty, nothing to pop!")
        else:
            removed_item = cart.pop()
            print("✅ Removed last item:", removed_item)

    # 7. Clear Cart
    elif choice == 7:
        cart.clear()
        print("✅ Cart cleared successfully!")

    # 8. Exit
    elif choice == 8:
        print("Thank you for shopping 😊")
        break

    else:
        print("❌ Invalid choice! Try again.")
