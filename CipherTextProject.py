start = input("Type encode to Encrypt or decode to Decrypt\n")
message = input("Type your Message to Encrypt\n")
shift = int(input("Type you shift amount\n"))

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt(original_text,shift_amount):
    ciphertext = ""
    for i in original_text:
        a = alphabets.index(i) + shift_amount
        if a > len(alphabets)-1:
            a = a - len(alphabets)
        ciphertext+=alphabets[a]
    print(f"Encrypted version: {ciphertext}")   
encrypt(message,shift)

#decryption
def decrypt(original_text,shift_amount):
    ciphertext = ""
    for i in original_text:
        a = alphabets.index(i) - shift_amount
        if a > len(alphabets)-1:
            a = a - len(alphabets)
        ciphertext+=alphabets[a]
    print(f"Decrypted version: {ciphertext}") 
decrypt(message,shift)