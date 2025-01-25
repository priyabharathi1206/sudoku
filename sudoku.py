print("Sudoku..")
print("lets start..")
# matrix=[[0]*3]*3. The program updates the matrix but uses shared lists ([0] * 3 repeated), causing all rows to share the same data
matrix=[[0 for _ in range(3)] for _ in range(3)]
count=5
point=0

def display():
    for i in range(0,3):
        for j in range(0,3):
            print(matrix[i][j],end=" ")
        print("\n")


def check(num,row,column):
    for i in range(0,3):
        if (matrix[row][i]==num):
            print("yes")
            return 0
        if (matrix[i][column]==num):
            print("yes")
            return 0
        
    return 1
        
name=input("Enter your name:")
print("your platform ...")
display()
print("You can start now..")
while(True):
    #position=input("position") 
    
    row=int(input("row:"))
    column=int(input("column:"))
    number=int(input("number:"))
    
    matrix[row][column]=number
    res=check(number,row,column)
    display()
    if(res==0):
        count=count-1
        if (count !=0):
            print("think and play")
            print(f"you have only {count} attempts")
        
    #print(matrix[row][column])    
    

