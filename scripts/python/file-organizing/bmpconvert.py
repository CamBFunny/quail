from PIL import Image

def bitmap_to_c_array(image_path):
    img = Image.open(image_path)
    img = img.convert('RGB')
    data = list(img.getdata())
    c_array = ', '.join(f'0x{r:02x}{g:02x}{b:02x}' for r, g, b in data)
    return f'unsigned char image[] = {{{c_array}}};'

# Usage
print(bitmap_to_c_array('../pip_splash.bmp'))
