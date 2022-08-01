
class Dog:

    count_animals = 0

    def __init__(self, name="Octavio"):
        self._name = name
        self._age = 13
        Dog.count_animals += 1



    def birthday(self):
        self._age += 1

    def get_age(self):
        print(self._name, self._age)

    def set_name(self, name):
        self._name = name

    def get_name(self):
        print(self._name)



def main():

    dog1 = Dog('Rocky')
    dog2 = Dog()
    #Lines from previous ex
    #dog1.birthday()
    #dog1.get_age()
    #dog2.get_age()
    dog1.get_name()
    dog2.get_name()
    print(Dog.count_animals)

if __name__ == '__main__':
    main()




