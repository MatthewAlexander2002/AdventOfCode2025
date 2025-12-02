import math

def main():
    total = 0
    with open("Day2/input.txt", 'r') as file:
        for text in file:
            updated = text.split(",")
            for num in updated:
                nums = num.split("-")
                print(nums)
                for x in range(int(nums[0]),int(nums[1])+1):
                    digits = [int(digit) for digit in str(x)]
                    length: int = len(digits)
                    if search(digits, length):
                        print(x)
                        total+=x
    print(total)
#takes in the number as an array and the length of the array
#digits = [int(digit) for digit in str(number)]
def search(digits, length):
    result = False
    mid = int(length/2)+1
    for window in range(1,mid):
        window_con = True
        for pos in range(0,length, window):
            if(digits[pos:pos+window]!=digits[0:window]):
                window_con = False
                break
        if(window_con):
            return True
    return False
                 
if __name__ == "__main__":
    main()
    
    
#im not reading the last window of possibilities i need to step through an 
# question and figure out why the window is missing that last result