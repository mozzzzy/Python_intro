#coding:utf-8
#
#リストというデータ構造
#	気持ち : 何かの並びの事?
#			複数の要素からなり、それには順序がついている
#		 「何か」は(直感とは異なり)「値」ではなく「変数」
#			「リスト」は、「変数」の並びであり、
#			その個々の変数に「値」が代入できる
#			# 配列に近い
#	
#
#
#
#
#
#
#range(n,m)		
#	= [n,n+1,...,m-1]
#リストを作る関数
#
#
#
#	a[n:m] -> [n,n+1,...,m-1]
#	例 : a[3,7] -> [3,4,5,6]
#	len(a[n,m]) -> m-n
#		a[n,n+1] = a[n] = n
#		a[;m] -> a[0:m]
#		a[n:] -> a[n:len(a)]



#range関数の使い方
print range(1,10)	#[1,2,3,4,5,6,7,8,9]
print range(10)		#[0,1,2,3,4,5,6,7,8,9]

#リストの足し算
print ['a','c','e']
print ['b','d','f']
print ['a','c','e']+['b','d','f']	#

#リスト内の各データを選択して出力
print ['a','c','e'][0]
print ['a','c','e'][1]
print ['a','c','e'][2]

#.pop()の使い方
print ['a','c','e'].pop()	# -->'e'
				#popは一番最後をとってくる

#insertの使い方
v = ['a','b','c']
v.insert(0,'x')		#0個目の箱に'x'を入れる
print v
v = ['l','m','n']
print v
v[0] = 's'
print v		#書き換えができる. 配列に近い



#リスト内の負のデータを正に変換する関数 "remove_low(list_name)"
def remove_low(l):
	j=0
	for i in l:
		if i<0:
			l[j]=-i
		j=j+1

l=[1,-2,3,-4,5,-6]
print l
remove_low(l)
print l


#リスト内のデータのデータ型の確認
print type([1][0])

#リスト内包表記
print [i**2 for i in range(1,10)]


#リスト内包表記の書き換え
l=[]
for i in range(1,10):
	l.append(i*i)	#appendは最後に追加

print l


#まとめて定義
a=range(10)
print a[3:6]	#3,4,5

#listのソート
l=[1,3,5,4,2,6,8,7]
print l
l.sort()
print l
	
