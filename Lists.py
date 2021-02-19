lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Oscar", "Toby"]

friends.extend(lucky_numbers)  # appends two lists together
friends.append("Creed")  # appends individual element
friends.insert(1, "Kelly")  # appends individual element in middle of list
friends.remove("Jim")  # removes element from the list
friends.clear()  # clears list
friends.pop()  # removes last element of list
friends.index("Kevin")  # returns index of found element
friends.count("Jim")  # returns how often element is found in list
friends.sort()  # sorts list to alphabetical order
lucky_numbers.sort()  # sorts list in ascending order
lucky_numbers.reverse()  # reverses order of list
friends2 = friends.copy()   # creates copy of list

print(friends)
