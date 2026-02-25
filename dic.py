
#This are the Games
# ---------------------- 1 -----------------------------
print("\n1. Student Grades (Highest Marks)")
students = {"Rahul": 85, "Ayesha": 92, "Meena": 95, "Kiran": 88}
top_student = max(students, key=students.get)
print("Highest Marks Student:", top_student, "=", students[top_student])

# ---------------------- 2 -----------------------------
print("\n2. Word Frequency Counter")
text = "python is easy and python is powerful"
words = text.split()
freq = {}

for w in words:
    freq[w] = freq.get(w, 0) + 1

print("Word Frequency:", freq)

# ---------------------- 3 -----------------------------
print("\n3. Employee Directory (Update Salary)")
employees = {
    101: {"name": "Ravi", "role": "Developer", "salary": 40000},
    102: {"name": "Meena", "role": "Tester", "salary": 35000}
}

emp_id = 101
employees[emp_id]["salary"] = 50000
print("Updated Employee Data:", employees[emp_id])

# ---------------------- 4 -----------------------------
print("\n4. Phonebook Search")
phonebook = {"Rahul": "9876543210", "Ayesha": "9123456780"}

search_name = "Rahul"
if search_name in phonebook:
    print("Phone Number:", phonebook[search_name])
else:
    print("Name Not Found")

# ---------------------- 5 -----------------------------
print("\n5. Shopping Cart (Update Quantity)")
cart = {"Apple": 2, "Banana": 5}
cart["Apple"] = 4
print("Updated Cart:", cart)

# ---------------------- 6 -----------------------------
print("\n6. Inventory Management")
inventory = {"P101": 10, "P102": 5}

sale_product = "P102"
inventory[sale_product] -= 5

if inventory[sale_product] == 0:
    del inventory[sale_product]

print("Inventory After Sale:", inventory)

# ---------------------- 7 -----------------------------
print("\n7. Student Subjects List")
student_subjects = {
    "Rahul": ["Math", "Science"],
    "Ayesha": ["English", "History"]
}

print("Subjects of Rahul:", student_subjects["Rahul"])

# ---------------------- 8 -----------------------------
print("\n8. Frequency of Characters")
string = "dictionary"
char_count = {}

for ch in string:
    char_count[ch] = char_count.get(ch, 0) + 1

print("Character Frequency:", char_count)

# ---------------------- 9 -----------------------------
print("\n9. Country-Capital Finder")
capitals = {"India": "New Delhi", "USA": "Washington", "Japan": "Tokyo"}
country = "India"
print("Capital of", country, "is", capitals.get(country))

# ---------------------- 10 ----------------------------
print("\n10. Reverse Dictionary")
reverse_capitals = {v: k for k, v in capitals.items()}
print("Reversed Dictionary:", reverse_capitals)

# ---------------------- 11 ----------------------------
print("\n11. Merging Dictionaries (Sum Prices)")
shop1 = {"Pen": 10, "Book": 50}
shop2 = {"Book": 30, "Pencil": 5}

merged = shop1.copy()
for item, price in shop2.items():
    merged[item] = merged.get(item, 0) + price

print("Merged Dictionary:", merged)

# ---------------------- 12 ----------------------------
print("\n12. Top N Frequent Words")
text2 = "python is easy python is fun python is powerful"
words2 = text2.split()
count_words = {}

for w in words2:
    count_words[w] = count_words.get(w, 0) + 1

top5 = sorted(count_words.items(), key=lambda x: x[1], reverse=True)[:5]
print("Top Frequent Words:", top5)

# ---------------------- 13 ----------------------------
print("\n13. Dictionary Sorting by Marks")
marks = {"Rahul": 85, "Ayesha": 92, "Meena": 95, "Kiran": 88}

sorted_marks = dict(sorted(marks.items(), key=lambda x: x[1], reverse=True))
print("Sorted by Marks:", sorted_marks)

# ---------------------- 14 ----------------------------
print("\n14. Nested Dictionary - School System (Average Marks)")
school = {
    "Class10": {"Rahul": 85, "Ayesha": 92},
    "Class11": {"Meena": 95, "Kiran": 88}
}

class_name = "Class10"
avg = sum(school[class_name].values()) / len(school[class_name])
print("Average Marks of", class_name, "=", avg)

# ---------------------- 15 ----------------------------
print("\n15. Duplicate Finder")
numbers = [1, 2, 3, 2, 4, 5, 1, 2]
dup_count = {}

for num in numbers:
    dup_count[num] = dup_count.get(num, 0) + 1

print("Duplicate Numbers Count:", dup_count)

# ---------------------- 16 ----------------------------
print("\n16. Voting System")
votes = {"CandidateA": 0, "CandidateB": 0}

votes["CandidateA"] += 1
votes["CandidateB"] += 1
votes["CandidateA"] += 1

print("Voting Result:", votes)

# ---------------------- 17 ----------------------------
print("\n17. Currency Converter")
rates = {"USD": 83, "EUR": 90}

amount = 10
currency = "USD"

converted = amount * rates[currency]
print(amount, currency, "=", converted, "INR")

# ---------------------- 18 ----------------------------
print("\n18. Dictionary Comprehension (Squares 1-10)")
squares = {x: x * x for x in range(1, 11)}
print("Squares Dictionary:", squares)

# ---------------------- 19 ----------------------------
print("\n19. Remove Duplicates from List (Preserve Order)")
items = [10, 20, 10, 30, 20, 40]
unique_dict = {}

for i in items:
    unique_dict[i] = True

unique_list = list(unique_dict.keys())
print("List After Removing Duplicates:", unique_list)

# ---------------------- 20 ----------------------------
print("\n20. Pass/Fail Students")
student_marks = {"Rahul": 85, "Ayesha": 35, "Meena": 55, "Kiran": 20}

pass_students = {}
fail_students = {}

for name, mark in student_marks.items():
    if mark >= 40:
        pass_students[name] = mark
    else:
        fail_students[name] = mark

print("Pass Students:", pass_students)
print("Fail Students:", fail_students)


