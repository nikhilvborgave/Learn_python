alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def encrypt(original_text, shift_amount):

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

    shifted_number = []
    new_word = ""
    for letter in original_text:
        shifted_number.append(alphabet.index(letter) + shift_amount)
    #print(shifted_number)
    for number in shifted_number:

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?
        index = number % len(alphabet)
        new_word += alphabet[index]
    print(f"Here is the encoded result: {new_word}")

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.
encrypt(original_text= text, shift_amount= shift)
