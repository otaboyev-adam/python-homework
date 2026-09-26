# # 1-question

# list_0 = ['a', 'b', 'c', 'd', 'b']
# element = 'a'

# print(list_0.count(element))



#2-question

# list_1 = [1,2,3,4,5,6,7,8,9]
# sum_of_list = sum(list_1)
# print(sum_of_list)



#3-question


# list_2 = [1,2,3,4,5,6,7,8,9]
# max_value = max(list_2)
# print(max_value)




# 4-question



# list_3 = [1,2,3,4,5,6,7,8,9]
# min_value = min(list_3)
# print(min_value)



# 5-question


# list_4 = ['apple', 'banana', 'cherry', 'date']
# element_to_check = 'banana' in list_4
# print(element_to_check)



# 6-question


# list_5 = [1, 2, 3, 4, 5]
# if list_5:
#     print(list_5[0])
# else:
#     print("The list is empty.")



# 7-question

# list_6 = [1, 2, 3, 4, 5]
# if list_6:
#     print(list_6[-1])
# else:
#     print("The list is empty.")




# 8-question


# list_7 = [1, 2, 3, 4, 5]
# list_7_sliced = list_7[1:4]
# print(list_7_sliced)



# 9-question


# list_8 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# list_8_reversed = list(reversed(list_8))
# print(list_8_reversed)






# 10-question


# list_9 = [5,3,2,1,4]
# list_9_sorted = sorted(list_9)
# print(list_9_sorted)





# 11-question


# list_10 = [1,1,2,2,3,3,4,4,5,5]
# list_10_unique = list(set(list_10))
# print(list_10_unique)





# 12-question


# list_11 = [1,2,4,5,6,7,8,9]
# element_to_insert = 3
# list_11.insert(2, element_to_insert)






# 13-question


# list_12 = [1,2,3,4,5]
# element_to_look_for = 3
# print(list_12.index(element_to_look_for))




# 14-question


# list_13 = [1,2,3,4,5]
# print(bool(list_13))



# 15-question 


# list_14 = [1,2,3,4,5,6,7,8,9,10,11,13,15]
# even_count = sum(number % 2 == 0 for number in list_14)
# print(even_count)


# # 16-question 


# list_15 = [1,2,3,4,5,6,7,8,9,10,11,13,15]
# odd_count = sum(number % 2 == 1 for number in list_15)
# print(odd_count)





# 17-question


# list_01 = [1,2,3,4]
# list_02 = [5,6,7,8]

# new_list = list_01 + list_02
# print(new_list)




# 18-question


# main_list = [1, 2, 3, 4, 5]
# sublist = [3, 4]

# for i in range(len(main_list)):
#     if main_list[i:i + len(sublist)] == sublist:
#         print(True)
#         break
# else:
#     print(False)





# 19 - question 


# list_019 = [1,2,3,4,5,6,7,9]

# what_to_remove = int(input("O'zgartirmoqchi bo'lgan sonni kiriting: "))
# what_to_insert = int(input("O'rniga qaysi sonni kiritamiz: "))

# f_index = list_019.index(what_to_remove)
# list_019[f_index] = what_to_insert

# print(list_019)




# 20 - question 


# list_200 = [6,5,3,7,9,2,4,78,2,3]
# list_200.sort()
# print(f'second largest num is {list_200[-2]}')



# 21 - question 


# list_201 = [6,5,3,7,9,2,4,78,2,3]
# list_201.sort()
# print(f'second smallest num is {list_201[2]}')



# 22-question 



# list_220 = [1,2,3,4,5,6,7,8,9]
# list_even_nums = []

# for i in list_220:
#     if i % 2 == 0:
#         list_even_nums.append(i)

# print(list_even_nums)




# 23-question




# list_230 = [1,2,3,4,5,6,7,8,9]
# list_odd_nums = []

# for i in list_230:
#     if i % 2 == 1:
#         list_odd_nums.append(i)

# print(list_odd_nums)





# 24-question 



# list_240 = [1,23,4,56,8,9,8765,43,245,678,98,2]

# print(len(list_240))




# 25-question


# list_250 = [1,2,3,45,6,78,76,54,567]
# list_251 = list_250.copy()

# print(list_251)





# 26-question



# list_260 = [12,3,4,32,45,53,13,35,6]

# middle = len(list_260) // 2

# if middle % 2 == 0:
#     print(list_260[middle - 1 : middle + 1])
# else:
#     print(list_260[middle])






# 27-question 


