import os

for p in range(0, 2):
    os.rename(f"quail{p}", f"quail_{p}")
