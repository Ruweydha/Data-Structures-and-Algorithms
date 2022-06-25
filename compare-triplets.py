def compareTriplets(a, b):
    # Write your code here
    scores = [0,0]
    for i in range(len(a)):
        if a[i] > b[i]:
            scores[0] += 1
        elif b[i]> a[i]:
           scores[1] += 1   
            
    return scores    