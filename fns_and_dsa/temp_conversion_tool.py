FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        temperature = float(input("Enter the temperature to convert: "))  # Attempt to convert input to float
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
        if unit == 'C':
            converted_temperature = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is equal to {converted_temperature:.2f}°F")
        elif unit == 'F':
            converted_temperature = convert_to_celsius(temperature)
            print(f"{temperature}°F is equal to {converted_temperature:.2f}°C")
        else:
            raise ValueError("Invalid unit. Please enter 'C' or 'F'.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")  # Correct error message

# Tests (using pytest)
import temp_conversion_tool  # Make sure to import your script
import pytest
from unittest import mock

def test_celsius_to_fahrenheit_conversion(capsys):
    with mock.patch('builtins.input', side_effect=["30", "C"]):
        temp_conversion_tool.main()
    captured = capsys.readouterr()
    assert "30°C is equal to 86.00°F" in captured.out

def test_fahrenheit_to_celsius_conversion(capsys):
    with mock.patch('builtins.input', side_effect=["86", "F"]):
        temp_conversion_tool.main()
    captured = capsys.readouterr()
    assert "86°F is equal to 30.00°C" in captured.out

# Additional Test for Invalid Input
def test_invalid_temperature_input(capsys):
    with mock.patch('builtins.input', side_effect=["abc", "C"]):  
        temp_conversion_tool.main()
    captured = capsys.readouterr()
    assert "Invalid temperature. Please enter a numeric value." in captured.out

if __name__ == "__main__":
    main()