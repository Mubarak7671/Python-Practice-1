# ============================================
# LIST & TUPLE ASSIGNMENT PROGRAMS (1–30)
# ============================================

print("\n========== A. BASIC LIST & TUPLE OPERATIONS ==========")

# 1. Student Names Indexing
print("\n1. Student Names Indexing")
students = ["Aman", "Ravi", "Sita", "John", "Kiran",
            "Neha", "Arjun", "Meena", "Raj", "Pooja"]
print("1st Student:", students[0])
print("5th Student:", students[4])
print("Last Student:", students[-1])


# 2. Replace 3rd Food Item
print("\n2. Replace Favorite Food")
foods = ["Pizza", "Burger", "Pasta", "Dosa", "Ice Cream"]
foods[2] = "Biryani"
print("Updated Foods:", foods)


# 3. Tuple Cities → List → Tuple
print("\n3. Tuple Conversion")
cities = ("Delhi", "Mumbai", "Chennai", "Goa", "Pune")
city_list = list(cities)
city_list.append("Hyderabad")
cities = tuple(city_list)
print("Updated Tuple:", cities)


# 4. Check Fruit Present
print("\n4. Fruit Check")
fruits = ["banana", "mango", "apple", "orange"]
if "apple" in fruits:
    print("Apple is present!")
else:
    print("Apple not found!")


# 5. Even Numbers Using Slicing
print("\n5. Even Numbers from 1–20")
nums = list(range(1, 21))
print("Even Numbers:", nums[1::2])


print("\n========== B. ITERATION & MANIPULATION ==========")

# 6. Add Numbers Without sum()
print("\n6. Add Numbers Without sum()")
numbers = [10, 20, 30, 40, 50]
total = 0
for n in numbers:
    total += n
print("Total Sum:", total)


# 7. Weekdays Tuple Uppercase
print("\n7. Weekdays in Uppercase")
weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday",
            "Friday", "Saturday", "Sunday")
for day in weekdays:
    print(day.upper())


# 8. Reverse List Without reverse() or slicing
print("\n8. Reverse List Manually")
lst = [1, 2, 3, 4, 5]
rev = []
for i in range(len(lst)):
    rev.append(lst[len(lst) - 1 - i])
print("Reversed List:", rev)


# 9. Average Temperature
print("\n9. Average Temperature")
temps = [36.5, 37.2, 38.0, 39.1, 40.0]
avg = sum(temps) / len(temps)
print("Average Temp:", avg)


# 10. Find Index of 30 Without index()
print("\n10. Index of 30")
tup = (10, 20, 30, 40, 50)
for i in range(len(tup)):
    if tup[i] == 30:
        print("Index of 30:", i)


print("\n========== C. REALISTIC PROBLEM-SOLVING ==========")

# 11. Highest & Lowest Marks
print("\n11. Highest & Lowest Marks")
marks = [78, 90, 65, 88, 72]
print("Highest Mark:", max(marks))
print("Lowest Mark:", min(marks))


# 12. Remove Duplicates in Cart
print("\n12. Unique Shopping Cart Items")
cart = ["milk", "bread", "milk", "eggs", "bread"]
unique_cart = list(set(cart))
print("Final Cart:", unique_cart)


# 13. Increase Salary by 10%
print("\n13. Salary Increment")
salaries = [25000, 40000, 30000, 50000, 45000]
updated = []
for s in salaries:
    updated.append(s + (s * 0.10))
print("Updated Salaries:", updated)


# 14. Merge Two Lists into Tuples
print("\n14. Merge Items & Quantity")
items = ["pen", "pencil", "eraser"]
qty = [5, 10, 2]
merged = list(zip(items, qty))
print("Merged List:", merged)


# 15. Count Scores More Than 50
print("\n15. Count Scores > 50")
scores = [45, 60, 90, 30, 75]
count = 0
for s in scores:
    if s > 50:
        count += 1
print("Students scored >50:", count)


print("\n========== D. SORTING & SEARCHING ==========")

# 16. Sort Numbers Ascending & Descending
print("\n16. Sorting Numbers")
nums = [34, 12, 67, 45, 89, 21]
print("Ascending:", sorted(nums))
print("Descending:", sorted(nums, reverse=True))


# 17. Sort Tuple Words Alphabetically
print("\n17. Sort Tuple Words")
words = ("banana", "apple", "cherry", "date")
sorted_words = tuple(sorted(words))
print("Sorted Tuple:", sorted_words)


# 18. 2nd Largest Number
print("\n18. Second Largest Number")
nums = [10, 50, 30, 90, 70]
nums_sorted = sorted(nums)
print("Second Largest:", nums_sorted[-2])


# 19. Search Name Without using 'in'
print("\n19. Search Name Without 'in'")
names = ["Aman", "Ravi", "Sita", "John"]
search = "Sita"
found = False

for n in names:
    if n == search:
        found = True

if found:
    print("Name Found!")
else:
    print("Name Not Found!")


# 20. Remove Negative Numbers
print("\n20. Remove Negative Numbers")
nums = [10, -5, 20, -3, 40]
positive = []
for n in nums:
    if n >= 0:
        positive.append(n)
print("Positive List:", positive)


print("\n========== E. CONVERSION & REAL-LIFE USAGE ==========")

# 21. String to List of Characters
print("\n21. String to Characters")
text = "hello world"
chars = list(text)
print(chars)


# 22. List to Tuple
print("\n22. List to Tuple")
lst = [1, 2, 3, 4]
tup = tuple(lst)
print("Tuple:", tup)


# 23. Join Words into Sentence
print("\n23. Join Words")
words = ["Python", "is", "fun"]
sentence = " ".join(words)
print("Sentence:", sentence)


# 24. Products Costing More Than 35
print("\n24. Products > 35")
products = [("Milk", 40), ("Bread", 30), ("Eggs", 60)]
for p, price in products:
    if price > 35:
        print(p, "costs", price)


# 25. Only .txt Files
print("\n25. Filter .txt Files")
files = ["file1.txt", "file2.doc", "file3.txt"]
txt_files = []
for f in files:
    if f.endswith(".txt"):
        txt_files.append(f)
print("TXT Files:", txt_files)


print("\n========== F. ADVANCED & APPLICATION BASED ==========")

# 26. Intersection of Two Lists
print("\n26. Common Elements")
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = list(set(list1) & set(list2))
print("Intersection:", common)


# 27. Find Topper
print("\n27. Find Topper")
students_scores = [("Alice", 85), ("Bob", 70), ("Charlie", 90)]
topper = max(students_scores, key=lambda x: x[1])
print("Topper:", topper)


# 28. Count Frequency of Elements
print("\n28. Frequency Counter")
lst = [1, 2, 2, 3, 3, 3]
freq = {}

for item in lst:
    freq[item] = freq.get(item, 0) + 1

print("Frequency:", freq)


# 29. Remove Words with Length < 4
print("\n29. Remove Short Words")
words = ["cat", "lion", "tiger", "ox", "bear"]
filtered = []

for w in words:
    if len(w) >= 4:
        filtered.append(w)

print("Filtered Words:", filtered)


# 30. Transaction Balance Calculator
print("\n30. Account Balance")
transactions = [200, -100, 300, -50, 400, -200]
balance = 0

for t in transactions:
    balance += t

print("Final Balance:", balance)


print("\n✅ All List & Tuple Programs Completed Successfully!")
