alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
def decrypt(original_text, shift_amount):
    shifted_number = []
    decoded_word = ""
    for letter in original_text:
        shifted_number.append(alphabet.index(letter) - shift_amount)
    #print(shifted_number)
    for number in shifted_number:
        index = number % len(alphabet)
        decoded_word += alphabet[index]
    print(f"Here is the decoded result: {decoded_word}")
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.
def caesar(direction):
    if direction == "encode":
        encrypt(original_text=text, shift_amount=shift)
    elif direction == "decode":
        decrypt(original_text=text, shift_amount=shift)
def encrypt(original_text, shift_amount):
    shifted_number = []
    encoded_word = ""
    for letter in original_text:
        shifted_number.append(alphabet.index(letter) + shift_amount)
    # print(shifted_number)
    for number in shifted_number:
        index = number % len(alphabet)
        encoded_word += alphabet[index]
    print(f"Here is the encoded result: {encoded_word}")


caesar(direction= direction)
