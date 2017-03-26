# coding:UTF-8
#
# World.py
#

import random
import curses
import time

from Car import *

#
#
#

class	World(object):
        def __init__(self):
		self.stdscr = curses.initscr()
                curses.noecho()
                curses.cbreak()
                self.y_max=24
		self.x_max=78
                self.car_width=4*2
                self.y_up=(self.y_max-self.car_width)/2
                self.y_down=(self.y_max+self.car_width)/2
                self.x_left=(self.x_max-self.car_width)/2
                self.x_right=(self.x_max+self.car_width)/2
                self.obj_list=[]

	def add(self,obj):
		self.obj_list.append(obj)

	def remove(self,obj):
		self.obj_list.remove(obj)

	def draw_road(self):
	        for x in range(0,self.x_max):
			self.stdscr.addch(self.y_up,x,ord('-'))
			self.stdscr.addch(self.y_down-1,x,ord('-'))
	        for y in range(0,self.y_max):
			self.stdscr.addch(y,self.x_left,ord('|'))
			self.stdscr.addch(y,self.x_right,ord('|'))
		for x in range(self.x_left,self.x_right+1):
		        for y in range(self.y_up,self.y_down):
				self.stdscr.addch(y,x,ord(' '))

        def draw(self):
		self.stdscr.clear()
                self.draw_road()
                for car in self.obj_list:
			car.draw(self.stdscr)
                self.stdscr.refresh()

        def tick(self):
                for car in self.obj_list:
			car.tick()

	def start(self):
	        for t in range(0,100):
			self.draw()
#	                self.stdscr.getch()
			time.sleep(0.3)
                        self.tick()
                        if t % 2 == 0:	#2秒に一回carを生成
	                        self.add_new_car()
		curses.endwin()

        def add_object(self,obj):
                self.obj_list.append(obj)

	def add_new_car(self):
		direction = random.randint(0,3)
                if direction == 0:
			car = Car(self,5,10,"RIGHT")
                elif direction == 1:
			car = Car(self,self.x_max-5,13,"LEFT")
                elif direction == 2:
			car = Car(self,37,self.y_max-2,"UP")
                else:
			car = Car(self,41,2,"DOWN")

	def dead_end(self,car):
	        if car.x < 2:
			return 1
		elif car.x > self.x_max - 2:
			return 1
	        elif car.y < 2:
			return 1
		elif car.y > self.y_max - 2:
			return 1
		else:
			return 0
#
#
#

if __name__ == "__main__":
        world = World()
	world.add_new_car()
	world.start()
