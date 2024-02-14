def main():
    tasks = []

    while True:
        print("\n===== to do list =====")
        print("1. Add task ")
        print("2. show tasks")
        print("3.Mark task as done")
        print("4. Exit")

        choice = input("enter your choice: ")

        if choice == '1':
            print()
            n_tasks = input("how may task you want to add : ")

            for i in range(1 , 2):
                task = input("Enter the task: ")
                tasks.append({"task": task, "done":False})
                print("task added!")

        elif choice == '2':
            print("\nTasks:")
            for index,task in enumerate(tasks):
                status = "Done" if task["done"] else "Not done"
                print(f"{index + 1}. {task['task']} - {status}")

        elif choice == '3':
            task_index = input("enter the task number to mark as done: ") -1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print("task marked as done! ")
            else:
                print("invalid task number.")

        elif choice == '4' :
            print("Exiting the To-Do List.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()