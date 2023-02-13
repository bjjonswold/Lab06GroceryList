'''
1. The output would be a list of numbers within the range of num. 
    For itemFetching(6), the output would be [1, 2, 3, 4, 5, 6, "got them all!"]
2. There would be a "Got them all!" after each number in the list
3. The output would be a list of strings. The output would be 
4. myFavoriteThings = [17, 0.2, "Phantom of the Opera"]
'''
#input: num--number of items to get
#output: you figure this out!
def itemFetching(num):
    lst = []
    for i in range(num):
        lst.append(i)
    lst.append("got them all!") #what would happen if we tabbed this line inside of the for-loop?
    return lst
    
#input: grocery list of mixed types
#output: you figure this out!
def itemSorting(lst):
    sorted = []
    for item in lst:
        if item == 1 or item == 3 or item == 5 or item == 9:
            print("I'm not sure why she uses odd numbers for bread...")
            sorted.append("bread")
        elif item == "peas" or item == "carrots" or item == "broccoli":
            print("Oh good, vegetables")
            sorted.append(item)
        elif item == 2.25 or item == 5.3:
            print("Not sure why there are prices in here.")
            sorted.append("snacks(??)")
        else:
            print("I can't even read her handwriting for this one...")
    return sorted
 
#input: timer--number of seconds in time out
#output: countDown-- a list with the timer counting down until 0
def timeOut(timer):
    countDown = []
    for i in range(timer, 0, -1):
        countDown.append(i)
    return countDown

print("TESTING", timeOut(4)) 
print("TESTING", timeOut(2)) 