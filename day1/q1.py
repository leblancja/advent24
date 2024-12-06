
file = open("input1.txt")

list1 = []
list2 = []

for line in file:
    left, right = line.split("   ")
    
    list1.append(int(left))
    list2.append(int(right))
    
a = list1.sort()
b = list2.sort()

def part1():
    diff = [abs(a-b) for a, b in zip(list1, list2)]
    res = sum(diff)
    print(res)
    return
    
def part2():
