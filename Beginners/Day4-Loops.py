
# The basic Version
# /\/\/\/\\/\/\/\/\/\/\/\
# if __name__ == '__main__':
#     n = int(input())
#     i=0
    
#     while(i<n):
#         print(i**2)
#         i+=1
     
# A better version without the need of initialization    
if __name__ == '__main__':
    n= int(input())
    for i in range(n):
        print(i**2)