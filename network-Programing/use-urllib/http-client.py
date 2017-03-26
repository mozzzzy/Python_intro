#coding:utf-8

import urllib
import sys

args = sys.argv

if not len(args) == 2:
	print "Usage : python %s URL" %args[0]
	quit();


url = args[1]

fhead = urllib.urlopen(url);
	# urlを指定してファイルopen
	#	ファイルと同様に扱える
	#		ネットワーク上(にweb公開された)ファイルが普通にオープンできる.
	
for line in fhead:
	print line.strip()	#stripは改行を削っているだけ


