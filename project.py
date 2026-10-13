print("===== PERSONAL STUDY PLANNER =====")

tasks = []

while True:
    print("\n1. Add Study Task")
    print("2. View Study Tasks")
    print("3. Complete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        subject = input("Enter subject: ")
        topic = input("Enter topic: ")
        hours = input("Enter study hours: ")

        task = [subject, topic, hours, "Pending"]
        tasks.append(task)

        print("Task added successfully!")

    elif choice == "2":
        print("\n===== YOUR STUDY TASKS =====")

        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks):
                print(
                    i + 1,
                    ".",
                    task[0],
                    "-",
                    task[1],
                    "-",
                    task[2],
                    "hours",
                    "-",
                    task[3]
                )

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\n===== COMPLETE A TASK =====")

            for i, task in enumerate(tasks):
                print(
                    i + 1,
                    ".",
                    task[0],
                    "-",
                    task[1],
                    "-",
                    task[3]
                )

            try:
                task_no = int(input("Enter task number to complete: "))

                if 1 <= task_no <= len(tasks):
                    tasks[task_no - 1][3] = "Completed"
                    print("Task completed successfully!")
                else:
                    print("Invalid task number.")

            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        print("Thank you for using Personal Study Planner!")
        break

    else:
        print("Invalid choice. Please try again.")
