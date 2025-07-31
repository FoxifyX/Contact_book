li = []
while True:
    try:
        print("\n=== To-Do Task Manager ===")
        print("1.Add task\n2.Remove task\n3.View task\n4.Exit")

        user = int(input("Select what do u want to do [1/2/3/4]: "))

    # Add task
        if user in (1,2,3,4):
            if user == 1:
                add_task = input("What you want to add?: ").strip().lower()
                if add_task:
                    print("---------------------")
                    print(f"✅ {add_task} has been added successfully.")
                    print("---------------------")

                    li.append(add_task)
                else:
                    print("⚠️ Task cannot be empty! ")

    # Remove task    
            elif user == 2:
                rem_task = input("What do you want to remove?: ").strip().lower()

                if rem_task in li:
                    li.remove(rem_task)

                    print("---------------------")
                    print(f"✅ {rem_task} has been removed successfully.")
                    print("---------------------")

                else:
                    print(f"❌ {rem_task} is not available in your task list")

    # View task
            elif user == 3:
                if li:
                    print("📝 Your Tasks:")
                    for i, task in enumerate(li, start=1):
                         print(f"{i}. {task}")
                else:
                    print("📭 No tasks added yet.")

    # Exit task
            elif user == 4:
                
                confirm = input("Do you want to exit?[Yes/No]: ")

                if confirm.strip.lower == "yes":
                    print("---------------------")
                    print("You have exited successfully !")
                    print("---------------------")
                    break

                elif confirm.strip().lower() == "no":
                    print("🔄 Continuing...")

    # Error maintenance
    
                else:
                    print("Please select between Yes or No.")

        
        else:
            print("⚠️ Invalid option. Please select between 1 to 4.")
    
    except ValueError:
        print("P⚠️ Invalid option. Please select between 1 to 4.")

    except Exception as e:
        print("Something Went wrong, ", e)

