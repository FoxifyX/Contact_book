# Basic Calculator
while True:
    try:
        #input from user
        first_num = int(input("Enter your first number: "))
        sec_num = int(input("Enter your second number: "))
        task = input("What u want to do[+, -, *, /]: ")

        # Mathematical operations

        if task in ("+", "-", "*", "/"):

            if task == "+":
                print(f"The sum of {first_num} and {sec_num} is {first_num + sec_num}")

            elif task == "-":
                print(f"The difference between {first_num} and {sec_num} is {first_num - sec_num}")

            elif task == "*":
                print(f"The multiplication of {first_num} and {sec_num} is {first_num * sec_num}")

            elif task == "/":
                if sec_num != 0:
                    print(f"The division of {first_num} and {sec_num} is {round(first_num / sec_num, 3)}")
                    
                else:
                    print("❌ Error: Cannot divide by zero!")
            else:
                print("Something wemt wrong !")

        else:
            print("❌ Error: You didn't select the right operator !")
        
    except ValueError:
        print("❌ Error: Please enter valid numbers only.")

    except Exception as e:
        print("⚠️ Something went wrong!", e)

    again = input("Do you want to calculate again? [Yes/No]").strip().lower()

    if again != "yes":
        print("👋 Bye! Hava a good day!")
        break
