#coding:utf-8
#
#while 文
#	条件が成立する間、文を実行し続ける
#
#[構文]
#	while 条件:	
#		文
#

sum = 0
i = int(raw_input('整数を入力してください'))
while i>0:
	sum = sum +i
	i = int(raw_input('整数を入力してください'))

print '合計は' + str(sum)
