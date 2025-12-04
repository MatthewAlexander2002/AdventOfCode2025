def main():
    total = 0
    with open("Day3/input.txt", 'r') as file:
        for text in file:
            int_arr = []
            text = text.strip()
            for num in text:
                int_arr.append(num)
            total += greedy(int_arr)

    print(total)
    
def greedy(arr):
    while len(arr) != 2:
        for pos in range(0, len(arr)):
            if(pos == len(arr)-1): #not sure if its in the right most position it needs to delete
                arr.pop(pos)
                break
            elif(arr[pos]<arr[pos+1]):
                arr.pop(pos)
                break
    
    final_int_string = ""
    for num in arr:
        final_int_string = final_int_string + num
        
    return int(final_int_string)

if __name__ == "__main__":
    main()