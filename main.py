from converter import roman_to_decimal 

accepted_roman = set(['I', 'V', 'X', 'L', 'C', 'D', 'M'])

def verify_input(user_input):
    if set(user_input) <= accepted_roman:
        return user_input
    else:
        raise ValueError('This is not a correct roman number')

if __name__ == "__main__":
    raw_input = input("enter a roman number: ")
    verify_input(raw_input)
    print (roman_to_decimal(raw_input))
