# Colorama Documentation by RIOTOFF


### First, we need to import the module...

## from colorama import Fore, Back, Style

### Next, you can just write...

## print(Fore.( YOUR COLOR WITHOUT '()'!!! ) )
# Example:
# print(Fore.RED)
# print('Red color is cool!')
# print(Fore.GREEN)
# print('But green is better!')

### All colors:
# Fore: LIGHTBLACK_EX, LIGHTRED_EX, LIGHTGREEN_EX, LIGHTYELLOW_EX, LIGHTBLUE_EX, LIGHTMAGENTA_EX, LIGHTCYAN_EX, LIGHTWHITE_EX
# Back: LIGHTBLACK_EX, LIGHTRED_EX, LIGHTGREEN_EX, LIGHTYELLOW_EX, LIGHTBLUE_EX, LIGHTMAGENTA_EX, LIGHTCYAN_EX, LIGHTWHITE_EX
# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL



#### MY CODE:

from time import sleep as sl
from colorama import Fore, Back, Style

sl(2)
print(Style.BRIGHT)
print(Fore.LIGHTGREEN_EX)
print('Hello everybody!')
sl(2)
print(Style.BRIGHT)
print(Back.BLUE)
print('you cant read this text lol')