import itertools


def palindrome_matcher(filename):
    with open(filename, "r", encoding="utf-8") as myfile:

        # Support both csv and txt, clean from spaces & new lines.
        words = []
        for element in myfile:
            if "," in element:
                items = element.split(",")
                for item in items:
                    item = item.replace("\n", "")
                    item = item.replace(" ", "")
                    if item != "":
                        words.append(item)
            else:
                element = element.replace("\n", "")
                words.append(element)

        # Create pairs.
        pairs = list(itertools.combinations(words, r=2))

        palindromes = {}

        for element in pairs:
            element_a = element[0]
            element_b = element[1]
            palindrome_status = True
            from_left = 0
            from_right = -1
            if len(element_a) == len(element_b):
                for i in range(len(element_a)):
                    if element_a[from_left] == element_b[from_right]:
                        continue
                    else:
                        palindrome_status = False
                    from_left += 1
                    from_right -= 1
                if palindrome_status:
                    palindromes[element_a] = element_b

        palindromes_to_print = ""

        for key, value in palindromes.items():
            palindromes_to_print += "\n" + key + " " + value
        return palindromes_to_print.replace("\n", "", 1)


