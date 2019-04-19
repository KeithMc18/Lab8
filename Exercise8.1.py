import random as rand


class Animal:

    def __init__(self, type_in):
        # rather than passing in an instance variable I used a guid to guarantee id will be unique
        self.id = rand.randint(1000, 9999)
        self.type = type_in

    def display_details(self):
        print('Animal:''\n')
        print('Id:                  ', self.id)
        print('Type:                ', self.type)


class Greyhound(Animal):

    def __init__(self, name_in, sex_in, father_in, mother_in):
        super().__init__(type_in='Greyhound')
        self.name = name_in
        self.sex = sex_in
        self.father = father_in
        self.mother = mother_in
        self.num_of_litters = 0
        self.num_of_pups = 0

    def update_breeding_record(self, pups_in):
        self.num_of_litters += 1
        self.num_of_pups += pups_in

    def display_details(self):
        super().display_details()
        print('Name :               ', self.name)
        print('Sex :                ', self.sex)
        print('Father :             ', self.father)
        print('Mother :             ', self.mother)
        print('Number of litters :  ', self.num_of_litters)
        print('Number of pups :     ', self.num_of_pups)


dog = Animal('Dog')
dog.display_details()

grey = Greyhound('frank', 'male', 'daddys-dog', 'some bitch')
grey.update_breeding_record(5)
grey.update_breeding_record(4)
grey.display_details()
