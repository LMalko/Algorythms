'''
    Requires installing speech synthesizer 'espeak' by commands:
        apt-get install python-espeak
        sudo apt install espeak

    subprocess.run(*args, shell=False)
        - run the command described by args
        - If passing a single string, either shell must be True or else the string
          must simply name the program to be executed without specifying any arguments

    lang="en" - language setting (english by default)
'''
import subprocess
import string
import time


def speak_ICAO(text, letter_pause=0.2, word_pause=0.5, lang="en"):

    d = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 'f':'foxtrot',
    'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett', 'k':'kilo', 'l':'lima',
    'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa', 'q':'quebec', 'r':'romeo',
    's':'sierra', 't':'tango', 'u':'uniform', 'v':'victor', 'w':'whiskey', 
    'x':'x-ray', 'y':'yankee', 'z':'zulu'}

    for char in text:
        if char in string.whitespace:
            time.sleep(word_pause)
        elif char in string.ascii_letters:
            subprocess.run("espeak -v {0} {1}".format(lang, d[char.lower()]), shell=True)
            time.sleep(letter_pause)

speak_ICAO('Yes, sir!')
