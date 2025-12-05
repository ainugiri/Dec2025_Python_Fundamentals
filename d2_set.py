devTeam  = {12,5, 17,19,12, 17, 19, 101, 21,101,121,101}
#           0, 1, 2,               3,  4,   5
# list  = []
# tuple = ()
# dict = { key:value, key=value }
# set = {}
print(f"The developers are {devTeam}")

testTeam = {6,7,8,9,10,12,12,11}
print(f"The Testers are {testTeam}")

commonPeople = devTeam.intersection(testTeam)
print(f"Both Dev and Test Team {commonPeople}")

# venn diagram 

teamA = {1,2,3,4}
teamB = {3,4,5,6}
teamC = {2,4,6,8}
print(teamA.intersection(teamB))
print(teamB.intersection(teamC))
print(teamA.intersection(teamC))
print(teamA.intersection(teamC).intersection(teamB))

print(teamA.union(teamB))
print(teamA.union(teamB).union(teamC))


# Only teamB
onlyA = teamA - teamB - teamC
print(onlyA)

onlyB = teamB - teamC - teamA
print(onlyB)

onlyC = teamC - teamA - teamB
print(onlyC)

symetDiff = teamA.symmetric_difference(teamB)
print(symetDiff)

print(3 in teamA)
print(13 in teamA)

# unique
# remove duplicates
# mathematical in datascience
# membership function check item in the collection
# value in set * 13 in teamB -> True / False