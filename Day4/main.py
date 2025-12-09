def main():
    size = 10
    arr2d = [[""]*size]*size
    x = 0
    y = 0
    with open("Day4/test.txt", 'r') as file:
        for line in file:
            line = line.strip()
            for char in line:
                arr2d[x][y] = char
                y+=1
            x+=1
            y=0
    
    print(search(arr2d, size))
    
def search(arr2d, size):
    total = 0
    size = size-1
    
    #first pos handler
    if(arr2d[0][0] == "@"):
        total+=1
     
    #top right corner   
    if(arr2d[0][size] == "@"):
        total+=1
    
    #first row
    for firstRow in range(1, size):
        if(arr2d[0][firstRow] == "@"):
            count = 0
            if(arr2d[0][firstRow-1] == "@"): #left
                count+=1
            if(arr2d[0][firstRow+1] == "@"): #right
                count+=1
            if(arr2d[1][firstRow] == "@"): #up
                count+=1
            if(arr2d[1][firstRow-1] == "@"): #up left
                count+=1
            if(arr2d[1][firstRow+1] == "@"): #up right
                count+=1
            if(count < 4):
                total+=1
    
    #first column
    for firstColumn in range(1, size):
        if(arr2d[firstColumn][0] == "@"):
            count = 0
            if(arr2d[firstColumn-1][0] == "@"): #down
                count+=1
            if(arr2d[firstColumn+1][0] == "@"): #up
                count+=1
            if(arr2d[firstColumn][1] == "@"): #right
                count+=1
            if(arr2d[firstColumn-1][1] == "@"): #right down
                count+=1
            if(arr2d[firstColumn+1][1] == "@"): #right up
                count+=1
            if(count < 4):
                total+=1
    
    #last pos
    if(arr2d[size][size] == "@"):
        total+=1
        
    #bottom left corner
    if(arr2d[size][0] == "@"):
        total+=1
    
    #last row
    for lastRow in range(1, size):
        if(arr2d[0][lastRow] == "@"):
            count = 0
            if(arr2d[size][lastRow-1] == "@"): #left
                count+=1
            if(arr2d[size][lastRow+1] == "@"): #right
                count+=1
            if(arr2d[size-1][lastRow] == "@"): #down
                count+=1
            if(arr2d[size-1][lastRow-1] == "@"): #down left
                count+=1
            if(arr2d[size-1][lastRow+1] == "@"): #down right
                count+=1
            if(count < 4):
                total+=1
    
    #last column
    for lastColumn in range(1, size):
        if(arr2d[lastColumn][0] == "@"):
            count = 0
            if(arr2d[lastColumn-1][size] == "@"): #down
                count+=1
            if(arr2d[lastColumn+1][size] == "@"): #up
                count+=1
            if(arr2d[lastColumn][size-1] == "@"): #left
                count+=1
            if(arr2d[lastColumn-1][size-1] == "@"): #left down
                count+=1
            if(arr2d[lastColumn+1][size-1] == "@"): #left up
                count+=1
            if(count < 4):
                total+=1
    
    #need to handle last
    for x in range(1, size-1):
        for y in range(1, size-1):
            count = 0
            if(arr2d[y-1][x] == "@"): #down
                count+=1
            if(arr2d[y-1][x-1] == "@"): # down left
                count+=1
            if(arr2d[y-1][x+1] == "@"): #down right
                count+=1
            if(arr2d[y][x-1] == "@"): #left
                count+=1
            if(arr2d[y][x+1] == "@"): #right
                count+=1
            if(arr2d[y+1][x] == "@"): #up
                count+=1
            if(arr2d[y+1][x-1] == "@"): #up left
                count+=1
            if(arr2d[y+1][x+1] == "@"): #up right
                count+=1
            if(count < 4):
                total+=1
    
    return total
    
if __name__ == "__main__":
    main()