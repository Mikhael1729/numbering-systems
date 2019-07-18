import sys

""" 
Convert a number less than or equal to 255 to 
binary numbering system
"""
def convert_to_binary(number):
    # Powers of two from 7 to 0
    powers_of_two = [128, 64, 32, 16, 8, 4, 2, 1]

    # Sum addens (it's to calculate the result)
    addens = []

    # Rest of each powers_of_two element with number
    rest = number

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

    return addens

number = int(sys.argv[1])
addens = convert_to_binary(number)

print('CONVERSION')
print('----------')
print('')

for adden in addens:
    print(adden)
