#Exercise 1 — Even or Odd

a = int(input(" "))
if a % 2 == 0 :
    print("even")
else:
    print("odd")


#Exercise 2 — Largest of Three Numbers

a = 10
b = 25
c = 15

if a > b:
    if a > c :
        print("a is largest number")
    else:
        print("c is largest number")
else:
    if b > c:
        print("b is biggest number")
    else:
        print("c is biggest number")


#Exercise 3 — Sum of Numbers

total = 0

for i in range(1,11):
    total = total + i

print(total)

#Challenge 🎯 — Reverse a Number

Input: 1234
Output: 4321

n = 1234
rev = 0

while n > 0 :
    ld = n % 10
    rev = rev * 10 + ld
    n = n//10

print(rev)


