import datetime
import math
from data import user_data, drinks

def get_user_data():
  user_data["age"] = int(input("Please write your age: "))
  user_data["weight"] = int(input("Please write your weight: "))
  user_data["gender"] = input("Please write your gender (male/female): ")

def time_diff():
  time = (datetime.datetime.now())
  time_string = time.strftime('%H:%M')
  return time_string

def time_since():
  time_of_intake = round(float(input("Please write your time of intake (eg. 12.30): ")))
  real_time = round(float(time_diff().replace(':', '.')))
  t = real_time - time_of_intake
  return t

def algorithm():
  coffee = input("Please write type of the drink consumed: ")
  quantity = float(input("Please write consumed amount in ml: "))

  user_choice = str(coffee)
  d = (drinks.get(user_choice) * quantity) #caffeine in a chosen drink

  c = math.log(0.9) #coefficient
  CI = d * pow(time_since(), c)
  print("Your current caffeine concentration is", round(CI), "ml.")

get_user_data()
print(user_data)
algorithm()