# Advanced Keystroke Logger with Encryption

## Overview
This project is an advanced keystroke logging system designed for secure and efficient keystroke capture with encryption. The logger operates in the background, recording all keystrokes with timestamps while ensuring that logged data remains encrypted for security. The implementation leverages Python's `pynput` library for capturing keystrokes and employs a Caesar cipher for basic encryption.

## Features
- **Real-Time Keystroke Logging**: Captures all keystrokes, including alphanumeric keys and special characters.
- **Encryption Mechanism**: Implements a Caesar cipher for obfuscating logged keystrokes.
- **Timestamps for Activity Tracking**: Each keystroke entry is recorded with a precise timestamp.
- **Stealth Mode**: On Windows, the console window is hidden to allow discreet operation.
- **Secure Logging to File**: Stores encrypted keystrokes in a log file to prevent unauthorized reading.
- **Graceful Termination**: Automatically stops logging when the `Escape` key is pressed.

## Technical Details
### Encryption Algorithm
This project uses a simple **Caesar cipher** with a shift value (default: `5`). While this encryption is not strong for high-security applications, it provides basic obfuscation of the captured keystrokes. The encryption function ensures that only alphabetic characters are shifted, preserving other characters as they are.


### Stealth Execution
On Windows, the script hides the console window using the `ctypes` library to ensure that it does not visibly run in the foreground. On Linux/macOS, there is no native way to completely hide the process, but it runs without requiring a terminal window.

## Installation & Usage
### Prerequisites
Ensure you have Python installed (3.x recommended) along with the required dependencies:
```bash
pip install pynput
```

### Running the Keylogger
1. Clone the repository:
   ```bash
   git clone https://github.com/nickych/Chibz_KeyLogger.git
   cd chibz_keylogger
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
    
4. Execute the script:
   ```bash
   python chibz_keylogger.py
   ```

The script will begin capturing keystrokes and writing them to `keystrokes.log` in encrypted format.

## Security & Ethical Considerations
> **Warning:** Keylogging software has serious ethical and legal implications. This project is strictly for security research, auditing, and educational purposes. Unauthorized deployment of keyloggers without consent may violate privacy laws and result in legal consequences.

- **Ensure you have explicit permission** before using this software on any system.
- **Never use keyloggers for malicious activities** such as credential theft or unauthorized surveillance.
- **Consider enhancing encryption** if you need more robust security beyond a Caesar cipher.

## Potential Enhancements
To make this keylogger more robust and secure, consider the following improvements:
- **Stronger Encryption**: Replace the Caesar cipher with AES or RSA encryption for secure keystroke storage.
- **Network Transmission**: Implement remote logging over a secure channel.
- **Process Persistence**: Enable automatic execution on system startup.
- **Data Integrity Checks**: Ensure the log file has not been tampered with using cryptographic hashes.

## License
This project is licensed under the MIT License.

## Disclaimer
The developer assumes no responsibility for misuse. This software is provided as-is for ethical and legal security testing. Use responsibly within legal boundaries.

---

**Reminder:** Unauthorized keylogging is illegal in many jurisdictions. Always obtain explicit consent before deploying this software on any system.

