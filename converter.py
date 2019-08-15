def decimal_val(roman_char):
    switcher = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000 
    }
    return switcher.get(roman_char)

def verify_roman_order(list, index):
    if (index == 0):
        return True
    if (index == len(list) -1):
        return True
    return list[index-1] >= list[index+1]

def roman_to_decimal(roman_number):
    total = 0
    converted_list = list(map(decimal_val, list(roman_number)))
    index_list = converted_list.copy()

    for val in converted_list:    
        i = index_list.index(val)
        index_list[i] = 0
        print("")
        print(converted_list, index_list)
        print("Processing %s (%de). Total avant=%d" % (val, i, total))
        if (i == len(roman_number) - 1):
            total += converted_list[i]
        else:
            if (converted_list[i] >= converted_list[i+1]):
                total += converted_list[i]
            if (converted_list[i] < converted_list[i+1]):
                if (verify_roman_order(converted_list, i)):
                    total -= converted_list[i]
                else:
                    raise ValueError('This is not a correct roman number')
    return total


if __name__ == "__main__":
    raw_input = input("enter a roman number: ")
    print (roman_to_decimal(raw_input))
