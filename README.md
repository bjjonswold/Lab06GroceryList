# Lab06GroceryList
List + For-Loop warmup

# Attached is some code
Review the code provided. Answer the following questions by adding comments to your code! You are free to talk with other students, and seek better understanding to these questions. See below for reminders on types, variables, and input

# Step 1
1. What is the output and its type for itemFetching(num)? For itemFetching(6)?
2. Find the comment in itemFetching(). What happens to our output if we tab that line so it lines up with the line above it? What would itemFetching(6) be?
3. What is the output and its type for itemSorting(lst)? What is the output for itemSorting(\[3, 7, "peas", 2.25, "carrots", 1, 5.3])?
4. Make a list with 17, 0.2, and "Phantom of the Opera" and assign it to a variable called myFavoriteThings.

# Step Two: Coding: timeOut(timer)
Find the function timeOut(timer). 

Your child got upset because you did not read her grocery list correctly, and now she is in time out. Make a list of numbers counting down from timer to 1 until she gets out of timeout.

For example, timeOut(4) should return \[4, 3, 2, 1].

timeOut(2) should return \[2, 1]

# Step 3: Test timeOut(timer)
How do you test code? You simply add the lines to your python file (in the future, you will have test lines in separate files).

As such, we would recommend adding the following just above def main().

print("TESTING", timeOut(4)) 

print("TESTING", timeOut(2)) 

Also add your own tests!

# Submitting the Assignment
Make sure to submit the assignment for grading! If you haven't clicked through the canvas link in a while, we would suggest clicking through it again before submitting.

# Reminder on Lists
Lists can have mixed types **in Python**, meaning that you can have strings and ints in the same list. Lists can be indexed in the same way that strings are indexed, 
and they are basically just containers. If you are ever dealing with a bunch of data of unspecified size, lists are a good option for saying "some amount of data".

# Reminder on For-Loops
For loops can be writen with in statements and range statements.
# in statements
    In statements typically look something like this:
        for i in list:
          do something
          
# Range
    Ranges actually have 3 arguments, but 2 of them are optional. With:
        range(4), this is really range(0, 4, 1), where it goes range(start, end, countBy)
        if we did range(0, 4, 2), we would see 0 and 2, but it would skip 1 and 3.
        So, if we wanted to go backwards, we would just have to swap 0 and 4 and countBy a negative
 Ranges are also end-excluding, so in range(4), we will never reach 4.
