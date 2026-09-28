#!/usr/bin/env python3
import os
import sys
import hashlib
from cryptography.fernet import Fernet, InvalidToken

KEY_ENV_VAR = "APP_ENCRYPTION_KEY"

def load_or_get_key() -> bytes:
    """Retrieves key from environment variable; exits securely if missing/invalid."""
    key = os.environ.get(KEY_ENV_VAR)
    if not key:
        print(f"[!] Error: Environment variable '{KEY_ENV_VAR}' is not set.")
        print(f"    Generate a key using: Fernet.generate_key().decode()")
        print(f"    Set it via: export {KEY_ENV_VAR}='your_key_here'")
        sys.exit(1)
    return key.encode()

def calculate_sha256(file_path: str) -> str:
    """Calculates SHA-256 hash of a file."""
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            while chunk := f.read(8192):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        print(f"[!] File not found: {file_path}")
        sys.exit(1)
    except Exception as e:
        print(f"[!] Error reading file '{file_path}': {e}")
        sys.exit(1)

def encrypt_file(input_file: str, output_file: str, key: bytes):
    """Encrypts input_file and saves output to output_file."""
    try:
        f = Fernet(key)
        with open(input_file, "rb") as file_in:
            data = file_in.read()
        encrypted_data = f.encrypt(data)
        with open(output_file, "wb") as file_out:
            file_out.write(encrypted_data)
        print(f"[+] File successfully encrypted: {output_file}")
    except FileNotFoundError:
        print(f"[!] File not found: {input_file}")
    except Exception as e:
        print(f"[!] Encryption failed: {e}")

def decrypt_file(input_file: str, output_file: str, key: bytes):
    """Decrypts input_file and saves output to output_file."""
    try:
        f = Fernet(key)
        with open(input_file, "rb") as file_in:
            encrypted_data = file_in.read()
        decrypted_data = f.decrypt(encrypted_data)
        with open(output_file, "wb") as file_out:
            file_out.write(decrypted_data)
        print(f"[+] File successfully decrypted: {output_file}")
    except FileNotFoundError:
        print(f"[!] File not found: {input_file}")
    except InvalidToken:
        print("[!] Decryption failed: Invalid key or corrupted payload.")
    except Exception as e:
        print(f"[!] Decryption failed: {e}")

def verify_integrity(original_file: str, decrypted_file: str):
    """Verifies SHA-256 match between two files."""
    hash_orig = calculate_sha256(original_file)
    hash_dec = calculate_sha256(decrypted_file)
    
    print(f"Original Hash:  {hash_orig}")
    print(f"Decrypted Hash: {hash_dec}")
    
    if hash_orig == hash_dec:
        print("[SUCCESS] File integrity verified: Hashes match.")
    else:
        print("[ALERT] File integrity check failed: Hashes DO NOT match!")

if __name__ == "__main__":
    key = load_or_get_key()
    
    # Example test usage:
    orig = "sample_students.csv"
    enc = "sample_students.csv.enc"
    dec = "sample_students_decrypted.csv"
    
    if os.path.exists(orig):
        print("--- 1. Encrypting File ---")
        encrypt_file(orig, enc, key)
        
        print("\n--- 2. Decrypting File ---")
        decrypt_file(enc, dec, key)
        
        print("\n--- 3. Integrity Check ---")
        verify_integrity(orig, dec)
    else:
        print(f"[!] Please create '{orig}' to test the script execution.")
