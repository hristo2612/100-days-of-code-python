# A program that 'encodes' & 'decodes' a message using Ceasar Cipher
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

finished = False


def encrypt(text, shift):
    # Put the last Shift N numbers of the array in front.
    encrypted_alphabet = [*alphabet[shift:], *alphabet[:shift]]
    print(alphabet)
    print(encrypted_alphabet)
    encrypted_text = ""
    for char in text:
        encrypted_char = char
        if char in alphabet:
            print(alphabet.index(char), char)
            encrypted_char = encrypted_alphabet[alphabet.index(char)]
        encrypted_text += encrypted_char

    print(f"Here's the encoded result: {encrypted_text}")


def decrypt(text, shift):
    encrypted_alphabet = [*alphabet[shift:], *alphabet[:shift]]
    decrypted_text = ""
    for char in text:
        decrypted_char = char
        if char in alphabet:
            decrypted_char = alphabet[encrypted_alphabet.index(char)]
        decrypted_text += decrypted_char

    print(f"Here's the decoded result: {decrypted_text}")


while not finished:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)
    else:
        print("Invalid method, exiting program.")
        finished = True

    go_again = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'\n")
    if go_again == "no":
        finished = True
