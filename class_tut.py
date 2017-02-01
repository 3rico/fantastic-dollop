class customer(object):
 def __init__(self, name, balance=0.0):
  self.name = name
  self.balance = balance 
 def withdraw(self, amount):
  if amount > self.balance: 
   raise RuntimeError ('Amount greater than aavailable balance')
  self.balance -= amount
  #return self.balance
 def deposit(self, amount):
  self.balance += amount
  #return self.balance
 def total(self):
  return self.balance


# make a customer

jeff = customer('jeff',1000.0)
jeff.deposit(10000)
jeff.withdraw(1000)
jeff.total()


jeff=customer('jeff',100)
eric=customer('Eric',1000000000)
betty=customer('betty',10000)
rita=customer('rita',10000000)

jeff.withdraw(1000)

jeff.deposit(100000)
eric.deposit(1000000)
betty.deposit(10000000)
rita.deposit(100000000)

jeff.withdraw(10000)
eric.withdraw(10000000)
betty.withdraw(1000000)
rita.withdraw(10000000)


class car(object):
 wheels = 4
 def __init__(self, make, model):
  self.make = make
  self.model = model
 @staticmethod
 def make_car_sound():
  print('voooooooommm!!!')
 
