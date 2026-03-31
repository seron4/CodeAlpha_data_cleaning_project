from validator import validate_data, is_false_data
from duplicate_checker import is_duplicate
import sqlite3

def insert_data(name, email):
    # Step 1: Validate
    valid, message = validate_data(name, email)
    if not valid:
        print("❌", message)
        return

    # Step 2: False data check
    if is_false_data(name):
        print("❌ False Data Detected")
        return

    # Step 3: Duplicate check
    if is_duplicate(email):
        print("❌ Duplicate Data")
        return

    # Step 4: Insert
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO records (name, email) VALUES (?, ?)", (name, email))

    conn.commit()
    conn.close()

    print("✅ Data Stored Successfully")

# User Input
name = input("Enter Name: ")
email = input("Enter Email: ")

insert_data(name, email)
