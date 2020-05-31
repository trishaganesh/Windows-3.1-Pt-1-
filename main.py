# Ask the user for a list of 3 friends 
# For each friend, we'll tell the user whether they are nearby 
# For each nearby friend, we'll save their name to 'nearby_friends.txt'

friends = input('Enter three friend names, separated by commas (no spaces, please): ').split(',')

people = open('people.txt', 'r')
people_nearby = people.readlines()  

people.close()

friends_set = set(friends)
people_nearby_set = set(people_nearby)

friends_nearby_set = friends_set.intersection(people_nearby_set)