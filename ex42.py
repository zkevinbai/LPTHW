# apparently he wants a simpler version of translating code to english, fine
# so be it, c'est la vie

# animal is-a object
class Animal(object):
    pass

# class Dog is-a Animal and has-a __init__ with parameters self and name
class Dog(Animal):

    def __init__(self, name):
        #Dog has-a name
        self.name = name
        print self.name

#cat is-a animal
class Cat(Animal):

    def __init__(self, name):
        #cat has-a name
        self.name = name
        print self.name

#person is-a object
class Person(object):

    def __init__(self, name):
        #person has-a name
        self.name = name
        print self.name

        # Person has-a pet of some kind
        self.pet = None

#employee is-a person
class Employee(Person):

    def __init__(self, name, salary):
        #class Employee is-a person
        # super is an inheritance trick that avoids writing out the enntire
        # name of a parent function, but not highly useful
        super(Employee, self).__init__(name)
        #Person has-a salary
        self.salary = salary
        print self.salary

# Fish is-a object
class Fish(object):
    pass

# Salmon is-a Fish
class Salmon(Fish):
    pass

# rover is-a Dog
rover = Dog("Rover")

# satan is-a Cat
satan = Cat("Satan")

# mary is-a Person
mary = Person("Mary")

# mary has-a pet satan
mary.pet = satan

# frank is-a employee with name frank and salary 120000
frank = Employee("Frank", 120000)

# frank has-a pet roverr
frank.pet = rover

# flipper is-a fish
flipper = Fish()

# crouse is-a salmon
crouse = Salmon()

# this doesnt do anything since halibut is not defined
harry = Halibut()
