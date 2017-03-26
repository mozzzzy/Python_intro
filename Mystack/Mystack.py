#coding:utf-8

#
# Mystack.py
#



# null stack
stack = [];

#stack ________ ==> x_______
def push(x):
	stack.append(x)

#stack x_______ ==> ________
def pop():
	stack.pop()

#stack x_______ --> x
def top():
	return stack[len(stack)-1]


