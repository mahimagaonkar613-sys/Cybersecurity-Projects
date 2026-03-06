import os
import hashlib
import json

DIRECTORY_TO_MONITOR = "test_folder"
HASH_FILE = "hashes.json"


def calculate_hash(filepath):
    sha256 = hashlib.sha256()

    with open(filepath, "rb") as f:
        while True:
            data = f.read(65536)
            if not data:
                break
            sha256.update(data)

    return sha256.hexdigest()


def scan_files():
    file_hashes = {}

    for root, dirs, files in os.walk(DIRECTORY_TO_MONITOR):
        for file in files:
            path = os.path.join(root, file)
            file_hashes[path] = calculate_hash(path)

    return file_hashes


def save_hashes(hashes):
    with open(HASH_FILE, "w") as f:
        json.dump(hashes, f, indent=4)


def load_hashes():
    if not os.path.exists(HASH_FILE):
        return None

    with open(HASH_FILE, "r") as f:
        return json.load(f)


def compare_hashes(old, new):

    for file in new:
        if file not in old:
            print("NEW FILE:", file)

        elif old[file] != new[file]:
            print("MODIFIED FILE:", file)

    for file in old:
        if file not in new:
            print("DELETED FILE:", file)


def main():

    new_hashes = scan_files()
    old_hashes = load_hashes()

    if old_hashes is None:
        print("Saving initial hashes...")
        save_hashes(new_hashes)

    else:
        compare_hashes(old_hashes, new_hashes)
        save_hashes(new_hashes)


main()