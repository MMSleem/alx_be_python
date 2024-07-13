def perform_operation(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        try:
            result = num1 / num2
            if num2 == 0:
                return "Division by zero is undefined."
            else:
                return result
        except ZeroDivisionError:
            return "Error: Division by zero is not allowed."
    else:
        return "Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'."
