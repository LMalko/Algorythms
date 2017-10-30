'''
99 bottles of beer on the wall, 99 bottles of beer.

Take one down, pass it around, 98 bottles of beer on the wall.

The same verse is repeated, each time with one fewer bottle.The song is completed when the singer or singers reach zero.

Your task here is write a Python program capable of generating all the verses of the song.'''


def bottles_99(bottles=99):

    bottles_left = bottles

    while bottles_left != 1:

        print(str(bottles_left) + " bottles of beer on the wall, " + str(bottles_left) + " bottles of beer.")

        bottles_left -= 1

        print("Take one down, pass it around, " + str(bottles_left) + " bottles of beer on the wall.")

    return "1 bottle of beer on the wall, 1 bottle of beer.\
            \nTake one down, pass it around, 0 bottles of beer on the wall."


print(bottles_99())
