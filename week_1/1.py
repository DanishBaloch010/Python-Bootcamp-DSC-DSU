
str = input("Enter a Word : ")

def diagonal(string):
    space=''
    for charIndex in range(len(string)):
        # first char with no following space
        if charIndex==0:
            print(string[charIndex])
        
        else:
            print(space,string[charIndex]) 
            space=space+' '
     
def reverseDiagonal(string):
    space=""
    for i in range(len(string)):
        space=space+" "
    space=space[:-1]
    for charIndex in range(len(string)):
        if(charIndex==(len(string)+1)):
            print(string[charIndex])
        else:
            print(space,string[charIndex])
            space=space[:-1]
             
diagonal(str)
reverseDiagonal(str)
diagonal(str)
reverseDiagonal(str)







