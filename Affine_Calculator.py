#Below is a Python script that calculates the values of aa and bb, decrypts or encrypts text,
#  and handles user input to determine what is missing. The script uses the affine cipher and
#  allows the user to provide any combination of aa, bb, plaintext, or encrypted text, and 
# it will calculate the missing values


def extended_gcd(a, b):
    """Extended Euclidean Algorithm to find the modular inverse."""
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x

def mod_inverse(a, m):
    """Find the modular inverse of a modulo m."""
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise ValueError("Modular inverse does not exist.")
    else:
        return x % m

def affine_encrypt(plaintext, a, b):
    """Encrypt plaintext using the affine cipher."""
    encrypted_text = ""
    for char in plaintext.upper():
        if char.isalpha():
            x = ord(char) - ord('A')
            y = (a * x + b) % 26
            encrypted_text += chr(y + ord('A'))
        else:
            encrypted_text += char
    return encrypted_text

def affine_decrypt(ciphertext, a, b):
    """Decrypt ciphertext using the affine cipher."""
    decrypted_text = ""
    a_inv = mod_inverse(a, 26)
    for char in ciphertext.upper():
        if char.isalpha():
            y = ord(char) - ord('A')
            x = (a_inv * (y - b)) % 26
            decrypted_text += chr(x + ord('A'))
        else:
            decrypted_text += char
    return decrypted_text

def find_a_b(plaintext, ciphertext):
    """Find a and b given plaintext and ciphertext."""
    if len(plaintext) != len(ciphertext):
        raise ValueError("Plaintext and ciphertext must be of the same length.")
    
    # Use the first two letters to set up equations
    x1 = ord(plaintext[0].upper()) - ord('A')
    y1 = ord(ciphertext[0].upper()) - ord('A')
    x2 = ord(plaintext[1].upper()) - ord('A')
    y2 = ord(ciphertext[1].upper()) - ord('A')
    
    # Solve for a and b
    try:
        a = (y2 - y1) * mod_inverse(x2 - x1, 26) % 26
        b = (y1 - a * x1) % 26
        return a, b
    except ValueError:
        raise ValueError("No valid a and b found for the given plaintext and ciphertext.")

def main():
    print("Affine Cipher Tool")
    print("What do you have?")
    print("1. a and b, and plaintext")
    print("2. a and b, and ciphertext")
    print("3. Plaintext and ciphertext (find a and b)")
    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == '1':
        a = int(input("Enter the value of a: "))
        b = int(input("Enter the value of b: "))
        plaintext = input("Enter the plaintext: ")
        ciphertext = affine_encrypt(plaintext, a, b)
        print(f"Encrypted text: {ciphertext}")

    elif choice == '2':
        a = int(input("Enter the value of a: "))
        b = int(input("Enter the value of b: "))
        ciphertext = input("Enter the ciphertext: ")
        plaintext = affine_decrypt(ciphertext, a, b)
        print(f"Decrypted text: {plaintext}")

    elif choice == '3':
        plaintext = input("Enter the plaintext: ")
        ciphertext = input("Enter the ciphertext: ")
        try:
            a, b = find_a_b(plaintext, ciphertext)
            print(f"Found a = {a}, b = {b}")
            print(f"Decrypted text: {affine_decrypt(ciphertext, a, b)}")
        except ValueError as e:
            print(e)

    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()