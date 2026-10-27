#store many items
ages = [21,72, 43, 76, 23, 78, 78, 90, 15] #list
names = ["Zack", "Jane", "Jack", "Jack", "Moha", "Rick"]

#functions
ages.append(31)

#ages.clear()
#ages.sort()

#ages.reverse() #reverse
print(ages)

jack_count = names.count("Jack")
print(jack_count)
print(len(names))
print(len(ages))
print(sum(ages))
print(sum(ages)/len(ages))

#retrive element
#print(names[0])
#print(names[-1])
#print(names[-2])

#print(ages[3:])
#print(ages[3:5])

#print(ages[:3])

#set
scores = {88, 78, 88, 65, 77, 78} #no duplicate
print(scores)
print(scores)
scores.add(90)
scores.remove(65)

#tuple immutable
weekdays = ("Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun")
print(weekdays)

#dictionary
person = {"name": "jason", "age": 22, "weight": 53, "height": 1.88}
print(person["name"])
print(person["age"])

people = [
    {"name": "Aria", "age": 29},
    {"name": "Morris", "age": 20},
    {"name": "Hellen", "age": 23}
]
print(people[0]["age"])

#loops
#for loops
#while

#for nums in range(1,1_000_001):
#   print(nums)

num = 0
while num <= 10:
    print(num)
    num += 1