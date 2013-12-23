from colorama import init
init()
from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')
print(Back.GREEN + '                  ')
print(Style.DIM + 'and in dim text')
print(Fore.RESET + Back.RESET + Style.RESET_ALL)
print('back to normal now')
