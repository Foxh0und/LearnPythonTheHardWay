##Animal is-a object
class Animal( object ):
    pass

##Dog is-a Animal
class Dog( Animal ):

    def __init( self, aName ):
        ##Dog has-a name
        self.fName = aName

##Cat is-a Animal
class Cat( Animal ):

    def __init( self, aName ):
        ##Cat has-a name
        self.fName = aName

##Person is-a Name
class Person( object ):

    def __init( self, aName ):
        ##Person has-a name and pet
        self.fName = aName
        self.fPet = none

## Employee is-a perosn
class Employee( Person ):

        def __init__( self, aName, aSalary ):
            ##Employee has-a name and salary
            super( Employee, self ).__init__( name )
            self.fSalary = aSalary

##Fish is-a object
class Fish( object ):
    pass

##Salmon is-a fish
class Salmon( Fish ):
    pass

##Halibut is-a fish
class Halibut( Fish ):
    pass

##lRover is a Dog and has-name rover
lRover = Dog( "Rover" )

##lSatan is-a cat and has-a name Satan
lSatan = Cat( "Satan" )

##lMary is-a person has-a name Mary
lMary = Person( "Mary" )

##lMary has-a pet which is now lSatan
lMary.fPet = lSatan

##lFrank is-a employee and his salary is 1200
lFrank = Employee( "Frank", 12000 )

##lFrank's pet is lRover
lFrank.fPet = lRover

##lFlipper is-a fish
lFlipper = Fish()

## lCrouse is-a salmon
lCrouse = Salmon()

## lHarry is-a halibut
lHarry = Halibut
