# Number Digit Analyzer
# This script finds 4-digit numbers where:
# 1. First two digits are even (and hundreds is not zero)
# 2. Last two digits are odd

def find_special_numbers():
    number = 1000
    while number <= 9999:
        temp_n = number
        
        # Extracting digits
        ones_digit = temp_n % 10
        temp_n //= 10
        
        tens_digit = temp_n % 10
        temp_n //= 10
        
        hundreds_digit = temp_n % 10
        temp_n //= 10
        
        thousands_digit = temp_n
        
        # Conditions
        last_two_are_odd = (ones_digit % 2 != 0) and (tens_digit % 2 != 0)
        first_two_are_even = (hundreds_digit % 2 == 0) and (thousands_digit % 2 == 0)
        hundreds_is_not_zero = (hundreds_digit != 0)
        
        if last_two_are_odd and first_two_are_even and hundreds_is_not_zero:
            print(f"Found: {number}")
            
        number += 1

if __name__ == "__main__":
    find_special_numbers()
