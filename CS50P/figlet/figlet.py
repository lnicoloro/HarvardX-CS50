import random
import sys
from pyfiglet import Figlet
figlet = Figlet()

if len(sys.argv) == 1:
    ## select random font for text
    font = random.choice(figlet.getFonts())
    text = input('Input: ')
    figlet.setFont(font=font)
    print('Output:')
    print(figlet.renderText(text))




elif len(sys.argv) == 3:
    if sys.argv[1] == '-f' or sys.argv[1] == '--font':
        if sys.argv[2] in figlet.getFonts():
            figlet.setFont(font=sys.argv[2])
            text = input('Input: ')
            print('Output:')
            print(figlet.renderText(text))
        else:
            sys.exit('Invalid Usage')
    else:
        sys.exit('Invalid Usage')


else:
    sys.exit('Invalid Usage')


