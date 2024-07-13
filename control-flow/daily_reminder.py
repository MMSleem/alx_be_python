def get_task_details():
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    return task, priority, time_bound

def generate_reminder(task, priority, time_bound):
    reminder = f"'{task}' is a {priority} priority task"
    match priority:
        case 'high':
            reminder += " that requires immediate attention"
        case 'medium':
            reminder += " that should be completed soon"
        case 'low':
            reminder += " that can be completed when you have free time"
        case _:
            reminder += " with an unspecified priority level"
    
    if time_bound == 'yes':
        reminder += " today!"
    else:
        reminder += "."
    
    return reminder

def main():
    task, priority, time_bound = get_task_details()
    reminder = generate_reminder(task, priority, time_bound)
    print(f"Reminder: {reminder}")

if __name__ == "_main_":
    main()