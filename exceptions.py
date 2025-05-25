def get_number(prompt):
    """Get a valid number from user input with error handling"""
    max_attempts = 3
    attempts = 0
    
    while attempts < max_attempts:
        try:
            user_input = input(prompt)
            number = float(user_input)
            return number
        except ValueError:
            attempts += 1
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"Error: Please enter a valid number. You have {remaining} attempt(s) left.")
            else:
                print("Maximum attempts reached for this input.")
                return None
    
    return None

def divide_numbers():
    """Main function to perform division with error handling"""
    print("Division Calculator with Error Handling")
    print("=" * 40)
    
    # Get first number (dividend)
    print("\nEntering the dividend (number to be divided):")
    dividend = get_number("Enter the first number (dividend): ")
    if dividend is None:
        print("Failed to get valid dividend. Exiting...")
        return
    
    # Get second number (divisor) with additional zero check
    print("\nEntering the divisor (number to divide by):")
    max_attempts = 3
    attempts = 0
    divisor = None
    
    while attempts < max_attempts and divisor is None:
        try:
            user_input = input("Enter the second number (divisor): ")
            temp_divisor = float(user_input)
            
            if temp_divisor == 0:
                attempts += 1
                remaining = max_attempts - attempts
                if remaining > 0:
                    print(f"Error: Cannot divide by zero! You have {remaining} attempt(s) left.")
                else:
                    print("Maximum attempts reached. Cannot proceed with division by zero.")
                    return
            else:
                divisor = temp_divisor
                break
                
        except ValueError:
            attempts += 1
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"Error: Please enter a valid number. You have {remaining} attempt(s) left.")
            else:
                print("Maximum attempts reached for divisor input.")
                return
    
    if divisor is None:
        print("Failed to get valid divisor. Exiting...")
        return
    
    # Perform division
    try:
        result = dividend / divisor
        print(f"\nResult: {dividend} ÷ {divisor} = {result}")
        print(f"Rounded to 2 decimal places: {result:.2f}")
        
    except Exception as e:
        print(f"An unexpected error occurred during division: {e}")

def main():
    """Main program loop"""
    while True:
        divide_numbers()
        
        # Ask if user wants to continue
        while True:
            try:
                continue_choice = input("\nDo you want to perform another division? (y/n): ").lower().strip()
                if continue_choice in ['y', 'yes']:
                    print("\n" + "=" * 50)
                    break
                elif continue_choice in ['n', 'no']:
                    print("Thank you for using the Division Calculator!")
                    return
                else:
                    print("Please enter 'y' for yes or 'n' for no.")
            except KeyboardInterrupt:
                print("\n\nProgram interrupted by user. Goodbye!")
                return

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        print("Program terminated.")