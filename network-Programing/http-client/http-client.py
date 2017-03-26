#coding:utf-8
import socket	# socketライブラリの利用
import sys	#コマンド引数などを利用する

args = sys.argv

if not len(args) == 3:
	print "Usage : python %s URL FILENAME"%args[0]
	quit()

pos = args[1].find('//')
host = args[1][pos+2:]

pos = host.find("/")
host = host[:pos]

print "URL = ",args[1]
print "HOST = ",host


mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)	#socketの作成
								#3層(network層)にIPを使う、transport層にTCPを使う、ことを宣言
								#	ちなみにソケットって何かって言うと、
								#	+----+
								#	| || | プラグをさす相手側のこと。
								#	+----+



mysock.connect((host,80))
	#相手のソケットと、接続を行う
	#成功すると、TCP/IPでのパイプができる


mysock.send('GET %s HTTP1.0\n\n'%args[1])
	#パイプに対してアプリケーション層のHTTPを使って送信


picture = ''	#ダウンロードする画像データになる予定
		#「文字列」 = 「byteのリスト」

count = 0	#現在までのダウンロードデータの長さ


while True:
	data = mysock.recv(512)
	if len(data) < 1:
		break

	count = count + len(data)	#サイズの更新
	#print len(count)
	picture = picture + data	#dataのアペンド


mysock.close()


#通信終了後
#ヘッダを見つける
pos = picture.find("\r\n\r\n")		#空行を探している
					#HTTPでは「\r\n(CRLF)」で改行を意味する
					#	==>\r\n\r\nは空行。
#ヘッダの出力
print "Header length",pos
print picture[:pos]		#a:bでaからbまでという意味だった。


#データ部分を見つける
picture = picture[pos+4:]	#header +　空行を取り除いた残り

#ファイルに保存
fhand = open(args[2],"wb")	#cat.jpgにWrite & Binaryモードで出力
				#!unixでは改行はLF(\nつまりLFつまり10)一つ
				#!windowsでは改行はCR LF(つまり\r\nつまりCRLF つまり13 10)
				#!macでは改行はCR
				#c言語ではファイルの行末処理を行いかどうかによって、textモード(改行の処理を行う)かbinaryモード(改行の処理を行わない)
				#を選べる。unixでは意味はない。windowsだと、cの内部で、"\n"が"\r\n"に変わる。macでは"\n"が"\r"に変わるはず。
				#	unixはwbにしなくても、binaryモードにしなくても良い

				#ASCII Code
				#	アメリカの電子通信を行うときの文字コード
				#		普通の文字 : (アルファベット、数字、記号)
				#		制御コード
				#			CR : キャリッジリターン teltypeのヘッドを先頭に戻す の意味
				#			LF : 業送り : 髪を1行ぶん送る
				#
				#本来ASCIIのルールでは「改行」 = 「キャリッジリターン」+「先送り」
				# unix ではCRT(ブラウン菅表示の端末)
				#	改行は1byteで良いだろう。。。
				#
				#OSの違いによって改行の処理が異なるのは嫌だったので、
				#textモードでは標準ライブラリが吸収する規則にした。


fhand.write(picture)	#本当はこんなことはしてはいけない。readしながらwriteしなさい。
fhand.close()
