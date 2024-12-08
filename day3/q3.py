import re

with open("input3.txt") as file:
    fileText = file.read()

def getValidInstructionNums(text):
    pattern = r"mul\((-?\d+),(-?\d+)\)"
    validInstuctionNums = re.findall(pattern, text)
    return validInstuctionNums

def getDoBlocks(text):
    startText = re.match(r'^(.*?)(?=do\(\)|don\'t\(\)|$)', text, re.DOTALL)
    doBlocks = re.findall(r'do\(\)(.*?)(?=do\(\)|don\'t\(\)|$)', text, re.DOTALL)

    validBlocks = []

    if startText:
        startText =startText.group(1)
        if not re.search(r'^.*don\'t\(\)', startText):
            validBlocks.append(startText)
    
    validBlocks.extend(doBlocks)

    return validBlocks

def part1():
    
    numPairs = getValidInstructionNums(fileText)

    acc = 0

    for num1, num2 in numPairs:

        num1 = int(num1)
        num2 = int(num2)

        acc += (num1 * num2)

    print(acc)
    return acc

def part2():

    blocks = getDoBlocks(fileText)
    acc = 0

    for block in blocks:
        print(block)
        numPairs = getValidInstructionNums(block)

        for num1, num2 in numPairs:
            num1 = int(num1)
            num2 = int(num2)

            acc += (num1 * num2)

    print(acc)
    return acc


part1()
part2()