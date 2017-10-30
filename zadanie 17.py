import re


def palindrome_recognizer(string):
    regex = re.compile(r"[^A-Za-z]")
    string = regex.sub('', string).lower()
    from_left = 0
    from_right = -1
    for i in range(int(len(string) / 2)):
        if string[from_left] == string[from_right]:
            from_left += 1
            from_right -= 1
        else:
            return False
    return True


print(palindrome_recognizer(	"Go hang a salami I'm a lasagna hog."))
# Lukasz
