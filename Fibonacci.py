# Designed for Python 3.6 by Leo Wilczek

# Prints the value of the Fibonacci sequence at the user-specified position
def fibonacci(pos):
    if pos > 0:  # validate that pos is in range
        index = 1   # initial index
        first = 0   # first value of Fibonacci
        second = 1  # second value of Fibonacci
        while index < pos:
            value = first + second  # find next value in sequence
            first = second          # the first value in the sequence is replaced by the second value
            second = value          # the second value in the sequence is replaced by the value of the addition of the previous first and second value
            index += 1              # increment the sequence position of the first value
        txt = "The value at position {} is {}.\n"  # create format string
        print(txt.format(pos, first))   # print the value of the user-specified postion to the user
    else:
        print("The position provided is out of range. Please specify an integer greater than 0.\n")   # tell the user that the specified position is out of range

running = 1
while(running == 1):
    position = input("Please enter a position in the Fibonacci sequence. This should be an integer greater than 0.\n" +
    "If you wish to exit the program, enter -1.\n")    # get user-specified position or exit value
    if int(position) == -1:
        input("Press any key to exit.\n")
        running = 0
    else:
        fibonacci(int(position)) # run fibonacci function on specified position
