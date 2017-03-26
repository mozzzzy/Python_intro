#coding:UTF-8


from ClassStack import ClassStack

priority = {"+":1,"-":1,"*":2,"/":2,"%":3,"?":4}


stack = ClassStack()
line = raw_input()

for word in line.split():
	if word in priority:	# 演算子だったら
		while not stack.empty() and priority[word] <= priority[stack.top()]:
			print " " + stack.top()
			stack.pop()
		stack.push(word)
	else:
		print " " + word

