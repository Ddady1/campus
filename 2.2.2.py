
class Dog:

    def __init__(self):
        self.name = 'rexi'
        self.age = 13

    def birthday(self):
        self.age += 1

    def get_age(self):
        print(self.name, self.age)



def main():

    dog1 = Dog()
    dog2 = Dog()
    dog1.birthday()
    dog1.get_age()
    dog2.get_age()

if __name__ == '__main__':
    main()




