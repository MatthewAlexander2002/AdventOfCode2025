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
                    stuff:str = str(x)
                    length = len(stuff)
                    mid = int(length/2)
                    half1 = stuff[:mid]
                    half2 = stuff[mid:]
                    if half1 == half2:
                        total += x
    print(total)
                 
if __name__ == "__main__":
    main()