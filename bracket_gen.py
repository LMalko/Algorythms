from random import shuffle, randint

def gen_bracket_string(N):
    opening_bracket = "["
    closing_bracket = "]"
    brackets = list(opening_bracket * N + closing_bracket * N)
    shuffle(brackets)
    return "".join(brackets)


def validate_bracket_tree(bracket_string):
    opening_bracket = "["
    closing_bracket = "]"
    # routine for checking whether or not a parenthesized expression is valid:
    # if current parenthesis is opening, push it to stack
    # if current parenthesis is closing and the stack is not empty, pop opening parenthesis from stack
    # else, if the stack is empty and a closing parenthesis is encountered, report error
    # the validation succeeds if tree traversal is not interrupted by an unmatched parenthesis
    stack = []
    if not bracket_string:
        return False

    for char in bracket_string:
        if char == opening_bracket:
            stack.append(opening_bracket)
        elif char == closing_bracket:
            if not stack:
                return False
            else:
                stack.pop()

    return True


def main():
    while True:
        brackets = ""
        print("\nAttempts: ")
        while not validate_bracket_tree(brackets):
            brackets = gen_bracket_string(randint(4, 10))
            print(" " + brackets)

        print("\nValid attempt:")
        print("\n " + brackets)
        input()


if __name__ == "__main__": main()
