import hashlib
import os
import sys 
import csv

USER_DATA_FILE = 'users.csv'


# ---------- Password Hash ----------
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# ---------- Initialize File ----------
def initialize_file():
    header = [
        'username',
        'password_hash',
        'full_name',
        'email',
        'phone',
        'age',
        'city'
    ]

    if not os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)


# ---------- Register ----------
def register():
    initialize_file()

    username = input("Enter Username: ")
    password = input("Enter Password: ")
    full_name = input("Enter Full Name: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone: ")
    age = input("Enter Age: ")
    city = input("Enter City: ")

    # Check existing username
    with open(USER_DATA_FILE, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['username'] == username:
                print("Username already exists.")
                return

    # Save new user
    with open(USER_DATA_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            username,
            hash_password(password),
            full_name,
            email,
            phone,
            age,
            city
        ])

    print("Registration successful.")


# ---------- Login ----------
def login():
    initialize_file()

    username = input("Enter Username: ").strip()
    password = input("Enter Password: ").strip()

    hashed_pass = hash_password(password)

    with open(USER_DATA_FILE, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['username'] == username and row['password_hash'] == hashed_pass:
                print("\nLogin successful!")
                print("Welcome:", row['full_name'])
                print("Email:", row['email'])
                print("Phone:", row['phone'])
                print("City:", row['city'])
                return

    print("Invalid username or password.")


# ---------- View Users ----------
def view_users():
    initialize_file()

    with open(USER_DATA_FILE, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


# ---------- Main Menu ----------
def main():
    while True:
        print("\n=== User Management System ===")
        print("1. Register")
        print("2. Login")
        print("3. View All Users")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            view_users()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main() 


    import csv
import os

FILE_NAME = "patients.csv"


# ---------------- Initialize File ----------------
def initialize_file():
    header = ["patient_id", "name", "age", "gender", "disease", "phone"]

    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(header)


# ---------------- Generate Patient ID ----------------
def generate_patient_id():
    with open(FILE_NAME, "r") as file:
        reader = list(csv.reader(file))
        return len(reader)  # Auto increment


# ---------------- Add Patient ----------------
def add_patient():
    initialize_file()

    patient_id = generate_patient_id()
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    gender = input("Enter Gender: ")
    disease = input("Enter Disease: ")
    phone = input("Enter Phone: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([patient_id, name, age, gender, disease, phone])

    print("Patient Added Successfully!")


# ---------------- View All Patients ----------------
def view_patients():
    initialize_file()

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


# ---------------- Search Patient ----------------
def search_patient():
    patient_id = input("Enter Patient ID to Search: ")

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["patient_id"] == patient_id:
                print("Patient Found:")
                print(row)
                return

    print("Patient Not Found!")


# ---------------- Delete Patient ----------------
def delete_patient():
    patient_id = input("Enter Patient ID to Delete: ")
    rows = []

    with open(FILE_NAME, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["patient_id"] != patient_id:
                rows.append(row)

    with open(FILE_NAME, "w", newline="") as file:
        fieldnames = ["patient_id", "name", "age", "gender", "disease", "phone"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print("Patient Deleted Successfully!")


# ---------------- Main Menu ----------------
def main():
    while True:
        print("\n===== Hospital Management System =====")
        print("1. Add Patient")
        print("2. View Patients")
        print("3. Search Patient")
        print("4. Delete Patient")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_patient()
        elif choice == "2":
            view_patients()
        elif choice == "3":
            search_patient()
        elif choice == "4":
            delete_patient()
        elif choice == "5":
            print("Exiting System...")
            break
        else:
            print("Invalid Choice!")


if __name__ == "__main__":
    main()