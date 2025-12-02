import math

def main():
    dir = 50
    counter = 0
    
    with open("Day1/input.txt", 'r') as file:
        # file_content = file.read()
        for line in file:
            dir_start = dir
            dir_line = line[0]
            line.strip
            int_line = int(line[1:])
            counter += math.floor(int_line/100)
            int_line = int_line%100
            
            if dir_line == 'L':
                if dir < int_line:
                    diff = int_line-dir
                    dir = 100-diff
                    # counter += 1
                else:
                    # if dir == int_line:
                    #     counter += 1
                    dir = dir-int_line
            else:
                dir = (dir+int_line)%100
            if (dir_line == 'L') & (dir_start < dir): #& (dir_start != 0):
                counter += 1
            if (dir_line == 'R') & (dir_start > dir):
                counter += 1
    print(counter)             
    
if __name__ == "__main__":
    main()