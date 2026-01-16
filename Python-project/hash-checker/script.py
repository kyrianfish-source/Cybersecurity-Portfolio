# File Hash Checker
# This script calculates the SHA-256 hash of a file and compares it to a known good hash.

import hashlib

def get_file_hash(filename):
    sha256 = hashlib.sha256()

    with open(filename, "rb") as file:
        for block in iter(lambda: file.read(4096), b""):
            sha256.update(block)

    return sha256.hexdigest()

known_hash = "5d41402abc4b2a76b9719d911017c592"  # Example hash
file_hash = get_file_hash("example.txt")

print("Calculated Hash:", file_hash)

if file_hash == known_hash:
    print("File integrity verified.")
else:
    print("Warning: File hash does NOT match!")
