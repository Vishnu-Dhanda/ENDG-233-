# encryption.py
# VISHNU DHANDA, ENDG 233 F21
# A terminal-based encryption application capable of both encoding and decoding text when given a specific cipher.
# You may optionally import the string module from the standard Python library. No other modules may be imported.
# Remember to include docstrings for your functions and comments throughout your code.

### Define your functions here
def check_unique_characters(cipher):
    """Function checks cipher inputted by user for unique characters.
    
    Parameters:
    cipher -- string representing the cipher text inputted by the user.

    Return:
    Function returns a boolean (True or False) value.
    True - if the cipher contains unique characters.
    False - if cipher does not contain unique characters.
    """
    cipher_set = set(cipher) #converts cipher string inputted by user into a set.
    return(len(cipher) == len(cipher_set)) #checks if length of the string is equal to length of the elements in the set.

def check_special_characters(cipher):
    """Function checks cipher inputted by user for special characters such as !,@,#,$,%,^,* .etc 
    
    Parameters:
    cipher -- string representing the cipher text inputted by the user.

    Return:
    Function returns a boolean (True or False) value.
    True -- if the cipher does not contain special characters.
    False -- if cipher contains special characters.
    """
    return cipher.isalnum() #inbuilt isalnum function used to checks the cipher for special characters

def encode (text_to_encode):
    """
    Function uses the output_dict_encode dictionary to convert the text entered by the user into a encoded text
    as per requirement of the inputted cipher. It then displays / prints the encoded text.

    Parameters:
    text_to_encode -- string representing the text inputted by the user which they would like to encode according to
    a given cipher.

    Return: prints / displays the encoded text to the user.
    """
    output = ''
    #while loop iterates through each character in the text_to_encode inputted by the user and checks its corresponding value in the output_dict_encode.
    #It creates a string of the ciphered text which is assigned a variable output.
    i = 0 #initialize i
    while i < len(text_to_encode): #executes the while loop as long as condition is true
        if text_to_encode[i] in output_dict_encode:
            output = output + output_dict_encode[text_to_encode[i]]
        i = i + 1 #increment i
    return print(f'Your output is: {output}') 

def decode(text_to_decode):
    """Function uses the output_dict_decode dictionary to convert the text entered by the user into a decoded text
    as per requirement of the inputted cipher. It then displays / prints the encoded text.

    Parameters:
    text_to_decode -- string representing the text inputted by the user which they would like to decode according to
    a given cipher.

    Return: prints / displays the encoded text to the user.
    """
    output = ''
    i = 0 
    #while loop iterates through each character in the text_to_decode inputted by the user and checks its corresponding value in the output_dict_decode.
    #It creates a string of the deciphered text which is assigned a variable output.
    while i < len(text_to_decode): #executes the while loop as long as condition is true
        if text_to_decode[i] in output_dict_decode:
            output = output + output_dict_decode[text_to_decode[i]]
        i = i + 1 #increment i
    return print(f'Your output is: {output}')

print("ENDG 233 Encryption Program")
print('')
### Add your main program code here'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
option_selected = input('Select 1 to encode or 2 to decode your message, select 0 to quit: ')
#Executes the while loop as long as this condition is true, If not the program prints the final 'Thank you for using the encryption program.'
#message and terminates.
while option_selected != '0': 
    if option_selected  == '1':
        text_to_encode = input('Please enter the text to be encoded: ')
        text_to_encode = text_to_encode.lower() #converts any uppercase characters in text_to_encode to lowercase.
        cipher = input('Please enter the cipher text: ')

        #checks if cipher meets the requirements: If its length is 26 characters, If the characters entered are unique, no repeats
        #and if any special characters are entered.
        if len(cipher) != 26 or check_unique_characters(cipher) == False or check_special_characters(cipher) == False:
            print('Your cipher must contain 26 unique elements of a-z or 0-9.') #if cipher does not meet the requirements the following message is displayed
            print('')
        else:
            print('Your cipher is valid.')
            keys = alphabet 
            values = cipher
            output_dict_encode = dict(zip(keys, values)) #maps each character in alphabet to the corresponding character in the inputted cipher according to the character position.
                                                         #uses the alphabet characters as the keys and the cipher characters as the corresponding values.
            encode(text_to_encode) #passes the text_to_encode inputted by the user into the encode function.
            print('')
    
    if option_selected == '2':
        text_to_decode = input('Please enter the text to be decoded: ')
        text_to_decode = text_to_decode.lower()
        cipher = input('Please enter the cipher text: ')

        #checks if cipher meets the requirements: If its length is 26 characters, If the characters entered are unique, no repeats
        #and if any special characters are entered.
        if len(cipher) != 26 or check_unique_characters(cipher) == False or check_special_characters(cipher) == False:
            print('Your cipher must contain 26 unique elements of a-z or 0-9.') #if cipher does not meet the requirements the following message is displayed
            print('')
        else:
            print('Your cipher is valid.')
            keys = cipher
            values = alphabet
            output_dict_decode= dict(zip(keys, values)) #maps each character in the inputted cipher to the corresponding character in the alphabet according to the character position.
                                                        #uses the cipher characters as the keys and the alphabet characters as the corresponding values.
            decode(text_to_decode) #passes the text_to_decode inputted by the user into the decode function.
            print('')
    
    option_selected = input('Select 1 to encode or 2 to decode your message, select 0 to quit: ') #If an invalid cipher is provided, user is prompted for re-entry without terminating the program
print('Thank you for using the encryption program.') #If user selects option 0 this message is displayed and the program is terminated.