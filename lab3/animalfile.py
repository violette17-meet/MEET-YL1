class Animal(object):
	def __init__(self, sound, name, age ):
		self.sound=sound
		self.name=name
		self.age=age
	def eat(self,food):
		print(self.name+" is eatiing" + food )
	def sleep(self,dream):
		print("The "+ str(self.age)+ " years old "+ self.name +" is dreaming about "+dream)


