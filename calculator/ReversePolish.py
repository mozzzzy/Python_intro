#coding:UTF-8
#
#

from ClassStack import ClassStack

stack = ClassStack()	#空のスタックを一つ用意
line = raw_input()	#一行入力

for word in line.split():
	if word == "?":
		print stack.top()
	elif word == "+":
		op1 = stack.top()
		stack.pop()
		op2 = stack.top()
		stack.pop()
		stack.push(op2+op1)
	elif word == "-":
		op1 = stack.top()
		stack.pop()
		op2 = stack.top()
		stack.pop()
		stack.push(op2-op1)
	elif word == "*":
		op1 = stack.top()
		stack.pop()
		op2 = stack.top()
		stack.pop()
		stack.push(op2*op1)
	elif word == "/":
		op1 = stack.top()
		stack.pop()
		op2 = stack.top()
		stack.pop()
		stack.push(op2/op1)
	elif word == "%":
		op1 = stack.top()
		stack.pop()
		op2 = stack.top()
		stack.pop()
		stack.push(op2%op1)
	else:
		stack.push(int(word))