# numbers = [10, 4, 7, 2, 15, 8, 3]

# sublist = numbers[1:6]

# print(max(sublist))



# # 28-question

# numbers = [10, 4, 7, 2, 15, 8, 3]

# sublist = numbers[1:6]

# print(min(sublist))



#29-question


# list_290 = [1111,3234568,23,65,32,78,89,54]
# index_of_num_to_remove = int(input("O'chirmoqchi bo'lgan soniingiz indexi: "))

# del list_290[index_of_num_to_remove]
# print(list_290)







# 30-question


# list_300 = [1,2,3,4,5,67,7,8,4,]

# print(list_300 == sorted(list_300))




# 32-question


# list_310 = [1,2,3,4,5,6]
# list_311 = [7,8,9,0]

# merged_sorted = list_310 + list_311
# merged_sorted.sort()

# print(merged_sorted)



# 31-question 


# list_320 = [1,2,3,4,6,7,8,9]
# multiplier = int(input("Necha marta takrorlansin: "))
# list_321 = []


# for i in list_320:
#     list_321.extend([i] * multiplier)

# print(list_321)





# 33-question

# numbers = [5, 2, 7, 2, 9, 2, 1]
# element = 2

# indexes = []

# for i in range(len(numbers)):
#     if numbers[i] == element:
#         indexes.append(i)

# print(indexes)






# 34-question 


# list_340 = [1,2,3,45,6,7,8,9]

# rotated = list_340[-1:] + list_340[0:-1]

# print(rotated)





# 35-question

# list_350 = []
# range_1 = int(input("qaysi sondan boshlansin: "))
# range_0 = int(input("qaysi songacha: "))

# for i in range(range_1, range_0):
#     list_350.append(i)

# print(list_350)





# 36-question


# list_360 = [1,2,3,4,5,6,7,-9,-8]

# sum_of_positive = 0


# for i in list_360:
#     if i > 0:
#         sum_of_positive += i

# print(sum_of_positive)





# 37-question



# list_370 = [1,2,3,4,5,6,7,-9,-8]

# sum_of_negative = 0


# for i in list_360:
#     if i < 0:
#         sum_of_negative += i

# print(sum_of_negative)




# 38-question


# list_380 = [1,2,2,1]

# print(list_380 == list_380[::-1])





# 39-question


# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# size = int(input("nechta elementdan bo'linsin: "))
# result = []

# for i in range(0, len(numbers), size):
#     result.append(numbers[i:i+size])


# print(result)


# 40-question

# list_400 = [1,2,3,45,0,7,3,3,7,54,2,4,6,8,4,2,4,6,8,9,4,2]
# result = []


# for i in list_400:
#     if i not in result:
#         result.append(i)

# print(result)





# Tuple tasks
# # 1-question 

# numbers = (1, 2, 3, 2, 4, 2)
# element = 2

# print(numbers.count(element))






# 2-question

# tuple_020 = (1,2,3,4,5,6,7,8)

# print(max(tuple_020))




# 3-question 


# tuple_030 = (1,2,3,4,5,6,8)

# print(min(tuple_030))



# 4 - question


# tuple_040 = (1,2,3,45,6,7,8,97654)
# element = 4

# print(element in tuple_040)



# 5- question


# tuple_050 = (1,2,3,4,5,7)

# if bool(tuple_050) == True:
#     print(tuple_050[0])
# else:
#     print("tuple is empty")



# 6 - question 

# tuple_060 = (1,2,3,4,5,7)

# if bool(tuple_060) == True:
#     print(tuple_060[-1])
# else:
#     print("tuple is empty")




# 7 - question 


# tuple_070 = (1,2,3,4,5,6, "adddf", 'l')

# print(len(tuple_070))





# 8-question

# numbers = (1, 2, 3, 4, 5)

# new_tuple = numbers[:3]

# print(new_tuple)








# 9-question

# numbers = (1, 2, 3, 4, 5)

# new_tuple = numbers[:3]

# print(new_tuple)





# 10-question


# numbers = ()

# print(bool(numbers))




# 11-question

# numbers = (5, 2, 7, 2, 9, 2, 1)
# element = 2

# indexes = []

# for i in range(len(numbers)):
#     if numbers[i] == element:
#         indexes.append(i)

# print(indexes)






# 12-question 


# numbers = (5, 2, 7, 2, 9, 2, 1)

# numbers = sorted(numbers)

# print(numbers[-2])






# 13-question

