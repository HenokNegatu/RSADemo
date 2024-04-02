class RSA:
    """
    This function checks if a number is prime (has exactly two divisors: 1 and itself).
    """
    def is_prime(self, num):
    
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def gcd(a, b):
        """
        This function calculates the greatest common divisor (GCD) of two numbers.
        """
        while b != 0:
            a, b = b, a % b
        return a

    def generate_keypair(self, p, q):
        """
        This function generates a public/private key pair based on two prime numbers.
        """
        if not (self.is_prime(p) & self.is_prime(q)):
            raise ValueError("Both p and q must be prime numbers")
        n = p * q
        phi_n = (p - 1) * (q - 1)
        # Choose an integer e such that 1 < e < phi_n and gcd(e, phi_n) = 1
        e = 2  # You can modify this to choose a different valid 'e' value
        while self.gcd(e, phi_n) != 1:
            e += 1
        # d is the modular multiplicative inverse of e modulo phi_n
        d = pow(e, -1, phi_n)
        return ((e, n), (d, n))  # Public key, Private key

    def encrypt(self, pk, plaintext):
        """
        This function encrypts a plaintext message using the public key (e, n).
        """
        e, n = pk
        # Convert plaintext to ASCII integer list (assuming single-byte characters)
        text_ascii = [ord(char) for char in plaintext]
        # Encrypt each ASCII character using modular exponentiation
        cipher = [pow(char, e, n) for char in text_ascii]
        return cipher

    def decrypt(self, pk, ciphertext):
        """
        This function decrypts an encrypted message using the private key (d, n).
        """
        d, n = pk
        # Decrypt each ASCII character using modular exponentiation
        plain = [pow(char, d, n) for char in ciphertext]
        # Convert ASCII integers back to characters
        text = ''.join([chr(char) for char in plain])
        return text

if __name__ == "__main__": 
    # Example usage
    p = 11  # Replace with larger prime numbers for real use
    q = 13  # Same here
    
    

    print("Generating keypair...")
    public, private = generate_keypair(p, q)
    print("Public key:", public)
    print("Private key:", private)

    message = "This is a secret message"
    rsa = RSA()

    
    print("Encrypting message:", message)
    encrypted_message = RSA.encrypt(public, message)
    print("Encrypted message:", encrypted_message)

    print("Decrypting message...")
    decrypted_message = RSA.decrypt(private, encrypted_message)
    print("Decrypted message:", decrypted_message)
