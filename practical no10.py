while True:
    print("\n====TASK MANAGER====")
    print("1. Add Task")
    print("2. Process Tasks")
    print("3.Undo Tasks")
    print("4.Show Tasks")
    print("5.Exit")

    choice=input("Enter choice:")
    if choice=="1":
        task=input("Enter task:")
        add_task(task)
    elif choice=="2":
        process_task()
    elif choice=="3":
        undo_task()
    elif choice=="4":
        show_tasks()
    elif choice=="5":
        break
    else:
        print("Invalid Choice")