# numbers = (5, 2, 7, 2, 9, 2, 1)

# numbers = sorted(numbers)

# print(numbers[-2])






# 14-question

# element = 5

# my_tuple = (element,)

# print(my_tuple)







# 15-question

# numbers = [1, 2, 3, 4, 5]

# numbers_tuple = tuple(numbers)

# print(numbers_tuple)








# 16-question


# numbers = (1, 2, 3, 4, 5)

# print(numbers == tuple(sorted(numbers)))





# 17-question

# numbers = (10, 4, 7, 2, 15, 8)

# subtuple = numbers[1:5]

# print(max(subtuple))




# 18-question 


# numbers = (10, 4, 7, 2, 15, 8)

# subtuple = numbers[1:5]

# print(min(subtuple))






# 19-question


# numbers = (1, 2, 3, 2, 4)

# element = 2

# if element in numbers:
#     index = numbers.index(element)
#     new_tuple = numbers[:index] + numbers[index + 1:]
# else:
#     new_tuple = numbers

# print(new_tuple)




# 20-savol


# numbers = (1, 2, 3, 4, 5, 6, 7, 8)
# size = 2

# result = []

# for i in range(0, len(numbers), size):
#     result.append(numbers[i:i + size])

# result = tuple(result)

# print(result)





# 21-question


# numbers = (1, 2, 3)
# times = 3

# result = ()

# for element in numbers:
#     result += (element,) * times

# print(result)





# 22-question

# numbers = tuple(range(1, 11))

# print(numbers)




# 23-question

# numbers = (1, 2, 3, 4, 5)

# reversed_tuple = numbers[::-1]

# print(reversed_tuple)




# 24-question


# numbers = (1, 2, 3, 2, 1)

# print(numbers == numbers[::-1])




# 25-quest



# numbers = (1, 2, 2, 3, 1, 4)

# result = ()

# for element in numbers:
#     if element not in result:
#         result += (element,)

# print(result)












#      SET tasks


# 1 - question

# set_1 = {1, 2, 3}
# set_2 = {3, 4, 5}

# result = set_1 | set_2

# print(result)






# 2- question

# set_1 = {1, 2, 3}
# set_2 = {2, 3, 4}

# result = set_1 & set_2

# print(result)






# 3- question

# set_1 = {1, 2, 3}
# set_2 = {2, 3, 4}

# result = set_1 - set_2

# print(result)






# 4 - question


# set_1 = {1, 2}
# set_2 = {1, 2, 3, 4}

# print(set_1.issubset(set_2))






# 5 -question 


# numbers = {1, 2, 3, 4}
# element = 3

# print(element in numbers)







# 6- question


# numbers = {1, 2, 3, 4}

# print(len(numbers))






# 7 - question


# numbers = [1, 2, 2, 3, 3, 4]

# result = set(numbers)

# print(result)






# 8 - question


# numbers = {1, 2, 3, 4}
# dis_num = 3
# numbers.discard(dis_num)

# print(numbers)






# 9 - question 


# numbers = {1, 2, 3}

# new_set = numbers.clear()

# print(new_set)








# 10 - question 

# numbers = set()

# print(bool(numbers))






# 11-quest


# set_1 = {1, 2, 3}
# set_2 = {3, 4, 5}

# result = set_1 ^ set_2

# print(result)




# 12 - question 


# numbers = {1, 2, 3}
# add_num = 4 
# numbers.add(add_num)

# print(numbers)






# 13 - question 


# numbers = {1, 2, 3, 4}

# removed = numbers.pop()

# print(removed)
# print(numbers)





# 14 - question


# numbers = {5, 2, 8, 1, 9}

# print(max(numbers))




# 15 - question 


# numbers = {5, 2, 8, 1, 9}

# print(min(numbers))




# 16 - question 



# numbers = {1, 2, 3, 4, 5, 6}
# result = {number for number in numbers if number % 2 == 0}

# print(result)





# 17 - question 

# numbers = {1, 2, 3, 4, 5, 6}
# result = {number for number in numbers if number % 2 != 0}

# print(result)





# 18 -question 

# starting_num = 5
# ending_num = 9
# numbers = set(range(starting_num, ending_num))

# print(numbers)





# 19 - question 

# list_1 = [1, 2, 3]
# list_2 = [3, 4, 5]

# result = set(list_1 + list_2)

# print(result)







# 20 - question 

# set_1 = {1, 2, 3}
# set_2 = {4, 5, 6}

# print(set_1.isdisjoint(set_2))





