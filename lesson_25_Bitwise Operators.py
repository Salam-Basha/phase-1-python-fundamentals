#===========================================
#Lesson 25 — Bitwise Operators 
#===========================================


#a & b     # AND
#a | b     # OR
#a ^ b     # XOR
#~a        # NOT
#a << 1    # Left shift
#a >> 1    # Right shift


#Exercise 1 — AND and OR

a = 6
b = 4

print(a & b)
print(a | b)

#Exercise 2 — XOR

x = 7
y = 5

print(x ^ y)

#Exercise 3 — NOT

a = 10

print(~a)


#Exercise 4 — Shift operators

a = 4

print(a << 2)
print(a >> 1)


#Challenge 🎯 — Bitwise calculator

a = 12
b = 10

print(a & b)
print(a | b)
print(a ^ b)
print(~a)
print(a << 1)
print(a >> 1)


#Common mistakes:
# & is bitwise AND; and is logical AND.
# | is bitwise OR; or is logical OR.
# ^ means XOR, not power. For powers, use **.
# ~5 gives -6, not -5.


