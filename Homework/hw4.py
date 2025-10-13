from pyfiglet import figlet_format
from colorama import Fore, Back

figlet_form = figlet_format('The spectacular quickly becomes normal.', 'fuzzy')
text_colored = Fore.BLACK + Back.BLUE + figlet_form

print(text_colored)
