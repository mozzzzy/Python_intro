#coding:utf-8
#　「交通量シミュレーション」交差点(十字路)がある。そこに信号があり、それを制御して交通整理をしたい。車はランダムにやってきて、どれだけ渋滞したかを考える。
#
# 信号は
#	15秒 青	1台1秒で通過
#	5秒  黄 1台2秒で通過
#	20秒 赤 停止
#
#	一方が青や黄色の時は、他方は赤。
#	一方が赤になった時に、他方は青。
#
#
#	t		|0	|15	|20	|35	|40		...
#	----------------+-----------------------+-------+--------
#	Up/down		|R	|	|B	|Y	|R
#	Left/Right	|B	|Y	|R	|	|B
#

time = 0	#world time
next_time = 15


car_list_up = []	#上から下に向かって交差点を通過しようとしている車のリスト
car_list_down = []	#下から上
car_list_left = []	#左から右
car_list_right = []	#右から左

signal_up_down = "RED"
signal_left_right = "BLUE"

while time < 10000:
	if time == next_time:
		if signal_left_right == "BLUE":
			signal_left_right = "YELLOW"
			next_time = next_time +5
		elif signal_left_right == "YELLOW":
			signal_left_right = "RED"
			signal_up_down = "BLUE"
			next_time = next_time +15
		if signal_up_down == "BLUE":
			signal_up_down = "YELLOW"
			next_time = next_time +5
		elif signal_up_down == "YELLOW":
			signal_up_down = "RED"
			signal_left_right = "BLUE"
			next_time = next_time +15

	if signal_left_right == "BLUE":
		if len(car_list_left) > 0:
			pop(car_list_left)
		if len(car_list_left) > 0:
			pop(car_list_left)
	elif signal_left_right == "YELLOW":
		if len(car_list_left) > 0:
			pop(car_list_left)
	elif signal_up_down == "BLUE":
		if len(car_list_up) > 0:
			pop(car_list_up)
		if len(car_list_up) > 0:
			pop(car_list_up)
	elif signal_up_down == "YELLOW":
		if len(car_list_up) > 0:
			pop(car_list_up)


	print "Time =" + 
	print "Signal UP/DOWN" + signal_up_down
	print ""
		
