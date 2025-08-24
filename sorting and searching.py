# Task 1

city_names = [
    "Tokyo", "Delhi", "Shanghai", "São Paulo", "Mumbai", "Mexico City", "Beijing", "Osaka", "Cairo", "New York City",
    "Dhaka", "Karachi", "Buenos Aires", "Istanbul", "Kolkata", "Manila", "Lagos", "Rio de Janeiro", "Los Angeles",
    "Moscow", "Kinshasa", "Tianjin", "Paris", "Lima", "Bangkok", "London", "Bogotá", "Chongqing", "Baghdad", "Tehran",
    "Bangalore", "Santiago", "Hyderabad", "Sydney", "Guangzhou", "Shenzhen", "Jakarta", "Tokyo", "Chicago", "Houston",
    "Luanda", "Berlin", "Madrid", "Singapore", "Toronto", "Barcelona", "Washington D.C.", "Miami", "Casablanca",
    "Dubai", "Kuala Lumpur", "Addis Ababa", "Hanoi", "Johannesburg", "Ho Chi Minh City", "Riyadh", "Khartoum",
    "Alexandria", "Melbourne", "Monterrey", "Tel Aviv", "Warsaw", "Buenos Aires", "Caracas", "Rome", "Naples", "Lima",
    "Lahore", "Abidjan", "Brisbane", "San Francisco", "Montreal", "Kabul", "Havana", "Vienna", "Brasília", "Helsinki",
    "Lisbon", "Stockholm", "Athens", "Prague", "Zurich", "Stuttgart", "Copenhagen", "Oslo", "Munich", "Managua",
    "Budapest", "Brussels", "Algiers", "Hobart", "Reykjavik", "Cape Town", "Nairobi", "Lusaka", "Accra", "Dakar",
    "Durban", "Tashkent", "Kigali", "Maputo", "Windhoek"]

def linear_search(city_names, target):
    for i in range(len(city_names)):
        if city_names[i] == target:
            return i
    return -1

target = input("Enter the City Name you'd like to look for: ")
index = linear_search(city_names, target)

if index != -1:
    print(f"City Name found at index number {index}!")
else:
    print("City Name not found!")

new_list = city_names.sort

print (city_names)

target = input("Enter the City Name you'd like to look for: ")

index = linear_search(city_names, target)

if index != -1:
    print(f"City Name found at index number {index}!")
else:
    print("City Name not found!")