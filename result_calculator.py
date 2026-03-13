def get_grade(average):
    """Return the grade based on the average mark."""
    if average >= 75:
        return "A"
    elif average >= 65:
        return "B"
    elif average >= 50:
        return "C"
    elif average >= 35:
        return "S"
    else:
        return "F"

def calculate_results():
    print("--- Result Calculator (Type 'exit' to quit) ---")
    while True:
        try:
            # Input marks for three subjects
            user_input = input("\nEnter marks for Subject 1 (or 'exit'): ").strip().lower()
            if user_input == 'exit':
                print("Exiting calculator. Goodbye!")
                break
                
            mark1 = float(user_input)
            mark2 = float(input("Enter marks for Subject 2: "))
            mark3 = float(input("Enter marks for Subject 3: "))

            # Validation: Marks should be between 0 and 100
            marks = [mark1, mark2, mark3]
            if not all(0 <= m <= 100 for m in marks):
                print("Error: Marks should be between 0 and 100.")
                continue

            # Calculate Total and Average
            total = sum(marks)
            average = total / 3

            # Determine Grade
            grade = get_grade(average)

            # Display results
            print("\n--- Results ---")
            print(f"Total Marks:   {total:.2f}")
            print(f"Average Marks: {average:.2f}")
            print(f"Grade:         {grade}")

        except ValueError:
            print("Error: Please enter valid numeric marks or 'exit'.")

if __name__ == "__main__":
    calculate_results()
