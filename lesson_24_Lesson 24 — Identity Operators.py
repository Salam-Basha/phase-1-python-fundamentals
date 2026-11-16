#===============================================
#Lesson 24 — Identity Operators in Python
#===============================================


#Exercise 1 — Predict the output

a = 10
b = a 

print(a is b)
print(a is not b)


#Exercise 2 — Predict the output

x = [1,2,3]
y = [1,2,3]

print(x == y)
print(x is y)


#Exercise 3 — Write a program

a = "python"
b = a

print(a is b)
print(a is not b)


#Challenge  
#Create a variable called password and set it to None.
#Use an if statement and is to check whether the password is None. Print "Password not set" if it is.

password = None
if password is None:
    print("password not set")
