class Animal :

        def __init__(self,name,specie):

                self.__name = name 
                self.specie = specie 
        
        def getAnimal (self):
                
                print(f"{self.__name} is a {self.specie}")

       
                

class Dog(Animal):
        
        def bark (self):
                print(f"{self.__name} was Barking")

        def __del__ (self):
                print("Object is Delete Sucessfully...")


dog = Dog("Suraj", "Dog")
dog.getAnimal()
dog.bark()
                