def encrypt(text, key):

    encrypted_text = ''
    for char in text:
        if char.isalpha():
            shift = (ord(char) + key - 65) % 26 + 65 if char.isupper() else (ord(char) + key - 97) % 26 + 97
            encrypted_text += chr(shift)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text, key):

    return encrypt(encrypted_text, -key)

def main():
    try:
        text = input("Enter the text to encrypt: ")
        key = int(input("Enter the encryption key (an integer): "))
        encrypted_text = encrypt(text, key)
        print("Encrypted text:", encrypted_text)
        
        decrypted_text = decrypt(encrypted_text, key)
        print("Decrypted text:", decrypted_text)
    except ValueError:
        print("Invalid input! Key must be an integer.")

if __name__ == "__main__":
    main()
