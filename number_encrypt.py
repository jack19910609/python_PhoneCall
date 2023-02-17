import colorama
import binascii
from colorama import Fore,Style,Back

def main():
    colormaInit()
    welcome()

    YELLOW = "\x1b[1;33;40m" 
    RED = "\x1b[1;31;40m"

    print(f"\n{RED}Enter the Phone Number : ", end='')
    To_input = input()

    stringTobinery = text_to_bits(To_input)
    flipbinery = addbinary(stringTobinery)
    flipstring= text_from_bits(flipbinery)

    print("Encrypy Message : " , flipstring)

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

def addbinary(binary):
    f = open('secert.txt' , 'r')
    addedbinary = bin(int(binary, 2) + int(f.read(), 2))[2:]
    f.close()
    return addedbinary

   
def colormaInit():   
    colorama.init()

#welcome 
def welcome():
	wel =Fore.GREEN + """
        +==========================================+
        |............   Encrypt Tool   ............|
        +------------------------------------------+
        |             #Author: Jimmy               | 
        |	       Version 1.0                 |
        |                                          |
        |              Encrypt String              |
        |                                          |
        +==========================================+
        |............   Encrypt Tool   ............|
        +------------------------------------------+\n\n
"""

	print(wel)

if __name__ == '__main__':
	main()
