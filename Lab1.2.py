alphabet = ["A", "Ă", "Â", "B", "C", "D", "E", "F", "G", "H",
            "I", "Î", "J", "K", "L", "M", "N", "O", "P", "Q",
            "R", "S", "Ș", "T","Ț", "U", "V", "W", "X", "Y", "Z"]

print("1. Encryption")
print("2. Decryption")

choice = int(input("Choose: "))

if choice == 1:
    text = input("Enter a message to encrypt: ")
    upper = text.upper()
    
    key1 = int(input("Enter the first key: "))
    key2 = input("Enter the second key: ").upper()
    
    if len(key2) < 7:
        print("The second key must have at least 7 letters.")
        exit()
    else:
        i = 0
        while i < len(key2):
            j = 0
        
            while j < len(alphabet):
                if key2[i] == alphabet[j]:
                    break

                j += 1
        
            if j == len(alphabet):
                print("The key must contain only letters.")
                break

            i += 1

    keyArray = []

    i = 0

    while i < len(key2):
        j = 0

        while j < len(keyArray):
            if key2[i] == keyArray[j]:
                break

            j += 1

        if j == len(keyArray):
            keyArray.append(key2[i])

        i += 1
    
    i = 0

    while i < len(alphabet):
        j = 0

        while j < len(keyArray):
            if alphabet[i] == keyArray[j]:
                break

            j += 1

        if j == len(keyArray):
            keyArray.append(alphabet[i])

        i +=1
    
    print("Key 2:", keyArray)

    encryptedmessage = ""
    
    i = 0
    keyPosition = 0

    while i < len(upper):
        j = 0
        
        while j < len(alphabet):
            if upper[i] == alphabet[j]:
                k = 0

                while k < len(alphabet):
                    if keyArray[keyPosition] == alphabet[k]:
                        encryptedmessage += alphabet[(j + key1 + k) % len(alphabet)]
                        break
                    
                    k += 1

                break
        
            j += 1
    
        i += 1
        keyPosition += 1

        if keyPosition == len(keyArray):
            keyPosition = 0

    print("The encrypted message: ", encryptedmessage)

elif choice == 2:
    text = input("Enter a message to decrypt: ")
    upper = text.upper()
    
    key1 = int(input("Enter the first key: "))
    key2 = input("Enter the second key: ").upper()
    
    if len(key2) < 7:
        print("The second key must have at least 7 letters.")
        exit()
    else:
        i = 0
        while i < len(key2):
            j = 0

            while j < len(alphabet):
                if key2[i] == alphabet[j]:
                    break

                j += 1

            if j == len(alphabet):
                print("The key must contain only letters.")
                break

            i += 1

    keyArray = []

    i = 0

    while i < len(key2):
        j = 0

        while j < len(keyArray):
            if key2[i] == keyArray[j]:
                break

            j += 1

        if j == len(keyArray):
            keyArray.append(key2[i])

        i += 1
    
    i = 0

    while i < len(alphabet):
        j = 0

        while j < len(keyArray):
            if alphabet[i] == keyArray[j]:
                break

            j += 1

        if j == len(keyArray):
            keyArray.append(alphabet[i])

        i +=1

    print("Key 2:", keyArray)

    decryptedmessage = ""
    
    i = 0
    keyPosition = 0

    while i < len(upper):
        j = 0
        
        while j < len(alphabet):
            if upper[i] == alphabet[j]:
                k = 0

                while k < len(alphabet):
                    if keyArray[keyPosition] == alphabet[k]:
                        decryptedmessage += alphabet[(j - key1 + k) % len(alphabet)]
                        break
                    
                    k += 1

                break
        
            j += 1
    
        i += 1
        keyPosition += 1

        if keyPosition == len(keyArray):
            keyPosition = 0

    print("The decrypted message: ", decryptedmessage)

