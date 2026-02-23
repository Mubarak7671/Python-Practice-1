# ============================================
# PYTHON SET PROGRAMS (1 to 20)
# ============================================

# 1. Unique Names
print("\n1. Unique Names")
names = ["Ravi", "Sita", "Ravi", "Aman", "Sita"]
unique_names = set(names)
print("Unique Names:", unique_names)


# 2. Common Skills
print("\n2. Common Skills")
applicant1 = {"Python", "Java", "SQL"}
applicant2 = {"Python", "C++", "SQL"}
common_skills = applicant1.intersection(applicant2)
print("Common Skills:", common_skills)


# 3. Exclusive Skills
print("\n3. Exclusive Skills")
exclusive = applicant1.symmetric_difference(applicant2)
print("Exclusive Skills:", exclusive)


# 4. Union of Hobbies
print("\n4. Union of Hobbies")
friend1 = {"Music", "Cricket", "Reading"}
friend2 = {"Movies", "Cricket", "Gaming"}
all_hobbies = friend1.union(friend2)
print("All Hobbies:", all_hobbies)


# 5. Classroom Attendance
print("\n5. Classroom Attendance")
present_students = {"A", "B", "C"}
total_students = {"A", "B", "C", "D", "E"}
absent_students = total_students - present_students
print("Absent Students:", absent_students)


# 6. Duplicate Remover
print("\n6. Duplicate Remover")
def remove_duplicates(lst):
    return list(set(lst))

nums = [1, 2, 2, 3, 4, 4, 5]
print("After Removing Duplicates:", remove_duplicates(nums))


# 7. Vowel Finder
print("\n7. Vowel Finder")
word = "education"
vowels = {"a", "e", "i", "o", "u"}
found = set(word).intersection(vowels)
print("Vowels Present:", found)


# 8. Disjoint Check
print("\n8. Disjoint Check")
football = {"A", "B", "C"}
cricket = {"D", "E"}
print("Play both?", not football.isdisjoint(cricket))


# 9. Subset Check
print("\n9. Subset Check")
frontend = {"HTML", "CSS"}
web = {"HTML", "CSS", "JavaScript", "Python"}
print("Frontend subset of Web?", frontend.issubset(web))


# 10. Superset Check
print("\n10. Superset Check")
company_skills = {"Python", "SQL", "Django", "Git"}
job_req = {"Python", "SQL"}
print("Company covers job requirements?", company_skills.issuperset(job_req))


# 11. Symmetric Difference in Orders
print("\n11. Symmetric Difference in Orders")
site1 = {"Cust1", "Cust2", "Cust3"}
site2 = {"Cust2", "Cust4"}
only_one_site = site1.symmetric_difference(site2)
print("Customers ordered from only one site:", only_one_site)


# 12. Frequency Counter (Unique Words)
print("\n12. Unique Words in Paragraph")
para = "Python is easy and Python is powerful"
unique_words = set(para.split())
print("Unique Words:", unique_words)


# 13. Password Character Types
print("\n13. Password Character Types")
password = "Hello@123"

digits = set("0123456789")
upper = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
lower = set("abcdefghijklmnopqrstuvwxyz")
special = set("@#$%^&*")

pwd_set = set(password)

print("Has Digit?", bool(pwd_set & digits))
print("Has Uppercase?", bool(pwd_set & upper))
print("Has Lowercase?", bool(pwd_set & lower))
print("Has Special?", bool(pwd_set & special))


# 14. Unique Characters in Sentence
print("\n14. Unique Characters in Sentence")
sentence = "hello world"
unique_chars = set(sentence.replace(" ", ""))
print("Unique Characters Count:", len(unique_chars))


# 15. Prime Numbers up to 50
print("\n15. Prime Numbers up to 50")
primes = set()

for num in range(2, 51):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        primes.add(num)

print("Prime Numbers:", primes)


# 16. Intersection in Cities
print("\n16. Common Cities")
company1 = {"Delhi", "Mumbai", "Goa"}
company2 = {"Goa", "Chennai", "Delhi"}
common_cities = company1 & company2
print("Common Cities:", common_cities)


# 17. Unique Digits
print("\n17. Unique Digits")
number = 122334455
unique_digits = set(str(number))
print("Unique Digits:", unique_digits)


# 18. Symmetric Difference in Elections
print("\n18. Candidates in Exactly One Party")
party1 = {"A", "B", "C"}
party2 = {"B", "D", "E"}
exactly_one = party1 ^ party2
print("Only One Party Candidates:", exactly_one)


# 19. Frozen Set Usage
print("\n19. Frozen Set Usage")
vowel_frozen = frozenset({"a", "e", "i", "o", "u"})
dictionary = {vowel_frozen: "Vowels Key"}
print("Frozen Set used as Dictionary Key:", dictionary)


# 20. Set Operations Menu
print("\n20. Set Operations Menu")

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Set1:", set1)
print("Set2:", set2)

print("\nUnion:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference (Set1-Set2):", set1 - set2)
print("Symmetric Difference:", set1 ^ set2)

print("\n✅ All Set Programs Completed Successfully!")
