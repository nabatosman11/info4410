from pqcrypto.kem.kyber512 import generate_keypair, encrypt, decrypt

def ml_kem_example():
    print(" ML-KEM (Kyber512) Key Encapsulation Example")

    public_key, secret_key = generate_keypair()
    print("Keypair generated")

    ciphertext, shared_secret_enc = encrypt(public_key)
    print(" Shared secret encapsulated")

    shared_secret_dec = decrypt(ciphertext, secret_key)
    print(" Shared secret decapsulated")

    assert shared_secret_enc == shared_secret_dec, " Shared secrets do not match!"
    print(" Shared secrets match! Secure communication possible.")

if __name__ == "__main__":
    ml_kem_example()
