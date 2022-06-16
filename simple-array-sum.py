def simpleArraySum(ar):
    # Write your code here
    sum = 0
    #Checking that the array is not empty
    if len(ar) > 0:
        for number in ar:
            #We are assuming that not all items are numbers
            sum += int(number)
    
    return sum  