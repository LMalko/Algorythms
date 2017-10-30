''' Define a function overlapping() that takes two lists and returns True if they have at least one member in common, 
False otherwise. You may use your is_member() function, or the in operator, but for the sake of the exercise, 
you should (also) write it using two nested for-loops.'''


def overlapping(list_one, list_two):
    for element in list_one:
        for item in list_two:
            if element == item:
                return True
    return False
