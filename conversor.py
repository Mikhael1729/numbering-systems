""" 
Convert a number less than or equal to 255 to 
binary numbering system
"""
def convert_to_binary(number):
    # Number in binary
    converted = ''

    # Powers of two from 7 to 0
    powers_of_two = [128, 64, 32, 16, 8, 4, 2, 1]

    # Rest of each powers_of_two element with number
    rest = number

    for n in powers_of_two:
        rest -= n  
        
        if rest >= 0:
            converted += '1'
        else:
            rest += n
            converted += '0'

    return converted

"""
Convert any number to binary numbering system
"""
def convert_any_number_to_binary(number):
    print('Doing something')

"""
Testing
"""
converted1 = convert_to_binary(2)
converted2 = convert_to_binary(80)
converted3 = convert_to_binary(105)
converted4 = convert_to_binary(255)

print('converted1 ->', converted1)
print('converted2 ->', converted2)
print('conterted3 ->', converted3)
print('converted4 ->', converted4)

