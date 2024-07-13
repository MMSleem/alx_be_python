def display_menu():
    """Displays the menu options to the user."""
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def add_item(shopping_list):
    """Prompts the user for an item and adds it to the shopping list."""
    item = input("Enter the item to add: ")  # This line was missing
    shopping_list.append(item)
    print(f"{item} added to the list.")


def remove_item(shopping_list):
    """Prompts the user for an item and removes it from the shopping list."""
    item = input("Enter item to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} removed from the list.")
    else:
        print(f"{item} not found in the list.")


def view_list(shopping_list):
    """Displays the current items in the shopping list."""
    if shopping_list:
        print("\nYour Shopping List:")
        for i, item in enumerate(shopping_list, start=1):
            print(f"{i}. {item}")
    else:
        print("Your shopping list is empty.")


def main():
    shopping_list = []

    while True:
        display_menu()  # Display the menu
        choice = input("Enter your choice: ")

        if choice == '1':
            add_item(shopping_list)  # Call the add_item function
        elif choice == '2':
            remove_item(shopping_list)  # Call the remove_item function
        elif choice == '3':
            view_list(shopping_list)  # Call the view_list function
        elif choice == '4':
            print("Goodbye!")
            break  # Exit the loop
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
