roman_decimal_table = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

def verify_input(user_input):
    if set(user_input) <= set([roman_key for roman_key in roman_decimal_table]):
        return user_input
    else:
        raise ValueError('This is not a correct roman number')

def convert_roman_to_decimal(roman):
    result = 0
    decimal_of_roman = list(map(lambda x: roman_decimal_table[x], roman))
    for index, decimal_value in enumerate(decimal_of_roman):
        if index < len(roman)-1:
            if decimal_value >= decimal_of_roman[index + 1]:
                result += decimal_value
            else:
                result -= decimal_value
        else:
            result += decimal_value
    return result
    

if __name__ == "__main__":
    raw_input = input("enter a roman number: ")
    verified_input = verify_input(raw_input)
    print(convert_roman_to_decimal(verified_input))
