if __name__ == '__main__':
    N = int(input())
    
    myList = []
    
    for i in range(N):
        command = input().split()
        action = command[0]
        if(action == 'insert'):
            # this insert method is so durable 🔥🔥🔥
            myList.insert(int(command[1]), int(command[2]))
        elif (action == 'print'):
            print(myList)
        elif (action == 'remove'):
            myList.remove(int(command[1]))
        elif (action == 'append'):
            myList.append(int(command[1]))
        elif (action == 'sort'):
            myList.sort()
        elif (action == 'pop' ):
            myList.pop()
        elif (action == 'reverse') :
            myList.reverse()
            
            
        
