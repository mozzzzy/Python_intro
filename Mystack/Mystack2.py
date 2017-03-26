#coding:utf-8

#
# Mystack2.py
#	...複数のスタックを使えるようにする



# null stack (実態はlist)
stackDic = {};	#stack辞書

def newStack(name):
	stackDic[name]=[]	#key であるnameに対応するlistを作る

#stack ________ ==> x_______
def push(name,x):
	stackDic[name].append(x)

#stack x_______ ==> ________
def pop(name):
	stackDic[name].pop()

#stack x_______ --> x
def top(name):
	return stackDic[name][len(stackDic[name])-1]


