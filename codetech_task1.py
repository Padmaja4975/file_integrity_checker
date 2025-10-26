import hashlib
import os
import json

# Function to calculate hash of a file
def calculate_hash(file_path):
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            # Read file in chunks
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        print(f"[!] File not found: {file_path}")
        return None


# Function to create a baseline of hashes
def create_baseline(directory, baseline_file="baseline.json"):
    baseline_data = {}
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            baseline_data[file_path] = calculate_hash(file_path)
    
    with open(baseline_file, "w") as f:
        json.dump(baseline_data, f, indent=4)
    print(f"[+] Baseline created and saved to {baseline_file}")


# Function to check integrity of files
def check_integrity(directory, baseline_file="baseline.json"):
    if not os.path.exists(baseline_file):
        print("[!] No baseline found. Please create one first.")
        return
    
    with open(baseline_file, "r") as f:
        baseline_data = json.load(f)
    
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            current_hash = calculate_hash(file_path)
            old_hash = baseline_data.get(file_path)
            
            if old_hash is None:
                print(f"[NEW] File added: {file_path}")
            elif current_hash != old_hash:
                print(f"[CHANGED] File modified: {file_path}")
                # Add this at the end of check_integrity()
    changes_found = False
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            current_hash = calculate_hash(file_path)
            old_hash = baseline_data.get(file_path)
            
            if old_hash is None:
                print(f"[NEW] File added: {file_path}")
                changes_found = True
            elif current_hash != old_hash:
                print(f"[CHANGED] File modified: {file_path}")
                changes_found = True
    
    for file_path in baseline_data.keys():
        if not os.path.exists(file_path):
            print(f"[DELETED] File missing: {file_path}")
            changes_found = True
    
    if not changes_found:
        print("[OK] No changes detected. Files are intact.")
    
    # Check for deleted files
    for file_path in baseline_data.keys():
        if not os.path.exists(file_path):
            print(f"[DELETED] File missing: {file_path}")


# Main Program
if __name__ == "__main__":
    print("=== FILE INTEGRITY CHECKER ===")
    print("1. Create Baseline (First Time)")
    print("2. Check Integrity (Compare with Baseline)")
    choice = input("Enter choice (1/2): ")

    directory = input("Enter directory path to monitor: ").strip()

    if choice == "1":
        create_baseline(directory)
    elif choice == "2":
        check_integrity(directory)
    else:
        print("Invalid choice. Please enter 1 or 2.")