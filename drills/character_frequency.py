# google.com'
# result :  {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

name = "google.com"
name = "rubenn"

#brute force go throug string len(n) times and check if current char is repeated without countind itself

#print(len(name))

result = {}

for index in range(len(name)):
    counter = 0
    for index2 in range(len(name)):
        if name[index] == name[index2]:
            counter+=1

    result[name[index]] = counter

print(result)



# sort the string

#two pointer count if next is equal before
    #increment counter and keep checking until !=
    # feed the empty set

    #reset count

    #do the same next character

    # feed the empty set with one and move pointers

    # if last letter there's no next stop, if previous was != update set with last char

