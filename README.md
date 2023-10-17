# Caffeine Intake Calculator

This Python script allows users to calculate caffeine concentration in their body in real time.

## Algorithm

Algorithm is based on caffeine half-life in plasma and other factors.


$CI = d \times t^{c}$

$c = \log(0.9)$

Where,\
$CI$ - caffeine intake\
$d$ - caffeine content of a given drink\
$t$ - time since intake (hours)\
$c$ - coefficient estimated based on half-life


## Data

The script contains a dictionary named `drinks` that stores various drinks and their respective caffeine content based on data from <a href="https://www.coffeecode.co.uk" target="_blank">Coffee code</a>
:

```python
drinks = {
  "Caffee Latte (235 ml)": 95,
  "Cappuccino (235 ml)": 63,
  "Flat White (140 ml)": 63,
  "Espresso (30 ml)": 63,
  "Energy Drink (250 ml)": 80,
  "Energy Drink (500 ml)": 160,
  "Dzik Energy Drink (500 ml)": 200
}
```
## Author

<a href="https://www.linkedin.com/in/mariuszbaranski/" target="_blank"><b>Mariusz Barański</b></a>