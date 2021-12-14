# FizzBuzz Python 3 algorithm developed by Leo Wilczek

i = 100 # value of last number to assess
p = 1   # value to start the sequence
# while loop runs for each value between p and i
while p <= i:
    # if remainder of p divided by three is 0, check if also divisible by 5 with no remainder
    if(p % 3 == 0):
        if(p % 5 == 0):
            print("FizzBuzz")   # if p is also divisible by 5 with no remainder, print "FizzBuzz"
        else:
            print("Fizz")   # if p is only divisible by 3, print "Fizz"
    elif(p % 5 == 0):
        print("Buzz")   # if p is only divisible by 5, print "Buzz"
    else:
        txt = "{}"  # if not divisible by 3 or 5 without remainder, print the value of p
        print(txt.format(p)) # as p is an integer, format it as string
    p += 1  # increment p each iteration
input("Press any key to exit . . .")    # wait for user input to close console
