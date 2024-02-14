# Kyle Dencker
# Petey Message Decoder

# Decodes the message
def decrypt(message, key):
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    translated = ""
    
    for letter in message:
        if letter in LETTERS:
            value = chr((ord(letter) - ord('A') - key) % 26 + ord('A'))
            translated += value
        else:
            translated += letter
            
    return translated

def main():
    # Welcome Message
    print("Welcome to the Petey Message Decoder")
    print("------------------------------------")
    print("We will be trying to decode messages from Petey.")

    message = input("Please enter a message:\n")

    # Output's possible answers
    print("Generating Possible Outputs:")
    print("----------------------------")

    for num in range(1, 26):
        print("Key #", num, ": ", decrypt(message, num), sep="")

    print("----------------------------")
    print("Done")



main()
