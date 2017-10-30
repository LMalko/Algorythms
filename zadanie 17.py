import re


# Write a version of a palindrome recognizer that also accepts phrase palindromes such as 
# "Go hang a salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", 
# "Sit on a potato pan, Otis", "Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas", 
# "I roamed under it as a tired nude Maori", "Rise to vote sir", or the exclamation 
# "Dammit, I'm mad!". Note that punctuation, capitalization, and spacing are usually ignored.


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

# Lukasz
