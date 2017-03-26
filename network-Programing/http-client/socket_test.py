#coding:utf-8
import socket	# socketライブラリの利用を宣言


mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)	#socketの作成
								#3層(network層)にIPを使う、transport層にTCPを使う、ことを宣言
								#	ちなみにソケットって何かって言うと、
								#	+----+
								#	| || | プラグをさす相手側のこと。
								#	+----+



mysock.connect(('ec2-52-41-23-150.us-west-2.compute.amazonaws.com',80))
	#相手のソケットと、接続を行う
	#成功すると、TCP/IPでのパイプができる


mysock.send('GET http://ec2-52-41-23-150.us-west-2.compute.amazonaws.com/index.html HTTP1.0\n\n')
	#パイプに対してアプリケーション層のHTTPを使って送信



while True:
	data = mysock.recv(512)
	if len(data) < 1:
		break

	#標準出力に表示
	print data

	


mysock.close()
