# Python Data Structures Exercises Solutions

# =============================================
# Exercise 1: Lists
# =============================================

print("=== EXERCISE 1: LISTS ===")

# 1. Create a list with 5 items (names of people) and output the 2nd item
names = ["Alice", "Bob", "Charlie", "Diana", "Edward"]
print(f"1. Second item: {names[1]}")

# 2. Change the value of the first item to a new value
names[0] = "Alexander"
print(f"2. List after changing first item: {names}")

# 3. Add a sixth item to the list
names.append("Fiona")
print(f"3. List after adding sixth item: {names}")

# 4. Add "Bathel" as the 3rd item in your list
names.insert(2, "Bathel")
print(f"4. List after adding 'Bathel' as 3rd item: {names}")

# 5. Remove the 4th item from the list
names.pop(3)
print(f"5. List after removing 4th item: {names}")

# 6. Use negative indexing to print the last item
print(f"6. Last item using negative indexing: {names[-1]}")

# 7. Create a new list with 7 items and use range of indexes to print 3rd, 4th and 5th items
seven_items = ["Item1", "Item2", "Item3", "Item4", "Item5", "Item6", "Item7"]
print(f"7. Items 3rd to 5th: {seven_items[2:5]}")

# 8. Write a list of countries and make a copy of it
countries = ["Uganda", "Kenya", "Tanzania", "Rwanda", "Burundi"]
countries_copy = countries.copy()
print(f"8. Original countries: {countries}")
print(f"   Copy of countries: {countries_copy}")

# 9. Loop through the list of countries
print("9. Looping through countries:")
for country in countries:
    print(f"   - {country}")

# 10. List of animal names and sort them in both orders
animals = ["Lion", "Elephant", "Zebra", "Giraffe", "Cheetah"]
animals_ascending = sorted(animals)
animals_descending = sorted(animals, reverse=True)
print(f"10. Animals ascending: {animals_ascending}")
print(f"    Animals descending: {animals_descending}")

# 11. Output only animal names with letter 'a' in them
animals_with_a = [animal for animal in animals if 'a' in animal.lower()]
print(f"11. Animals with 'a': {animals_with_a}")

# 12. Join two lists (first names and second names)
first_names = ["John", "Jane", "Mike"]
second_names = ["Doe", "Smith", "Johnson"]
full_names = first_names + second_names
print(f"12. Joined names: {full_names}")

print("\n" + "="*50)

# =============================================
# Exercise 2: Tuples
# =============================================

print("=== EXERCISE 2: TUPLES ===")

# 1. Output favorite phone brand from tuple
x = ("samsung", "iphone", "tecno", "redmi")
favorite_phone = x[1]  # Assuming iphone is favorite
print(f"1. My favorite phone brand: {favorite_phone}")

# 2. Use negative indexing to print 2nd last item
print(f"2. Second last item: {x[-2]}")

# 3. Update "iphone" to "itel" (convert to list, modify, convert back)
phone_list = list(x)
phone_list[1] = "itel"
x_updated = tuple(phone_list)
print(f"3. Updated tuple: {x_updated}")

# 4. Add "Huawei" to tuple
x_with_huawei = x + ("Huawei",)
print(f"4. Tuple with Huawei: {x_with_huawei}")

# 5. Loop through the tuple
print("5. Looping through phones:")
for phone in x:
    print(f"   - {phone}")

# 6. Remove/delete first item (convert to list, remove, convert back)
phone_list = list(x)
phone_list.pop(0)
x_without_first = tuple(phone_list)
print(f"6. Tuple without first item: {x_without_first}")

# 7. Create tuple of cities in Uganda using constructor
uganda_cities = tuple(["Kampala", "Entebbe", "Jinja", "Mbarara", "Gulu"])
print(f"7. Uganda cities: {uganda_cities}")

# 8. Unpack the tuple
city1, city2, city3, city4, city5 = uganda_cities
print(f"8. Unpacked cities: {city1}, {city2}, {city3}, {city4}, {city5}")

# 9. Use range of indexes to print 2nd, 3rd and 4th cities
print(f"9. Cities 2nd to 4th: {uganda_cities[1:4]}")

# 10. Join two tuples (first names and second names)
first_names_tuple = ("John", "Jane", "Mike")
second_names_tuple = ("Doe", "Smith", "Johnson")
full_names_tuple = first_names_tuple + second_names_tuple
print(f"10. Joined name tuples: {full_names_tuple}")

# 11. Create tuple of colors and multiply by 3
colors = ("red", "blue", "green")
colors_multiplied = colors * 3
print(f"11. Colors multiplied by 3: {colors_multiplied}")

