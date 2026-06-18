# Enter your code here. Read input from STDIN. Print output to STDOUT


if '__main__' == __name__:
    # i had to ignore the group number because i haven't seen the purpose of having it
    input()
    # then got the rooms
    user = input()
    members = user.split() 
    
    rooms = {}
    
    for i in members:
        item = int(i)
        if item in rooms:
            # if the item exists in the dictionary just add the count to be one
            rooms[item] += 1
        else:
            # if not just count it as one
            rooms[item] = 1
    
    for i in rooms:
        # since the captain room only will have 1 person , the count will be 1 which confirms the room number of the captain
        if rooms[i] == 1:
            print(i)
            break

