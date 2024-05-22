from random import randint

class RSA:
    
    def __init__(self) -> None:
        self.private = ""
        self.public = ""
    """
    check if a number is prime.
    """
    def is_prime(self, num):
    
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def gcd(self, a, b):
        """
        calculate the greatest common divisor (GCD) of two numbers.
        """
        while b != 0:
            a, b = b, a % b
        return a

    def generate_prime(self):
        """
        Generates a random prime number.
        """
        while True:
            # Focus on odd numbers (except 2, the only even prime)
            num = randint(2, 100)  # You can adjust the upper limit for larger primes
            if num % 2 != 0 and self.is_prime(num):
                return num
            
    def generate_keypair(self):
        print("generaing key pair...")
        p =  self.generate_prime()
        q = self.generate_prime()
        n = p * q
        z = (p - 1) * (q - 1)
        # Choose an integer e such that 1 < e < z and gcd(e, z) = 1
        e = 2  # You can modify this to choose a different valid 'e' value
        while self.gcd(e, z) != 1:
            e += 1
        # d is the modular multiplicative inverse of e modulo z
        d = pow(e, -1, z)
        self.public = (e,n)
        self.private = (d,n)
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
    
    def encryptPipline(self,public_key, fileByte):
        return self.encrypt(public_key, fileByte)
    
    def decryptPipline(self, cipher):
        return self.decrypt(self.private, cipher)

if __name__ == "__main__": 
    

    message = "This is a secret message"
    rsa = RSA()
    (private, public)=rsa.generate_keypair()
    print("Encrypting message:", message)
    encrypted_message = rsa.encryptPipline(message)
    print(f"Encrypted message: {encrypted_message} \n")

    print("Decrypting message...")
    decrypted_message = rsa.decryptPipline(encrypted_message)
    print("Decrypted message:", decrypted_message)


