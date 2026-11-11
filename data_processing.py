import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
for city in cities[:5]:
    print(city)
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = [float(city['temperature']) for city in cities]
print(sum(temps)/len(temps))
print()

# Print all cities in Germany
print(f"All of cities in Germany")

for city in cities:
    if city["country"] == "Germany":
        print(city)
print()

# Print all cities in Spain with a temperature above 12°C
print(f"All cities in Spain with a temperature above 12")

for city in cities:
    if city["country"] == "Spain" and float(city["temperature"]) > 12:
        print(city)
print()

# Count the number of unique countries
print(f"Count the number og unique countries")

countries = set()

for city in cities:
    countries.add(city["country"])

print(len(countries))
print()

# Print the average temperature for all the cities in Germany
print(f"The average temperature for all the cities in Germany")

temps = []

for city in cities:
    if city["country"] == "Germany":
        temps.append(float(city["temperature"]))

print(sum(temps) / len(temps))
print()

# Print the max temperature for all the cities in Italy
print(f"The max temperature for all the cities in Italy")

temps = []

for city in cities:
    if city["country"] == "Italy":
        temps.append(float(city["temperature"]))

print(max(temps))
print()

def filter_items(condition, dict_list):
    result = []

    for item in dict_list:
        if condition(item):
            result.append(item)

    return result


def aggregate(aggregation_key, aggregation_function, dict_list):
    values = []

    for item in dict_list:
        values.append(item[aggregation_key])

    return aggregation_function(values)

#commit 2

# Print the average temperature of all the cities
print(f"The average temperature of all the cities")

print(aggregate("temperature", lambda values: sum(float(x) for x in values) / len(values), cities))
print()

# Print all cities in Germany
print(f"All cities in Germany")

germany_cities = filter_items(lambda city: city["country"] == "Germany", cities)
for city in germany_cities:
    print(city)
print()

# Print all cities in Spain with a temperature above 12°C
print(f"All cities in Spain with a temperature above 12°C")

spain_cities = filter_items(lambda city: city["country"] == "Spain"and float(city["temperature"]) > 12,cities)
for city in spain_cities:
    print(city)
print()

# Count the number of unique countries
print(f"Count the number of unique countries")

print(aggregate("country",lambda values: len(set(values)),cities))
print()

# Print the average temperature for all the cities in Germany
print(f"The average temperature for all the cities in Germany")

print(aggregate("temperature",lambda values: sum(float(x) for x in values) / len(values),germany_cities))
print()

# Print the max temperature for all the cities in Italy
print(f"The max temperature for all the cities in Italy")

italy_cities = filter_items(lambda city: city["country"] == "Italy",cities)
print(aggregate("temperature",lambda values: max(float(x) for x in values),italy_cities))
print()