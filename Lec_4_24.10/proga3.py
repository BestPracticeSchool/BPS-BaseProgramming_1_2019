#РЕАЛИЗАЦИИ МАССИВОВ
#В Python существует 2 реализации массивов: списки и кортежи

#Списки --- list()
my_list = [10, 20, 30, 40, 5, -1, 20]
print(my_list[0], my_list[1])
print("Last element of my_list is: ", my_list[6])
print("Last element of my_list is: ", my_list[-1])
print(my_list[-3])
print(my_list[-0])

#Empty list()

my_list_1 = []
print(type(my_list_1))
my_list_2 = list()

#Dop elemts

print("##############################")
nums = [20,30,40,100,200,300,4,3,5,6, 20]
nums.append(98)
print(nums)
nums.pop()
print(nums)

print(dir(nums))

print(nums.count(20))
print(nums.index(30))
print(nums.index(20))

nums.sort(reverse = True)
print(nums)


print("##################################")
print(sum(nums))
print(len(nums))

average = sum(nums) / len(nums)
print(average)




















