class IntegerToRoman:
    def __init__(self, number):
        """Initialize the object with an integer number"""
        if not isinstance(number, int):
            raise ValueError("Input must be an integer")
        if number <= 0 or number > 3999:
            raise ValueError("Number must be between 1 and 3999")
        self.number = number

    def convert(self):
        """Convert the integer to a Roman numeral"""
        value_map = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        
        result = ""
        num = self.number

        for value, symbol in value_map:
            while num >= value:
                result += symbol
                num -= value

        return result


# Example usage
num = 1994
converter = IntegerToRoman(num)
print(f"Integer: {num} -> Roman Numeral: {converter.convert()}")

num = 58
converter = IntegerToRoman(num)
print(f"Integer: {num} -> Roman Numeral: {converter.convert()}")
