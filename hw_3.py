# Name: Adrian Diaz
# hw3.py
import math
import random
##### Template for Homework 3, exercises 1 - 4 ######

# ********** Exercise 1 ********** 
print("Exercise 1")
# Define is_divisible function here
def is_divisible(m,n):
##### YOUR CODE HERE #####
    if n == 0:
        print("Division by 0 is undefined!")
    elif m%n == 0: 
        a = True
        return a
    else: 
        a = False
        return a
# Test cases for is_divisible
#print is_divisible(10, 5)  # This should return True
#print is_divisible(18, 7)  # This should return False
#print is_divisible(42, 0)  # What should this return?
print(is_divisible(10,5)) #Returns True
print(is_divisible(18,7)) #Returns False
print(is_divisible(42,0)) #This returns a message warning division by 0 is undefined
# ********** Exercise 2 ********** 
print("Exercise 2")
# Define not_equal function here
def not_equal(a,b):
##### YOUR CODE HERE #####
    if a==b:
        return False
    else:
        return True
# Test cases for not_equal
##### YOUR CODE HERE #####
print(not_equal("r","r")) #Returns False
print(not_equal(0,0)) #Returns False, too
print(not_equal("a","b")) #Returns True
print(not_equal(4,5)) #Returns True, too
#This means, then, that the function works for both numeric and string values
print(not_equal(1+2+3+0,6)) #Returns False
print(not_equal(1+2+3+4,9)) #Returns True
#This means the function also works for expressions containing mathematical operations of numbers
# ********** Exercise 3 ********** 
print("Exercise 3")
## 1 - multadd function
def multadd(a,b,c):
##### YOUR CODE HERE #####
    return a*b+c
## 2 - Equations
##### YOUR CODE HERE #####
print(10==multadd(2,3,4)) #True
print(11==multadd(2,3,4)) #False
#Function seems to be working
# Test Cases
# angle_test =
angle_test=multadd(math.cos(math.pi/4),0.5,math.sin(math.pi/4))
# print "sin(pi/4) + cos(pi/4)/2 is:"
# print angle_test
print("sin(pi/4)+cos(pi/4)/2 is:", angle_test)
# ceiling_test =
ceiling_test=multadd(2,math.log(12,7),math.ceil(276/19))
# print "ceiling(276/19) + 2 log_7(12) is:"
# print ceiling_test
print("ceiling(276/19)+2log_7(12) is:", ceiling_test)
# ********** Exercise 4 **********

## 1 - rand_divis_3 function
def rand_divis_3():
##### YOUR CODE HERE #####
    a=int(random.randint(0,100))
    print("Number:", a)
    if a%3 == 0:
        b = True
        return b
    else:
        return False
        return b
# Test Cases (5)
print("Test 1")
print(rand_divis_3())
print("Test 2")
print(rand_divis_3())
print("Test 3")
print(rand_divis_3())
print("Test 4")
print(rand_divis_3())
print("Test 5")
print(rand_divis_3())