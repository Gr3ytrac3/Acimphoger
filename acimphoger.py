import os
import random
import string
import sys
from pathlib import Path


def print_banner():
    banner = r"""
     ___      _           __                            
    /   | ____(_)___ ___ / /___  ____ _____ ____  _____
   / /| |/ __/ / __ `__ \/ / __ \/ __ `/ __ `/ _ \/ ___/
  / ___ / /_/ / / / / / / / /_/ / /_/ / /_/ /  __/ /    
 /_/  |_\__/_/_/ /_/ /_/_/ .___/\__,_/\__, /\___/_/     
                       /_/          /____/             
    """
    print(banner)
    print("Author      : Cyberdev")
    print("Version     : 1.0.0")
    print("GitHub      : Gr3ytrac3")
    print("Tool        : Generate Fake IDs & Strong Passwords\n")


def get_user_inputs():
    print("-- Enter Fake Identity Info --")
    nickname = input("Enter a nickname: ").strip()
    fake_id = input("Enter a fake identity label: ").strip()

    while True:
        try:
            count = int(input("Enter number of passwords to generate (5-20): "))
            if 5 <= count <= 20:
                break
            else:
                print("Please enter a number between 5 and 20.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    while True:
        try:
            length = int(input("Enter password length (15-25): "))
            if 15 <= length <= 25:
                break
            else:
                print("Please enter a number between 15 and 25.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    save_path = input("Enter directory path to save the passwords: ").strip()
    return nickname, fake_id, count, length, save_path


def generate_password(length):
    if length < 4:
        raise ValueError("Password length too short for all character types")

    all_chars = string.ascii_letters + string.digits + "@#$%^&*()_+-={}[]|;'<>,./~"
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice("@#$%^&*()_+-={}[]|;'<>,./~")
    ]

    password += [random.choice(all_chars) for _ in range(length - 4)]
    random.shuffle(password)
    return ''.join(password)


def password_strength(password):
    score = 0
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in "@#$%^&*()_+-={}[]|;'<>,./~" for c in password):
        score += 1

    return "Weak" if score < 3 else ("Strong" if score == 4 else "Moderate")


def save_passwords(nickname, fake_id, passwords, path):
    Path(path).mkdir(parents=True, exist_ok=True)
    file_path = Path(path) / f"{nickname}_{fake_id}_passwords.txt"

    with open(file_path, "w") as f:
        for i, pwd in enumerate(passwords, 1):
            f.write(f"{i}. {pwd} \t[{password_strength(pwd)}]\n")

    print(f"\n[+] Passwords saved to {file_path}\n")


def main():
    print_banner()
    nickname, fake_id, count, length, save_path = get_user_inputs()

    passwords = [generate_password(length) for _ in range(count)]
    save_passwords(nickname, fake_id, passwords, save_path)


if __name__ == "__main__":
    main()
