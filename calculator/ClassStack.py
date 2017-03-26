#coding:utf-8

#
# ClassStack.py
#


class ClassStack:	#新しいクラスClassStackを作る
	def __init__(self):	#新しいデータを作るときに呼ぶ
		self.stack=[]	#空のリストを作る。
				#selfは別の文字列でも良い

	def push(self,x):
		self.stack.append(x)

	def pop(self):
		self.stack.pop()

	def top(self):
		return self.stack[len(self.stack)-1]

	def clear(self):
		self.stack = []

	def empty(self):
		return len(self.stack) == 0 
