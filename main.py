
# ╱╱╱╭━━━╮╱╱╱╱╭╮
# ╱╱╱┃╭━╮┃╱╱╱╱┃┃
# ╭━╮┃┃╱╰╋━━┳━╯┣━━╮
# ┃╭╮┫┃╱╭┫╭╮┃╭╮┃┃━┫
# ┃┃┃┃╰━╯┃╰╯┃╰╯┃┃━┫
# ╰╯╰┻━━━┻━━┻━━┻━━╯

from PIL import Image
import sys
from binary_dict import binary_dict
import json

def hex_to_rgb(hexa):
    return tuple(int(hexa[i:i+2], 16)  for i in (0, 2, 4))

def rgb_to_hex(r, g, b):
    return '{:02x}{:02x}{:02x}'.format(r, g, b)

with open("config.json") as c:
    config = json.load(c)

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

def code_to_text(image):
    str1 = ""
    str2 = ""
    img = Image.open(image)
    width, height = img.size
    try:
        for y in range(height):
            for x in range(width):
                px = img.getpixel((x,y))
                r,g,b = px
                str1 += config[rgb_to_hex(r,g,b)]
            str2 += str1
            str1 = ""
        print(text_from_bits(str2))
    except UnicodeDecodeError:
        print(f"Error in {y+1} stripe")

def text_to_code(text):
    img = Image.new('RGB', (8, len(text)))
    
    for y, e in enumerate(text):
        binary_code = binary_dict.get(e)
        if binary_code is None:
            continue
        
        for x in range(8):
            color = config[binary_code[x]]
            img.putpixel((x, y), hex_to_rgb(color))

    img.save("output.png")

if __name__ == "__main__":
    if sys.argv[1] == "create":
        text = sys.argv[2]
        text_to_code(text)
    elif sys.argv[1] == "read":
        file = sys.argv[2]
        code_to_text(file)