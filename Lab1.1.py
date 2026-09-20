alphabet = ["A", "Ă", "Â", "B", "C", "D", "E", "F", "G", "H",
            "I", "Î", "J", "K", "L", "M", "N", "O", "P", "Q",
            "R", "S", "Ș", "T","Ț", "U", "V", "W", "X", "Y", "Z"]

print("1. Encryption")
print("2. Decryption")

choice = int(input("Choose: "))

if choice == 1:
    text = input("Enter a message to encrypt: ")
    upper = text.upper()
    key = int(input("Enter the key: "))
    
    encryptedmessage = ""
    
    i = 0
    while i < len(upper):
        j = 0
        
        while j < len(alphabet):
            if upper[i] == alphabet[j]:
                encryptedmessage += alphabet[(j + key) % len(alphabet)]
                break
        
            j += 1
    
        i += 1

    print("The encrypted message: ", encryptedmessage)

elif choice == 2:
    text = input("Enter a message to decrypt: ")
    upper = text.upper()
    key = int(input("Enter the key: "))
    
    decryptedmessage = ""
    
    i = 0
    while i < len(upper):
        j = 0
        
        while j < len(alphabet):
            if upper[i] == alphabet[j]:
                decryptedmessage += alphabet[(j - key) % len(alphabet)]
                break
        
            j += 1
    
        i += 1

    print("The decrypted message: ", decryptedmessage)
