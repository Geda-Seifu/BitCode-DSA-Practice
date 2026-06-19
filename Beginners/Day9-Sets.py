# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    N = int(input())
    # this thing doesn't consider it a set when it's initiated with {}, it thinks this is a dictionary 
    listOfStamps = set()
    for _ in range(N):
        item = input()
        listOfStamps.add(item)
        
    print(len(listOfStamps))