import os
import sys

def read_file():
    path = "gods_eye_output.txt"
    if not os.path.exists(path):
        print("File not found.")
        return
    
    # Try different encodings
    for enc in ["utf-16", "utf-8", "big5", "cp950"]:
        try:
            with open(path, "r", encoding=enc) as f:
                content = f.read()
                print(f"--- Decoded with {enc} ---")
                print(content)
                return
        except:
            continue
    print("Failed to decode.")

if __name__ == "__main__":
    read_file()
