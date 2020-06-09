class Person:

    def __init__(self, name, age, pay=0, job=None):
        self.name = name
        self.age = age
        self.pay = pay
        self.job = job

    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)

    def changeJob(self, job):
        self.job = job

class Manager(Person):
    def giveRaise(self, percent, bonus=0.1):
        self.pay *= (1.0 + percent + bonus)


foltest = Person('Foltest', 40, 1000000, 'king of Temeria')
sobaka = Person('Sobaka', 8, 100000000, 'possession of BOMJ')

print (foltest.job)
print (sobaka.job)

foltest.giveRaise(49)
print(foltest.pay)

sobaka.changeJob('owner of BOMJ')
print(sobaka.job)
