#Sal's Shipping
import random

weight = random.randint(1,50)

#Ground Shipping
if weight <= 2:
  cost_ground = weight * 1.50 + 20.00
elif weight > 2 and weight <= 6:
  cost_ground = weight * 3.00 + 20.00
elif weight > 6 and weight <= 10:
  cost_ground = weight * 4.00 + 20.00
elif weight > 10:
  cost_ground = weight * 4.75 + 20.00  

print("Ground shipping total:",cost_ground)

premium_ground = 125

print("Premium Ground Shipping has a flat fee of $", premium_ground)

total_premium = cost_ground + 125
print("Premium Ground Shipping total:",total_premium)

#Drone Shipping
if weight <= 2:
  drone_ship = weight * 4.50
elif weight > 2 and weight <= 6:
  drone_ship = weight * 9.00
elif weight > 6 and weight <= 10:
  drone_ship = weight * 12.00
elif weight > 10:
  drone_ship = weight * 14.25

print("Drone Shipping cost total:",drone_ship)

