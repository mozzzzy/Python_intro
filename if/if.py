#coding:utf-8
#
#if分の使い方
#	if文は条件によって二つの文のどちらか一方を実行する.
#	[構文]
#		if 条件:
#			文1
#		elif 条件:
#			文2
#		else:
#			文3
#	文2がからの場合は、else:は省略可能
#


#if else
print '整数を入力しなさい'
i = int(raw_input())
if i>=0:
	print '正の整数'
else:
	print '負の整数'


#if elif else
print '再度,整数を入力しなさい'
i = int(raw_input())
if i>100:
	print 'over 100'
elif i>50:
	print 'over 50'
else:
	print 'under 50'






