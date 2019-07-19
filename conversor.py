import sys

"""
"Normalize" two binary numbers

That means if the numbers has different lenght correct it
adding 0s to the number with minor digits of the other one

return Array of strings
"""
def normalize_binary_numbers(number1, number2):
    len1 = len(number1)
    len2 = len(number2)

    if len1 == len2:
        return [number1, number2]
    
    normalized_number1 = number1
    normalized_number2 = number2

    if len1 > len2:
        for i in range(len1 - len2):
            normalized_number2 = '0' + normalized_number2
    else:
        for i in range(len2 - len1):
           normalized_number1 = '0' + normalized_number1

    return [normalized_number1, normalized_number2]

"""
Sum two binary numbers

return String
"""
def sum(number1, number2):
    normalization = normalize_binary_numbers(number1, number2)
    
    n1 = normalization[0]
    n2 = normalization[1]
    result = '' # Result
    c = '0' # Carrier

    for i in range(len(n1) - 1, -1, -1):
        # Operation: 0 + 0
        if (n1[i] == '0' and  n2[i] == '0'):
            if c == '0':
                result = '0' + result
            else:
                result = '1' + result
                c = '0'
        # Operation 0 + 1
        elif ((n1[i] == '0' and n2[i] == '1') or (n2[i] == '0' and n1[i] == '1')):
            if c == '0':
                result = '1' + result
            else:
                result = '0' + result
                c = '1'
        # Operation 1 + 1
        else: 
            if c == '0':
                result = '0' + result
                c = '1'
            else:
                result = '1' + result
                c = '1'
    
    if c == '1':
        result = c + result

    return result

""" 
Convert a decimal number to binary

This function uses the method of successive 
subtractions to convert the number to binary
numbering system.
"""
def convert_to_binary(number):
    # Powers of two from 7 to 0
    powers_of_two = [128, 64, 32, 16, 8, 4, 2, 1]

    # Sum addens (it's to calculate the result)
    addens = []

    # Rest of each powers_of_two element with number
    rest = number

    # Compute addens
    while(rest != 0):
        converted = ''
        
        for n in powers_of_two:
            rest -= n  
            
            if rest >= 0:
                converted += '1'
            else:
                rest += n
                converted += '0'

        addens.append(converted)

    # Sum addens
    result = '0'
    for adden in addens:
        result = sum(adden, result)

    return result
