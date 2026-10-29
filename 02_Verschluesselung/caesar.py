"""Cäsar-Chiffre: verschlüsseln, entschlüsseln und per Brute Force knacken.

Aufruf:
    python caesar.py enc 3 "Datenschutz ist wichtig"
    python caesar.py dec 3 "Gdwhqvfkxwc lvw zlfkwlj"
    python caesar.py brute "Gdwhqvfkxwc lvw zlfkwlj"
"""
import sys


def shift_char(ch: str, key: int) -> str:
    if ch.isupper():
        return chr((ord(ch) - ord("A") + key) % 26 + ord("A"))
    if ch.islower():
        return chr((ord(ch) - ord("a") + key) % 26 + ord("a"))
    return ch  # Leerzeichen, Ziffern, Umlaute bleiben unverändert


def encrypt(text: str, key: int) -> str:
    return "".join(shift_char(c, key) for c in text)


def decrypt(text: str, key: int) -> str:
    return encrypt(text, -key)


def brute_force(text: str) -> None:
    for key in range(1, 26):
        print(f"{key:2d}: {decrypt(text, key)}")


if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "enc":
        print(encrypt(sys.argv[3], int(sys.argv[2])))
    elif mode == "dec":
        print(decrypt(sys.argv[3], int(sys.argv[2])))
    elif mode == "brute":
        brute_force(sys.argv[2])
