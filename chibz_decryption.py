def decrypt(data, key):
    decrypted_data = ""
    for char in data:
        if char.isalpha():
            shift = key % 26
            if char.islower():
                decrypted_data += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                decrypted_data += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        else:
            decrypted_data += char
    return decrypted_data

LOG_FILE = "keystrokes.log"  
ENCRYPTION_KEY = 5  

try:
    with open(LOG_FILE, "r") as f:
        encrypted_lines = f.readlines()

    for line in encrypted_lines:
        timestamp, encrypted_text = line.strip().split("] ")
        encrypted_text = encrypted_text.strip()

        decrypted_text = decrypt(encrypted_text, ENCRYPTION_KEY)

        print(f"{timestamp}] {decrypted_text}")

except FileNotFoundError:
    print(f"Error: The file '{LOG_FILE}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")


with open("decrypted_keystrokes.log", "w") as f:
    for line in encrypted_lines:
        timestamp, encrypted_text = line.strip().split("] ")
        encrypted_text = encrypted_text.strip()
        decrypted_text = decrypt(encrypted_text, ENCRYPTION_KEY)
        f.write(f"{timestamp}] {decrypted_text}\n")

print("Decryption complete. Saved to 'decrypted_keystrokes.log'.")