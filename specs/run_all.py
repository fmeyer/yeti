import os
import sys
import doctest


OPTION_FLAGS = doctest.ELLIPSIS
HERE = os.path.join(os.path.dirname(__file__) or '.') 


if __name__ == '__main__':
    sys.path.append(HERE)

    for filename in os.listdir(HERE):
        if filename.endswith('.py') and filename not in ['run_all.py']:
            doctest.testmod(__import__(filename[:-3]),
                            optionflags=OPTION_FLAGS)
