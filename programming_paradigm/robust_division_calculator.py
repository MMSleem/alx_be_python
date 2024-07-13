# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        # Convert inputs to floats
        num = float(numerator)
        denom = float(denominator)

        # Perform division and handle division by zero
        result = num / denom
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."


if __name__ == "__main__":
    # Example usage
    # Expected output: The result of the division is 2.0
    print(safe_divide(10, 5))
    print(safe_divide(10, 0))  # Expected output: Error: Cannot divide by zero.
    # Expected output: Error: Please enter numeric values only.
    print(safe_divide("ten", 5))
