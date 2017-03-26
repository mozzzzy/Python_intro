# coding:UTF-8
#
# Car.py
#

from WorldObject import *

#
#
#

class Car(WorldObject):		#WorldObjectを継承している
        car_number = 0
	def __init__(self,world,x,y,direction):	# 新しいデータを作る場合呼ぶ
                super(Car,self).__init__(world)
		self.x=x
		self.y=y
		self.direction=direction
		self.number = Car.car_number
                Car.car_number = Car.car_number + 1

	def tick(self):
		if self.direction == "UP":
			self.y = self.y - 1
                elif self.direction == "DOWN":
			self.y = self.y + 1
		elif self.direction == "LEFT":
                        self.x = self.x - 1
		elif self.direction == "RIGHT":
			self.x = self.x + 1
		if self.world.dead_end(self):
			self.world.remove(self)

        def draw(self,stdscr):
		stdscr.addstr(self.y-1,self.x-1,'+-+')
		stdscr.addstr(self.y  ,self.x-1,'+%c+' % (ord('a')+self.number) )
		stdscr.addstr(self.y+1,self.x-1,'+-+')


