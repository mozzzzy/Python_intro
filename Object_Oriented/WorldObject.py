# coding:UTF-8
#
# WorldObject.py
#

#
#
#

class WorldObject(object):
	def __init__(self,world):
		self.world = world
		world.add(self)

#
#
#



