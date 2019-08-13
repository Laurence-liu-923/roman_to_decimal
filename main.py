#Roman - decimal
# I - 1
# V - 5
# X - 10
# L - 50
# C - 100
# D - 500
# M - 1000

accepted_roman = set(['I', 'V', 'X', 'L', 'C', 'D', 'M'])

def verify_input(user_input):
    if set(user_input) <= accepted_roman:
        return user_input
    else:
        raise ValueError('This is not a correct roman number')

if __name__ == "__main__":
    raw_input = input("enter a roman number: ")
    verify_input(raw_input)
