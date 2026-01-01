# Encoding a string to bytes using UTF-8
import shutil
import os
import string
import random
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

# Ask user to select the file they want encrypted
source_file = filedialog.askopenfilename()

# Create backup folder
directory_name = f'camcypher-content'
try:
    os.mkdir(directory_name)
    print(f"Directory '{directory_name}' created successfully.")
except FileExistsError:
    print(f"Directory '{directory_name}' already exists... Replaced")
    shutil.rmtree(directory_name)
    os.mkdir(directory_name)
except Exception as e:
    print(f"An error occurred: {e}")


# Load in .txt file as string
try:
    with open(source_file, 'r') as file:
        text_content = file.read()
except FileNotFoundError:
    print(f"Error: The file '{source_file}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

symbols = string.ascii_letters + string.punctuation + '!@#$%^&*()_+{}[]|:;"<>,.?/~`'
camcypher = [0] * len(symbols)

for n in range(len(symbols)):
    bake = [0] * random.choice(range(3, 12))
    for j in range(len(bake)):
        bake[j] = random.choice(symbols)
    bake[len(bake)-1] = ' '
    camcypher[n] = ''.join(bake)

encoded_bytes = [''] * (len(text_content) + 1)
trigger = False

for i in range(len(text_content)):
    for k in range(len(symbols)):
        if text_content[i] == symbols[k]:
            byte = camcypher[k]
            trigger = True
    if trigger:
        encoded_bytes[i] = str(byte)
        trigger = False
    else:
        encoded_bytes[i] = text_content[i]

# print(symbols)
# print(f"Camcypher: {camcypher}")
# print(f"Encoded bytes: {encoded_bytes}")

# 2. Save encrypted file and key in the same folder as original file
no_ext = f"{os.path.splitext(source_file)[0]}"
file_name = f"{no_ext}_camcypher.txt"
file1 = file_name

save = ''.join(encoded_bytes)
# 3. Open the file in write mode and 4. Write the string
with open(file_name, 'w', encoding='utf-8') as file:
    file.write(save)

save = ''.join(camcypher)
file_name = f"{no_ext}_key.txt"
# 3. Open the file in write mode and 4. Write the string
with open(file_name, 'w', encoding='utf-8') as file:
    file.write(save)

z_files = [file1, file_name]

destination_path = directory_name

for k in z_files:
    try:
        shutil.move(k, destination_path)
        print(f"File '{k}' copied to '{destination_path}' successfully.")
    except FileNotFoundError:
        print(f"Error: Source file '{k}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
