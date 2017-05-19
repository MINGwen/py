#! /usr/bin/python

# while True:
# 	try:
# 	    x=int(input("please enter a number:"))
# 	except ValueError:
# 		print("Oops!  That was no valid number.  Try again...")

words = ["i", "want", "travel"]
for w in words:
	print(w, len(w))
for i in range(0,10,2):
	print(i)
for j in range(len(words)):
	print(j,words[j])

#斐波那契数列
def fib(n):
	a,b = 0,1
	while a<n:
		print(a,end=" ")
		a,b=b,a+b
   
number = fib(99)
print(number)	
