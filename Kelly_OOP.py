class Pet:
    noise = " "
    species = "Mammal"
    def __init__(self,name,age,fur):
        self.name = name 
        self.age = age
        self.fur = fur
    def speak(self) :
        return ( '{} is {} years old and has {} fur. {} says {}'.format(self.name, self.age, self.fur,self.name, self.noise))

class Dog(Pet):
    noise = "Woof"
class Cat(Pet):
    noise = "Meow"     

pet_1 = Dog("Django",9,"Brown")
pet_2 = Cat("Crav",70, "White")
pet_3 = Dog("Brick", 3 , "Silver")
pet_4 = Cat("Dovley", 8, "Red")

if pet_1.age < pet_2.age and pet_1.age < pet_3.age and pet_1.age < pet_4.age :
    print(pet_1.speak())
elif pet_2.age < pet_1.age and pet_2.age < pet_3.age and pet_2.age < pet_4.age :
    print(pet_2.speak())
elif pet_3.age < pet_2.age and pet_3.age < pet_1.age and pet_3.age < pet_4.age :
    print(pet_3.speak())
elif pet_4.age < pet_2.age and pet_4.age < pet_3.age and pet_4.age < pet_1.age :
    print(pet_4.speak())
else:
    pass

