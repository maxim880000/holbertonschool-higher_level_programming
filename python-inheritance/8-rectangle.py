#!/usr/bin/python3


class Rectangle(BaseGeometry):
	"""classe rectangle qui herite de BaseGeometry"""
	def __init__(self, width, height):
		"""méthode qui est appelée quand tu crées un nouvel objet
		initialise t valeur de depart"""
		self.__width = width
		self.__height = height
