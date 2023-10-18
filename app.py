import datetime
import math
import flask

#variables
age = 22 #int(input("Please write your age: "))
weight = 82 #int(input("Please write your weight: "))
gender = "male" #str(input("Please write your gender (male/female): "))

def time_diff():
  time = (datetime.datetime.now())
  time_string = time.strftime('%H:%M')
  return time_string

time_of_intake = round(float(input("Please write your time of intake (eg. 12.30): ")))
real_time = round(float(time_diff().replace(':', '.')))
t = real_time - time_of_intake

#dictionary with a caffeine concentration multiplier
drinks = {
  "Caffee Latte": 0.404,
  "Cappuccino": 0.268,
  "Flat White": 0.45,
  "Espresso": 2.1,
  "Energy Drink": 0.32,
  "Dzik Energy Drink": 0.4
}

#algorithm
def algorithm():
  coffee = input("Please write type of the drink consumed: ")
  quantity = float(input("Please write consumed amount in ml: "))

  user_choice = str(coffee)
  d = (drinks.get(user_choice) * quantity) #caffeine in a chosen drink

  c = math.log(0.9) #coefficient
  CI = d * pow(t, c)
  print(CI)

algorithm()