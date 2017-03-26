#coding:utf-8

#
# ClassTest.py : classの作成,インスタンス化のサンプルコード.
#

#新しいclassの作成
class TestClass:

	#class変数
	test_class_variable = 0

	#コンストラクタ
	def __init__(self):	#新しくinstance化した際に呼び出される.
		print "new instance of TestClass is created."	#コンストラクタが
								#実行された事を確認
								#するためのデバッグ出力
		test_list = []	#空のリスト作成してみる


	#method
	def test_method1(self):
		self.test_list.insert(1);
		


#classを継承して新しいclassを作成
class TestClass2(TestClass):

	#コンストラクタのオーバーライド
	def __init__(self):
		print "new instance of TestClass2 is created."
	


#debug用main
if __name__ == "__main__":

	#TestClassの instance化
	test_instance1 = TestClass()
	test_instance2 = TestClass2()
