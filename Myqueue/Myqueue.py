#
#	Myqueue
#

queue = []

def enqueue(x):
	queue.insert(0,x)

def top():
	return queue[len(queue)-1]

def dequeue():
	queue.pop()


###test main code
if __name__ == "__main__":
	enqueue(1)	#1_____
	enqueue(5)	#51____
	enqueue(3)	#351___
	print top()		#==>1
	dequeue()	#35____
	print top()		#==>5
	enqueue(7)	#735___
	enqueue(9)	#9735__
	dequeue()	#973___
	print top()	#	==>3
	dequeue()	#97____
	print top()	#	==>7
	dequeue()	#9_____
	print top()	#	==>9
