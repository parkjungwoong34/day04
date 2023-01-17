# 1
year_list = []
for year in range(1980, 1986):
    year_list.append(year)
print(year_list)
# 2
print(year_list[3])
# 3
print(year_list[-1])

# 7.8.9
surprise = ["Groucho", "Chico", "Harpo"]
surprise[-1] = surprise[-1].lower() # low Not affects
print(surprise)
surprise[-1] = surprise[::-1]
print(surprise[-1])
surprise[-1] = surprise[-1][0].capitalize()
print(surprise[-1])

# 10
number_list = [number for number in range(10) if number % 2 == 1]
print(number_list)

# 11

start1 = ["fee", "fie", "foe"]

rhymes = [
    ("flop", "get a mop"),
    ("fope", "turn the rope"),
    ("fa", "get your ma"),
    ("fudge", "call the judge"),
    ("fat", "pet the cat"),
    ("fog", "walk the dog"),
    ("fun", "say we're done"),
]
start2 = "Someone better"
start1_caps = " ".join([word.capitalize() + "!" for word in start1])
for first, second in rhymes:
    print(f"{start1_caps} {first.capitalize()}!")
    print(f"{start2} {second}.")