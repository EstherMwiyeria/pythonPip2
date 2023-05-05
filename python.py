# 1. Write a Python program to get a single string from two given strings, 
# separated by a space, and swap the first two characters of each string

def swap_names(name1, name2):
    new_name = name2[:2] + name1[2:]
    new_name2 = name1[:2] + name2[2:]

    return new_name + " " + new_name2
print(swap_names("draw", "paint"))



# 2.  Write a Python function that takes a list of words and returns the longest
#  word and the length of the longest one
def list_of_words(words):
    count = 0

    for i in words:
        if len(i)>=count:
            count=len(i)
            return count
print(list_of_words(["MaryAnne","JaneClever","Blige"]))

# 3. Write a Python program that accepts a comma-separated sequence of words 
# as input and prints the distinct words in sorted form (alphanumerically).
def sort_distinct_words(words):
    words = words.split(",")
    
    words = [word.strip() for word in words]
   
    distinct_words = sorted(set(words))

    return distinct_words
print(sort_distinct_words("kelly,nelly,bekky,lely,shelly,velly"))



# 4.. Write a Python function that takes two lists and returns True if they have
#  at least one common member.
def common_member(list_a,list_b):
    result = False
    for x in list_a:
        for y in list_b:
            if x == y:
                result = True
                return result
print(common_member([1,2,3,4,5], [5,6,7,8,9]))


# 5. Write a Python program to convert a list to a list of dictionaries.
# Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
def list_to_dict(keys, values):
    dict_list = [{keys[i]: values[i]} for i in range(len(keys))]
    return dict_list
print(list_to_dict(["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]))

result = [num for num in range(1, 1001) if any(num % d == 0 for d in range(2, 10))]
print(result)


# 6. Write a Python program to check whether all dictionaries in a list are empty or not
my_list = [{},{},{}]
print(all(not d for d in my_list))

# 7. Given a list of numbers, use list comprehension to remove all odd numbers from the list:
# numbers = [3,5,45,97,32,22,10,19,39,43]
numbers = [3,5,45,97,32,22,10,19,39,43]
even_numbers = [n for n in numbers if n%2 == 0 ]
print(even_numbers)

# 8. Find the common numbers in two lists (without using a tuple or set) 
# list_a = 1, 2, 3, 4, 
# list_b = 2, 3, 4, 5

list_a = [1,2,3,4]
list_b = [2,3,4,5]
common_numbers = [x for x in list_a if x in list_b]
print (common_numbers)

# 9. Use a nested list comprehension to find all of the numbers from 1-1000 that
#  are divisible by any single digit besides 1 (2-9)
total_numbers=list(range(1,1000))
total_nums=list(range(2,9))
y = [number for number in range(1,1000) if True in [True for x in range(2,9) if number % x == 0]]
print(y)

# 10. Write a Python function to remove all vowels in a string
def remove_vowels(country):
    # empty = []
    vowels = ["a","b","c","d","e"]
    empty = ""
    for i in range(len(country)):
        if country[i] not in vowels:
            empty += country[i]
    return empty

print(remove_vowels("Kenya"))