#coding:utf-8
#ファイル名 , クラス名
from ClassStack import ClassStack	#こうしないとClassStack.ClassStack()とか書かないといけなくなる

s1 = ClassStack()	#新しいオブジェクトが作られる
			#同時にClassStack.__init__()が呼び出されて、s1.stackが[]になる

s1.push(1)	#s1.push(1) ==> push(s1,1)になる
s1.push(2)
print s1.top()
s1.pop()
print s1.top()
s1.pop()
print type(s1)
print dir(ClassStack)