# 21 - question 


# numbers = [1, 2, 2, 3, 3, 4]
# result = list(set(numbers))

# print(result)







# 22- question 


# numbers = [1, 2, 2, 3, 3, 4]

# print(len(set(numbers)))





# 23 - question 

# import random
# result = set(random.sample(range(1, 21), 5))
# print(result)












#                                 DICTIONARY questions







# 1- question


# student = {
#     "name": "Adam",
#     "age": 20
# }

# print(student.get("name"))





# 2 -question 


# student = {
#     "name": "Adam",
#     "age": 20
# }

# print("name" in student)





# 3 - question 


# student = {
#     "name": "Adam",
#     "age": 20,
#     "city": "Tashkent"
# }

# print(len(student))






# 4 - question 


# student = {
#     "name": "Adam",
#     "age": 20
# }

# keys = list(student.keys())

# print(keys)







# 5 - question 


# student = {
#     "name": "Adam",
#     "age": 20
# }

# values = list(student.values())

# print(values)








# 6 - questin


# dict_1 = {"a": 1, "b": 2}
# dict_2 = {"c": 3, "d": 4}

# result = dict_1 | dict_2

# print(result)









# 7 - question 


# student = {
#     "name": "Adam",
#     "age": 20
# }

# student.pop("age", None)

# print(student)







# 8 - question 

# student = {
#     "name": "Adam",
#     "age": 20
# }

# new_dict = student.clear()

# print(new_dict)












# 9 - question 

# student = {}

# print(bool(student))








# 10 - question 


# student = {
#     "name": "Adam",
#     "age": 20
# }

# key = "name"

# if key in student:
#     print((key, student[key]))
# else:
#     print(None)






# 11 - question 

# student = {
#     "name": "Adam",
#     "age": 20
# }

# student["age"] = 21

# print(student)








# 12 - question 



# student = {
#     "name": "Adam",
#     "age": 20
# }

# student["age"] = 21

# print(student)




# 13 - question 


# student = {
#     "a": 1,
#     "b": 2,
#     "c": 3
# }

# result = {}

# for key, value in student.items():
#     result[value] = key

# print(result)




# 14 - question 


# students = {
#     "Adam": 20,
#     "Ali": 21,
#     "John": 20
# }

# value = 20

# result = []

# for key in students:
#     if students[key] == value:
#         result.append(key)

# print(result)







# 15 - question 

# keys = ["name", "age", "city"]
# values = ["Adam", 20, "Tashkent"]

# result = dict(zip(keys, values))

# print(result)




#  16-question 

# student = {
#     "name": "Adam",
#     "info": {
#         "age": 20
#     }
# }

# result = False

# for value in student.values():
#     if isinstance(value, dict):
#         result = True
#         break

# print(result)



# 17 - question


# student = {
#     "name": "Adam",
#     "info": {
#         "age": 20,
#         "city": "Tashkent"
#     }
# }

# print(student["info"]["age"])






# 18 - question 


# from collections import defaultdict

# numbers = defaultdict(lambda: "Unknown")

# print(numbers["apple"])






# 19 -question 

# student = {
#     "Adam": 20,
#     "Ali": 21,
#     "John": 20,
#     "Bob": 22
# }

# print(len(set(student.values())))







# 20 -questions

# student = {
#     "c": 3,
#     "a": 1,
#     "b": 2
# }

# result = dict(sorted(student.items()))

# print(result)





# 21- question 


# student = {
#     "Adam": 30,
#     "Ali": 20,
#     "John": 25
# }

# result = dict(sorted(student.items(), key=lambda item: item[1]))

# print(result)






# 22 - question 



# student = {
#     "Adam": 30,
#     "Ali": 18,
#     "John": 25,
#     "Bob": 15
# }

# result = {}

# for key, value in student.items():
#     if value > 20:
#         result[key] = value

# print(result)





# 23-question 


# student = {
#     "Adam": 30,
#     "Ali": 18,
#     "John": 25,
#     "Bob": 15
# }

# result = {}

# for key, value in student.items():
#     if value > 20:
#         result[key] = value

# print(result)






# 24- question 


# data = (
#     ("name", "Adam"),
#     ("age", 20),
#     ("city", "Tashkent")
# )

# result = dict(data)

# print(result)








# 25 - question 

# student = {
#     "name": "Adam",
#     "age": 20,
#     "city": "Tashkent"
# }

# first_pair = next(iter(student.items()))

# print(first_pair)