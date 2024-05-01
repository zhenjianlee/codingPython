import random

setSize = int(input("Input array size:"))
setTarget = int(input("Input target number:"))
array = []
for i in range(setSize):
    array.append(random.randint(0, 10))

# [ 1 2 3 4 5 6 ] , target = 7

def findTwoSum(target):
    dic ={}
    for i in range(len(array)):
        check = target - array[i]
        if array[i] not in dic:
            dic[check]=i
        else:
            print("FOUND! " + str(check)+" and "+ str(array[i]))
            return [dic[array[i]],i]
        print(dic)



res= findTwoSum(setTarget)
print("Array="+str(array)+" Target="+str(setTarget)+ " Result="+str(res))