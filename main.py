"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    semester_cost = annual_cost / SEMESTERS_PER_YEAR
    return semester_cost


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    month_cost = annual_cost / MONTHS_PER_YEAR
    return month_cost


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    total_days = CLASS_DAYS_PER_SEMESTER * SEMESTERS_PER_YEAR
    day_cost = annual_cost / total_days
    return day_cost
    

    


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    semester_cost = cost_per_semester(annual_cost)
    credit_cost = semester_cost / credits
    return credit_cost


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    credit_cost = cost_per_credit(annual_cost, credits)
    class_cost = credit_cost * CS1430_CREDITS
    meeting_cost = class_cost / CS1430_MEETINGS_PER_SEMESTER
    return meeting_cost

def cost_of_skipped_classes(annual_cost, credits, skipped_classes):
    """Give back what the cost of skipped classes is."""
    meeting_cost = cost_per_class(annual_cost, credits)
    total_skipped_cost = meeting_cost * skipped_classes
    return total_skipped_cost


# ---- PROGRAM ----

def main():
    # Ask for the total cost for one year here.
    # Then ask for the credits this semester.
    print("Welcome to the Cost of College Calculator!")
    annual_cost = float(input("Enter the total cost for one year: "))
    credits = int(input("Enter the number of credits this semester: "))
    while True:
        print("\nMenu:")
        print("1. Cost per semester")
        print("2. Cost per month")
        print("3. Cost per day")
        print("4. Cost per credit")
        print("5. Cost per class")
        print("6. Cost of skipped classes")
        print("Q. Quit")

        choice = input("Choose an option: ").upper()

        if choice == "1":
            semester_cost = cost_per_semester(annual_cost)
            print(f"Cost per semester: ${semester_cost:.2f}")
        elif choice == "2":
            month_cost = cost_per_month(annual_cost)
            print(f"Cost per month: ${month_cost:.2f}")
        elif choice == "3":
            day_cost = cost_per_day(annual_cost)
            print(f"Cost per day: ${day_cost:.2f}")
        elif choice == "4":
            credit_cost = cost_per_credit(annual_cost, credits)
            print(f"Cost per credit: ${credit_cost:.2f}")
        elif choice == "5":
            class_cost = cost_per_class(annual_cost, credits)
            print(f"Cost per class: ${class_cost:.2f}")
        elif choice == "6":
            skipped_classes = int(input("Enter the number of skipped classes: "))
            skipped_cost = cost_of_skipped_classes(annual_cost, credits, skipped_classes)
            print(f"Cost of skipped classes: ${skipped_cost:.2f}")
        elif choice == "Q":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
