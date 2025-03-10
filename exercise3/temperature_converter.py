# Exercise 3: Temperature Converter
from typing import Union

# Defining a Temperature type for cleaner type hints
Temperature = Union[int, float]


def celsius_to_fahrenheit(celsius: Temperature) -> float:
    """
    Convert temperature from Celsius to Fahrenheit.

    Formula: F = C × 9/5 + 32

    Args:
        celsius: Temperature in Celsius

    Returns:
        Temperature in Fahrenheit (rounded to 2 decimal places)
    """
    a = 9/5
    b = 32
    return round(celsius * a + b, 2)
    pass


def fahrenheit_to_celsius(fahrenheit: Temperature) -> float:
    """
    Convert temperature from Fahrenheit to Celsius.

    Formula: C = (F - 32) × 5/9

    Args:
        fahrenheit: Temperature in Fahrenheit

    Returns:
        Temperature in Celsius (rounded to 2 decimal places)
    """
    a = 32
    b = 5/9
    return round((fahrenheit - a) * b, 2)
    pass


def celsius_to_kelvin(celsius: Temperature) -> float:
    """
    Convert temperature from Celsius to Kelvin.

    Formula: K = C + 273.15

    Args:
        celsius: Temperature in Celsius

    Returns:
        Temperature in Kelvin (rounded to 2 decimal places)
    """
    a = 273.15
    return round(celsius + a, 2)
    pass


def kelvin_to_celsius(kelvin: Temperature) -> float:
    """
    Convert temperature from Kelvin to Celsius.

    Formula: C = K - 273.15

    Args:
        kelvin: Temperature in Kelvin

    Returns:
        Temperature in Celsius (rounded to 2 decimal places)

    Raises:
        ValueError: If kelvin is less than 0 (below absolute zero)
    """
    a = 273.15
    if kelvin < 0:
        raise ValueError("Temperature cannot be below absolute zero)")
    return round(kelvin - a, 2)
    pass
