# oop/class_static_methods_demo.py

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method that adds two numbers.
        Does not use class or instance attributes.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method that multiplies two numbers.
        Prints the class attribute 'calculation_type' before returning the result.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
