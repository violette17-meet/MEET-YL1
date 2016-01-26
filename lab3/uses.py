from animalfile import *
import random
name=["samir","george","charlie","noura","aminah","nour","maya","faris","jiries","yousef","mario","musa","baseel","haitham"]
age=[12,13,14,15,16,18]
for i in range(50):
	dog = Animal("woof",name[random.randint(0,13)],str(age)[random.randint(0,5)])
	dog.eat("Bamba")

	

dog = Animal("woof","jeff",17)
cat = Animal("meow","lolo",4)


print(dog.sound)
dog.eat("Bamba")
cat.eat("Bamba")
dog.sleep("bed")
cat.sleep("food")
