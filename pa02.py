'''
/*=============================================================================
| Assignment: pa02 - Calculating an 8, 16, or 32 bit
| checksum on an ASCII input file
|
| Author: Bryce Kelly
| Language: Python
|
| To Compile:
| python pa02.py //Caution - expecting input parameters
|
| To Execute:
| or python-> python3 pa02.py inputFile.txt 8
| where inputFile.txt is an ASCII input file
| and the number 8 could also be 16 or 32
| which are the valid checksum sizes, all
| other values are rejected with an error message
| and program termination
|
| Note: All input files are simple 8 bit ASCII input
|
| Class: CIS3360 - Security in Computing - Summer 2023
| Instructor: McAlpin
| Due Date: 07/23/23
|
+=============================================================================*/
'''

# python: prompt$python3 pa02.py
# bash pa02test.sh pa02.c

import sys

def wrap_text(text, width):
    lines = []
    for i in range(0, len(text), width):
        lines.append(text[i:i + width])
    return '\n'.join(lines)
def convert_to_hex(line, m):
    ascii_values = " ".join(hex(ord(letter))[2:] for letter in line)
    ascii_values = ascii_values.split()
    ascii_values.pop()
    ascii_values.append("0a")
    return ascii_values
def calculate_checksum16(hex_numbers):
    bytes_data = bytes.fromhex(hex_numbers)

    
    checksum = 0


    for i in range(0, len(bytes_data), 2):
        byte_pair = bytes_data[i:i + 2]
        value = int.from_bytes(byte_pair, byteorder='big', signed=False)
        checksum = (checksum + value) & 0xFFFF


    checksum_hex = format(checksum, '04X').lower()

    return checksum_hex

def read_file(file_path, bitsum):
    try:
        file = open(file_path, 'r')
        content = file.read()
        h_values = convert_to_hex(content,1)
        if bitsum == 8:
            total = 0
            for x in h_values:
                x = int(x, 16)
                total+= x
            total &= 0xFF
            total = format(total, '02x')
            wrapped_content = wrap_text(content, 80)
            print("\n"+wrapped_content)
            print("{} bit checksum is {} for all {} chars\n".format(bitsum, total, int((len(content)*1))))
        elif bitsum == 16:
            
            hex_numbers = convert_to_hex(content,2)
            separator = ', '
            single_string = separator.join(hex_numbers)
            single_string2 = " "
            for l in single_string:
                if l == ",":
                    continue
                else:
                    single_string2 += l
            wrapped_content = wrap_text(content, 80)
            print("\n"+wrapped_content)
            carry = 0
            if len(hex_numbers)%2 != 0:
                single_string2 += " 58"
                print("X")
                carry += 1
            
            checksum = calculate_checksum16(single_string2)
            print("{} bit checksum is {} for all {} chars\n".format(bitsum, checksum, int((len(content)*1)+carry)))
        
        file.close()
        

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading the file: {e}")
        sys.exit(1)

file_path = sys.argv[1]
bitsum = int(sys.argv[2])

read_file(file_path, bitsum)


'''
/*=============================================================================
| I [Bryce Kelly] ([br284128]) affirm that this program is
| entirely my own work and that I have neither developed my code together with
| any another person, nor copied any code from any other person, nor permitted
| my code to be copied or otherwise used by any other person, nor have I
| copied, modified, or otherwise used programs created by others. I acknowledge
| that any violation of the above terms will be treated as academic dishonesty.
+============================================================================*/
'''