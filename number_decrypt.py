import colorama
from colorama import Fore,Style,Back
import binascii

def main():
    colormaInit()
    welcome()

    YELLOW = "\x1b[1;33;40m" 
    RED = "\x1b[1;31;40m"

    print(f"\n{RED}Enter the Code : ", end='')
    To_input = input()
    
    bineryString =  text_to_bits(To_input)
    flipbineryString = addbinary(bineryString)
    flipstring= text_from_bits(flipbineryString)

    print("flip string : " , flipstring)
    
def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

def addbinary(binary):
    f = open('secert.txt' , 'r')
    addedbinary = bin(int(binary, 2) - int(f.read(), 2))[2:]
    f.close()
    return addedbinary

def colormaInit():   
    colorama.init()

#welcome 
def welcome():
	wel =Fore.GREEN + """
        +==========================================+
        |............   decrypt Tool   ............|
        +------------------------------------------+
        |             #Author: Anonymous               | 
        |	       Version 1.0                 |
        |                                          |
        |              decrypt String              |
        |                                          |
        +==========================================+
        |............   decrypt Tool   ............|
        +------------------------------------------+\n\n
"""

	print(wel)

if __name__ == '__main__':
	main()
