# Encoding a string to bytes using UTF-8
import shutil
import os
import string
import random
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

# Prompt user to select folder with camcypher and key
def select_folder():
    """Opens a file dialog for the user to select a directory."""
    root = tk.Tk()
    root.withdraw()  # Hide the main Tkinter window
    folder_path = filedialog.askdirectory(title="Select a Folder")
    return folder_path

# Example usage:
selected_directory = select_folder()

files_in_folder = os.listdir(selected_directory)
actual_files = [f for f in files_in_folder if os.path.isfile(os.path.join(selected_directory, f))]

# Ask user to select the file they want encrypted
source_file = os.path.join(selected_directory, actual_files[0])

# Load in .txt file as string
try:
    with open(source_file, 'r') as file:
        text_content = file.read()
except FileNotFoundError:
    print(f"Error: The file '{source_file}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

key_source = os.path.join(selected_directory, actual_files[1])

# Load key
try:
    with open(key_source, 'r') as file:
        decypher_key = file.read()
except FileNotFoundError:
    print(f"Error: The file '{key_source}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

symbols = string.ascii_letters + string.punctuation + '!@#$%^&*()_+{}[]|:;"<>,.?/~`'
symbols = list(symbols)
j = 0
bake = [' '] * 2
counter = 0
i = 0

char_list = list(decypher_key)

for i in range(len(char_list)):
    bake[j] = char_list[i]
    if bake[j] == ' ':
        bake = ''.join(bake)
        truncated = bake[:(j+1)]
        index = symbols[counter]
        text_content = text_content.replace(truncated, index)
        bake = [''] * 2
        counter += 1
        j = -1
    bake += ' '
    i += 1
    j += 1

print(f"// DECYPHERED CONTENT //")

decoded_text = ''.join(text_content)

# Print instead of save
print(decoded_text)