def converter(mpg):
    # Conversion factors
    liters_per_gallon = 4.54609188  # 1 imperial gallon is equal to 4.546 liters
    kilometers_per_mile = 1.60934  # 1 mile is equal to 1.609 kilometers

  # Kilometers per liter is calculated by multiplying mpg by conversion factors
    kmpl = mpg * (kilometers_per_mile / liters_per_gallon)
    return round(kmpl, 2)
