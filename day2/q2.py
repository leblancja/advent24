
def isSafe(lineArr):
    ascending = None
    for i in range(1, len(lineArr)):
        diff = lineArr[i] - lineArr[i-1]
        if abs(diff) < 1 or abs(diff) > 3:
            return False
        
        if ascending is None:
            ascending = diff > 0

        elif (ascending and diff < 0) or (not ascending and diff > 0):
            return False
        
    return True
    
def hasSingleError(lineArr):
    for i in range(len(lineArr)):
        temp_line = lineArr[:i] + lineArr[i + 1:]
        if isSafe(temp_line):
            return True
    return False

def part1():
    numSafe = 0

    for line in file:
        nums = [int(num) for num in line.split()]
        
        if isSafe(nums):
            numSafe += 1
    
    print(numSafe)
    return numSafe

def part2():
    numSafe = 0
    
    for line in file:
        nums = [int(num) for num in line.split()]
        
        if(isSafe(nums)):
            numSafe += 1
        
        elif(hasSingleError(nums)):
            numSafe += 1    
        


    print(numSafe)
    return numSafe

file = open("input2.txt")
part1()
file.close
file = open("input2.txt")
part2()
file.close


