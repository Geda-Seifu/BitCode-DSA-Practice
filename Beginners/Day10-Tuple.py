if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    
    MyTupleList = tuple(integer_list)
    print(hash(MyTupleList))

# this is my attempt but Hacker rank is not accepting my submission
# the output i get on my machine is -3550055125485641917 but what hackerRank expect is 3713081631934410656