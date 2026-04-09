import os
import logging
from utility import setup_logging
import pandas as pd

DATA_DIR = "data"


# ---------------- MENU ----------------
def menu():
    while True:
        print("\n==== MENU ====")
        print("1. Check Attendance")
        print("2. Create Grade Level")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            check_attendance(DATA_DIR)
        elif choice == "2":
            create_grade_level(DATA_DIR)
        elif choice == "3":
            print("Exiting...")
            logging.info("Program exited")
            break
        else:
            print("Invalid choice. Try again.")


# ---------------- CREATE GRADE ----------------
def create_grade_level(path):
    os.makedirs(path, exist_ok=True)

    grade_level = input("Enter grade level to create (e.g., 6): ")

    if not grade_level.isdigit():
        print("Invalid grade level.")
        return

    grade_path = os.path.join(path, f"Grade-{grade_level}")
    os.makedirs(grade_path, exist_ok=True)

    logging.info(f"Grade level created: Grade-{grade_level}")
    print(f"Created: {grade_path}")

    # 🔥 NEW FEATURE
    print("\nDo you want to:")
    print("1. Manually create files")
    print("2. Auto-generate student & attendance files")

    choice = input("Enter choice: ")

    if choice == "1":
        logging.info(f"Manual file setup chosen for Grade-{grade_level}")
        print("You can manually add your Excel/CSV files in the folder.")

    elif choice == "2":
        create_default_files(grade_path, grade_level)

    else:
        print("Invalid choice. Skipping file creation.")

def create_default_files(grade_path, grade_level):
    try:
        # Students file
        students_file = os.path.join(grade_path, "students.csv")
        students_df = pd.DataFrame(columns=["student_id", "name", "gender"])
        students_df.to_csv(students_file, index=False)

        # Attendance file
        attendance_file = os.path.join(grade_path, "attendance.csv")
        attendance_df = pd.DataFrame(columns=["date", "student_id", "status"])
        attendance_df.to_csv(attendance_file, index=False)

        logging.info(f"Default files created for Grade-{grade_level}")
        print("✅ student and attendance files created successfully!")

    except Exception as e:
        logging.error(f"Error creating default files: {e}")
        print("Something went wrong while creating files.")


# ---------------- CHECK ATTENDANCE ----------------
def check_attendance(path):
    while True:
        grade_level = input("Enter grade level to check (e.g., 6): ")

        if not grade_level.isdigit():
            print("Invalid input. Try again.")
            continue

        grade_path = os.path.join(path, f"Grade-{grade_level}")

        if os.path.exists(grade_path):
            logging.info(f"Accessed attendance: Grade-{grade_level}")
            print(f"Accessing: {grade_path}")
            break
        else:
            logging.warning(f"Grade level not found: Grade-{grade_level}")
            print("Grade level does not exist. Try again.")


# ---------------- MAIN ----------------
if __name__ == '__main__':
    setup_logging(".logs")
    menu()