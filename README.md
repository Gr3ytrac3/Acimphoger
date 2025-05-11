# 🔐 Acimphoger

**A Command-Line Tool for Generating Secure Passwords with Identity-Based Customization**

---

## ✨ Features

- 🔠 Generates highly secure passwords using uppercase, lowercase, digits, and symbols
- 🧠 Classifies password strength as **Weak**, **Moderate**, **Strong**, or **Very Strong**
- 🧾 Accepts identity input like nicknames and fake names
- 📁 Saves passwords in a custom file at a user-defined path
- 🔄 Generates between 5–20 passwords, each 15–25 characters long
- 🔐 **Encrypts** the saved password file using AES (via Fernet) with a passphrase

---

## 🛠️ Requirements

- Python 3.7+
- [`cryptography`](https://pypi.org/project/cryptography/)

Install dependencies:

```bash
pip install cryptography
````

---

## 🚀 How to Use

1. Clone this repository:

```bash
git clone https://github.com/Gr3ytrac3/Acimphoger.git
cd Acimphoger
```

2. Run the tool:

```bash
python3 acimphoger.py
```

3. Follow the prompts:

   * Enter identity data (nickname + fake label)
   * Set how many passwords to generate and their length
   * Choose a save path
   * Optionally encrypt the file with a passphrase

---

## 📂 Sample Output

```bash
Nickname: KernelRed
Fake Identity: k3rn3l
Number of Passwords: 7
Password Length: 25

[+] Passwords saved to /home/user/KernelRed_k3rn3l_passwords.txt
[+] Encrypted file saved to /home/user/KernelRed_k3rn3l_passwords.txt.enc
```

> Encrypted files are base64-encoded and can only be decrypted with the original passphrase.

---

## 🔐 Encryption Info

* Uses **Fernet** from the `cryptography` library (AES-128 in CBC mode with HMAC)
* Keys are derived from your passphrase via SHA-256 hashing
* The `.enc` file is unreadable without the original passphrase

---

## 👨‍💻 Author

**Cyberdev (Gr3ytrac3)**
*Offensive Security Artisan | Builder of Digital Fortresses*
