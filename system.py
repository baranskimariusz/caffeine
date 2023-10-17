import datetime
import math

#variables
age = 22#int(input("Please write your age: "))
weight = 82#int(input("Please write your weight: "))
gender = "male"#str(input("Please write your gender (male/female): "))
time_of_intake = 18#float(input("Please write your time of intake (eg. 12.30): "))
#real_time = round(float(datetime.datetime.now()))

#dictionary https://coffeecode.co.uk/how-much-caffeine-in-coffee/
drinks = {
  "Caffee Latte": 95,
  "Cappuccino": 63,
  "Flat White": 63,
  "Espresso": 63,
  "Small Energy Drink": 80,
  "Large Energy Drink": 160,
  "Dzik Energy Drink": 200
}

#algorithm
coffee = input("Please write type of the drink consumed: ")
user_choice = str(coffee)
d = drinks.get(user_choice) #caffeine in a chosen drink

t = float(20) - time_of_intake #time passed since intake real_time
c = math.log(0.9) #coefficient

CI = d * pow(t, c)
print(CI)