# 12. Count occurrences of 8 in tuple
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count_8 = thistuple.count(8)
print(f"12. Number 8 appears {count_8} times in the tuple")

print("\n" + "="*50)

# =============================================
# Exercise 3: Sets
# =============================================

print("=== EXERCISE 3: SETS ===")

# 1. Create set of 3 favorite beverages using constructor
beverages = set(["Coffee", "Tea", "Juice"])
print(f"1. Favorite beverages: {beverages}")

# 2. Add 2 more items to beverages set
beverages.add("Water")
beverages.add("Soda")
print(f"2. Beverages after adding 2 items: {beverages}")

# 3. Check if microwave is present in the set
mySet = {"oven", "kettle", "microwave", "refrigerator"}
is_microwave_present = "microwave" in mySet
print(f"3. Is microwave present? {is_microwave_present}")

# 4. Remove "kettle" from the set
mySet.remove("kettle")
print(f"4. Set after removing kettle: {mySet}")

# 5. Loop through the set
print("5. Looping through mySet:")
for item in mySet:
    print(f"   - {item}")

# 6. Add list elements to set
my_set = {"apple", "banana", "cherry", "date"}
my_list = ["elderberry", "fig"]
my_set.update(my_list)
print(f"6. Set after adding list elements: {my_set}")

# 7. Join two sets (ages and first names)
ages_set = {25, 30, 35}
names_set = {"Alice", "Bob", "Charlie"}
joined_set = ages_set.union(names_set)
print(f"7. Joined sets: {joined_set}")

print("\n" + "="*50)

# =============================================
# Exercise 4: Strings
# =============================================

print("=== EXERCISE 4: STRINGS ===")

# 1. Concatenate integer and string
age = 25
name = "Alice"
result = str(age) + " " + name
print(f"1. Concatenated: {result}")

# 2. Remove spaces from beginning, middle, and end
txt = "      Hello,       Uganda!       "
cleaned_txt = " ".join(txt.split())
print(f"2. Cleaned string: '{cleaned_txt}'")

# 3. Convert to uppercase
txt_upper = cleaned_txt.upper()
print(f"3. Uppercase: {txt_upper}")

# 4. Replace 'U' with 'V'
txt_replaced = txt_upper.replace('U', 'V')
print(f"4. Replaced U with V: {txt_replaced}")

# 5. Return range of characters in 2nd, 3rd and 4th position
y = "I am proudly Ugandan"
substring = y[1:4]
print(f"5. Characters at positions 2-4: '{substring}'")

# 6. Correct the error in the string
x = 'All "Data Scientists" are cool!'
# or
x_alternative = "All \"Data Scientists\" are cool!"
print(f"6. Corrected string: {x}")

print("\n" + "="*50)

# =============================================
# Exercise 5: Dictionaries
# =============================================

print("=== EXERCISE 5: DICTIONARIES ===")

# Dictionary for exercises
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

# 1. Print the value of shoe size
print(f"1. Shoe size: {Shoes['size']}")

# 2. Change "Nick" to "Adidas"
Shoes["brand"] = "Adidas"
print(f"2. Updated brand: {Shoes}")

# 3. Add key/value pair "type": "sneakers"
Shoes["type"] = "sneakers"
print(f"3. Added type: {Shoes}")

# 4. Return list of all keys
keys_list = list(Shoes.keys())
print(f"4. All keys: {keys_list}")

# 5. Return list of all values
values_list = list(Shoes.values())
print(f"5. All values: {values_list}")

# 6. Check if "size" key exists
size_exists = "size" in Shoes
print(f"6. Does 'size' key exist? {size_exists}")

# 7. Loop through the dictionary
print("7. Looping through dictionary:")
for key, value in Shoes.items():
    print(f"   {key}: {value}")

# 8. Remove "color" from dictionary
Shoes.pop("color")
print(f"8. After removing color: {Shoes}")

# 9. Empty the dictionary (create a copy first to preserve for demo)
shoes_copy = Shoes.copy()
shoes_copy.clear()
print(f"9. Empty dictionary: {shoes_copy}")

# 10. Create dictionary and make a copy
my_dict = {"name": "John", "age": 30, "city": "Kampala"}
my_dict_copy = my_dict.copy()
print(f"10. Original: {my_dict}")
print(f"    Copy: {my_dict_copy}")

# 11. Nested dictionaries
nested_dict = {
    "person1": {
        "name": "Alice",
        "age": 25,
        "city": "Kampala"
    },
    "person2": {
        "name": "Bob",
        "age": 30,
        "city": "Entebbe"
    }
}
print("11. Nested dictionary:")
for person, details in nested_dict.items():
    print(f"    {person}: {details}")

print("\n" + "="*50)
print("All exercises completed successfully!")