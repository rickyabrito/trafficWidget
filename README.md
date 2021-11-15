# gitTest

# just trying out things ya know?

def car_listing(car_prices):
  result = ""
  for cars in car_prices:
    result += "{} costs {} dollars".format(cars,car_prices[cars]) + "\n" # iterating cars (keys) through car_prices; then in .format, using cars as the keys and car_prices[cars] to be able to iterate throught the values without creating another for loop
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))