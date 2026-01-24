import random
choice = random.choice(range(28))
with open(f"ascii_{choice}", 'r') as f:
    content = f.read()
    print(content)