# -*- coding: utf-8 -*- 
#
# 関数定義について
#


def iprint(v):
        print "整数"
        print v

def fprint(v):
        print "実数"
        print v

def myprint(v):
	if type(v) == int:
		iprint(v)
	elif type(v)== float:
		fprint(v)


myprint(1)

myprint(1.0)
