#coding:utf-8

try:
	while True:	#TrueはTが大文字じゃないとエラー
		print '文字列を入力してください'
		a = raw_input()	#入力を行う(EOFかもしれない)
		print a		#出力を行う(EOFの時はexceptに飛んでここには来ない)
	
except:
	print 'EOF'
