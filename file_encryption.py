
from pathlib import Path
from cryptography.fernet import Fernet, InvalidToken


def generate_key():
    """Generate and save a new encryption key."""
    key = Fernet.generate_key()
    Path("secret.key").write_bytes(key)
    print("Encryption key saved to secret.key")
    print("Keep this key private and make a secure backup.")


def load_key():
    """Load the existing encryption key."""
    key_path = Path("secret.key")

    if not key_path.is_file():
        print("Error: secret.key not found. Generate a key first.")
        return None

    return key_path.read_bytes()


def encrypt_file(file_path):
    """Encrypt a file and save it with the .encrypted extension."""
    path = Path(file_path)

    if not path.is_file():
        print("Error: File not found.")
        return

    if path.name == "secret.key" or path.suffix == ".encrypted":
        print("Error: Choose a normal file to encrypt.")
        return

    key = load_key()
    if key is None:
        return

    try:
        encrypted_data = Fernet(key).encrypt(path.read_bytes())
        output_path = Path(str(path) + ".encrypted")
        output_path.write_bytes(encrypted_data)
        print(f"Encryption successful: {output_path}")
    except (OSError, ValueError) as error:
        print(f"Encryption failed: {error}")


def decrypt_file(file_path):
    """Decrypt a .encrypted file into a separate output file."""
    path = Path(file_path)

    if not path.is_file():
        print("Error: File not found.")
        return

    if not path.name.endswith(".encrypted"):
        print("Error: Choose a file ending in .encrypted.")
        return

    key = load_key()
    if key is None:
        return

    try:
        decrypted_data = Fernet(key).decrypt(path.read_bytes())
        output_path = Path(str(path)[:-len(".encrypted")] + ".decrypted")
        output_path.write_bytes(decrypted_data)
        print(f"Decryption successful: {output_path}")
    except InvalidToken:
        print("Decryption failed: Wrong key or file was modified.")
    except OSError as error:
        print(f"Decryption failed: {error}")


def main():
    print("\n=== File Encryption Tool ===")
    print("1. Generate encryption key")
    print("2. Encrypt a file")
    print("3. Decrypt a file")
    print("4. Exit")

    choice = input("Choose an option (1-4): ").strip()

    if choice == "1":
        generate_key()
    elif choice == "2":
        encrypt_file(input("Enter file path: ").strip().strip('"'))
    elif choice == "3":
        decrypt_file(input("Enter encrypted file path: ").strip().strip('"'))
    elif choice == "4":
        print("Goodbye.")
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
