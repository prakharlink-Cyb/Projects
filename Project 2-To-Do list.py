print("================Plan your day================")

Plan = []

print("Welcome to to-do list.")
print("Plan your day.")

while True:
    user = input("Enter your task (type 'Done' to finish): ")
    if user.lower() == "done":
        break
    Plan.append(user)

done = input("Do you want to save this task list for today? (Y/N): ")

if done.lower() == "y":
    print("\nYour Today's Plan:")
    print(Plan)
    print("That's your today's task.")
else:
    print("\nTasks not added to today's plan.")
