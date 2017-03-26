#coding:utf-8

import urllib

fhead = urllib.urlopen("http://ec2-52-41-23-150.us-west-2.compute.amazonaws.com/index.html");
	# urlを指定してファイルopen
	#	ファイルと同様に扱える
	#		ネットワーク上(にweb公開された)ファイルが普通にオープンできる.
	
for line in fhead:
	print line.strip()	#stripは改行を削っているだけ
