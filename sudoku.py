print("Sudoku..")
print("lets start..")
# matrix=[[0]*3]*3. The program updates the matrix but uses shared lists ([0] * 3 repeated), causing all rows to share the same data
matrix=[["*" for _ in range(3)] for _ in range(3)]
count=5
point=0

def display():
    for i in range(0,3):
        for j in range(0,3):
            print(matrix[i][j],end=" ")
        print("\n")


def check(num,row,column):
    for i in range(0,3):
        # print(i)
        if (matrix[row][i]==num):
            print("yes")
            return 0
    for i in range(0,3):
        # print(i)
        if (matrix[i][column]==num):
            print("yes1")
            return 0
        
    print("no")   
    return 1

def final():
    for i in range(0,3):
        for j in range(0,3):
           if matrix[i][j]=="*":

                return 0

    for row in range(0,3):
        num=matrix[row][0]
        if (matrix[row][1]==num)or (matrix[row][2]==num):
            return 0
    for column in range(0,3):
        num=matrix[0][column]
        if (matrix[1][column]==num)or (matrix[2][column]==num):
            return 0
    return 1

def result(final):
    if final==0:
        print(f"you lost with {point} points")
    else:
        print(f"you won...apalause with {point} points")



#main
name=input("Enter your name:")
print("your platform ...")
display()
print("You can start now..")
while(True):
    #position=input("position") 
    
    row=int(input("row:"))
    column=int(input("column:"))
    number=int(input("number:"))
    
    
    res=check(number,row,column)
    matrix[row][column]=number
    print(res)
    display()
    if(res==0):
        
        if (count !=0):
            count=count-1
            point=point-5
            print("think and play")
            print(f"you have only {count} attempts with {point} points")
        else:
            print(f"your attempts completed with {point} points...try new game")
            break
    else:
        point=point+10
        print(f"points:{point}")
    finall=final()  
    if finall==1:
        break

result(final())

    #print(matrix[row][column])    
    

