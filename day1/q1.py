
file = open("input1.txt")

list1 = []
list2 = []

for line in file:
    left, right = line.split("   ")
    
    list1.append(int(left))
    list2.append(int(right))
    


def part1():
    a = list1.sort()
    b = list2.sort()

    diff = [abs(a-b) for a, b in zip(list1, list2)]
    res = sum(diff)

    print(res)
    return res
    
def part2():

    sims = []

    for num in list1:
         sims.append(num * (list2.count(num)))

    res = sum(sims)
    print(res)
    return res

part1()
part2()