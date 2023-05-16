
#cipher_text = (text, shift_key) mod 26 -> 26 characters in English Alphabet
def encrypt(text, shift):

    encrypted_text = " "
    
    #iterating through every character in the input string
    for i in range(len(text)):
        char = text[i]#getting individual characters of text then assign it to variable char

        #if the text is character is uppercase
        if char.isupper():
            #convert the character into its equivalent integer value
            #appply shift to the individual character
            #upper case letters in ascii starts in 65
            # A -> 65
            encrypted_text = encrypted_text + chr((ord(char) + shift - 65) % 26 + 65) 
    
        #lower case characters
        #lower case letters in ascii starts in 97
        # a -> 97
        else:
            encrypted_text = encrypted_text + chr((ord(char) + shift - 97) % 26 + 97) 

    return encrypted_text

def decrypt(text,shift):

    decrypted_text = " "
    #iterating through every character in the input string
    for i in range(len(text)):
        char = text[i]

        #if the text is character is uppercase
        if char.isupper():
            #convert the character into its equivalent integer value
            #appply shift to the individual character
            #upper case letters in ascii starts in 65
            # A -> 65
            decrypted_text = decrypted_text + chr((ord(char) - shift - 65) % 26 + 65) 
    
        #lower case characters
        #lower case letters in ascii starts in 97
        # a -> 97
        else:
            decrypted_text = decrypted_text + chr((ord(char) - shift - 97) % 26 + 97) 

    return decrypted_text

def file_input(text_file):

    with open(text_file) as f:
        contents = f.read()
        print("[1] - ENCRYPT") 
        print("[2] - DECRYPT")
        option = input()

        if option == '1':
            shift = int(input("Enter the shift value: "))
            encrypted = encrypt(contents, shift)
            print(encrypted)
        elif option == '2':
            shift = int(input("Enter the shift value: "))
            decrypted = encrypt(contents, shift)
            print(decrypted)

def main():
    
    print("WELCOME TO CEASAR CYPHER TOOL")
    print("SELECT THE FOLLOWING OPTIONS TO START")
    print("[1] = ENCRYPT")
    print("[2] = DECRYPT")
    print("[3] = ATTACH FILE")
    option = input()
    
    if option == '1':
        text = input("Enter the string: ")
        shift = int(input("Enter the shift value: "))
        encrypted = encrypt(text, shift)
        print(encrypted)
    elif option == '2':
        text = input("Enter the string: ")
        shift = int(input("Enter the shift value: "))
        decrypted = decrypt(text, shift)
        print(decrypted)
    elif option == '3':
        print("Enter FIle name with file extension: ")
        input_file = input()
        file_input(input_file)
    else:
        print("Improper Input")
main()