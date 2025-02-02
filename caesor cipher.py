def caesar_cipher(plain_text, shift):
    cipher_text = ""
    for char in plain_text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                shifted_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                shifted_char = chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            cipher_text += shifted_char
        else:
            cipher_text += char
    return cipher_text

if __name__ == "__main__":
    plain_text = input("Enter the plain text: ")
    shift = int(input("Enter the shift value: "))
    cipher_text = caesar_cipher(plain_text, shift)
    print("Cipher text:", cipher_text)