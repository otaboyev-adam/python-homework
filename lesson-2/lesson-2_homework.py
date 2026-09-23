
#                                         Number Data Type Questions:

# 1-question

# in_num = float(input("Iltimos son kiritng: "))
# rounded = round(in_num, 2)
# print(f'Siz kiritgan sonning yaxlitlangan qiymati: {rounded}')



# 2-question

# order_by = input("3 ta raqam kiriting: ").split(" ")
# print(f"Siz kiritgan raqamlarning eng kattasi {max(order_by)} va eng kichigi {min(order_by)}")



# 3-question

# km = float(input("Iltimos masofani km da kiriting: "))
# print(f"Siz kiritgan masofa {km} km, bu esa {km * 1000} metrga va {km * 100000} sm ga teng")



# 4-question

# devision = list(map(float, input("Iltimos ikkita son kiriting: ").split(" ")))
# print(f"Siz kiritgan sonlarning bo'linmasining butun qismi {devision[0] // devision[1]} va qoldiq {devision[0] % devision[1]} ga teng")



# 5-question

# tempe = float(input("Iltimos haroratni Celsiy da kiriting: "))
# print(f"Siz kiritgan harorat {tempe} Celsiy, bu esa {tempe * 9/5 + 32} Farengeytga teng")



# 6-question

# longnum = int(input("Iltimos uzun son kiriting: "))
# print(f"Siz kiritgan sonning oxirgi raqami {str(longnum)[-1]} ga teng")



# 7-question

# even_or_odd = int(input("Iltimos son kiriting: "))
# if even_or_odd % 2 == 0:
#     print(f"Siz kiritgan son {even_or_odd} juft son")
# else:
#     print(f"Siz kiritgan son {even_or_odd} toq son")








#                                         String Questions:



# 1-question

# name = input("Iltimos ismingizni kiriting: ").strip().title()
# year_of_birth = int(input("Iltimos tug'ilgan yilingizni kiriting: "))
# print(f"Sizning yoshingiz {2026 - year_of_birth} da")



# 2-question

# txt = 'LMaasleitbtui'
# print(f"Birinchi so'z: {txt[0::2]} \nIkkinchi so'z: {txt[1::2]}")



# 3-question

# word = input("Iltimos so'z kiriting: ").strip().lower()
# print(f"Siz kiritgan so'z hajmi {len(word)}, va uppercase: {word.upper()}, lowercase: {word.lower()}")



# 4-question

# word_2 = input("Iltimos so'z kiriting: ").strip().lower()
# if word_2 == word_2[::-1]:
#     print(f"Siz kiritgan so'z {word_2} palindrom so'z")
# else:
#     print(f"Siz kiritgan so'z {word_2} palindrom so'z emas")



# 5-question

# text = input("Matn kiriting: ")

# vowels = "aeiou"
# vowel_count = 0
# consonant_count = 0

# for i in text.lower():
#     if i in vowels:
#         vowel_count += 1
#     elif i.isalpha():
#         consonant_count += 1

# print("Vowels:", vowel_count)
# print("Consonants:", consonant_count)



# 6-question

# text = input("Matn kiriting: ")
# word_1 = input("So'z kiritng: ")


# if word_1 in text:
#     print(f"Siz kiritgan so'z matnda mavjud")
# else:
#     print(f"Siz kiritgan so'z matnda mavjud emas")



# 7-question

# sentence = input("Matn kiriting: ")
# replace_word = input("O'zgartirmoqchi bo'lgan so'zni kiriting: ")
# replace_with = input("Qaysi so'z bilan o'zgartirmoqchisiz: ")

# result_sentence = sentence.replace(replace_word, replace_with)
# print(f"O'zgartirilgan matn: {result_sentence}")



# 8-question

# text_0 = input("Matn kiriting: ").strip()
# print(f"Siz kiritgan stringning birinchi harfi: {text_0[0]}, oxirgi harfi: {text_0[-1]}")



# 9-question

# text_1 = input("Matn kiriting: ").strip()
# print(f"Siz kiritgan matn teskarisiga {text_1[::-1]} bo'ladi!")



# 10-question

# text_2 = input("Matn kiriting: ").strip().split(" ")
# print(f"Siz kiritgan matn {len(text_2)} ta so'zdan iborat")



# 11-question

# text_3 = input("Matn kiriting: ").strip()
# digits = []

# for i in text_3:
#     if i.isdigit():
#         digits.append(i)
#     else:
#         continue

# if bool(digits):
#     print(f"Siz kiritgan matnda raqamlar mavjud: {digits}")
# else:
#     print("Siz kiritgan matnda raqamlar mavjud emas")



# 12-question

# text_4 = input("Matn kiriting: ").strip().split(" ")
# result_text = " "
# for i in text_4:
#     result_text += i + ", "

# print(result_text)



# 13-question

# text_5 = input("Matn kiriting: ").strip()
# print(text_5.replace(" ", ""))



# 14-question

# a = input("Birinchi matnni kiriting: ").strip()
# b = input("Ikkinchi matnni kiriting: ").strip()

# if a == b:
#     print("Siz kiritgan matnlar bir xil")
# else:
#     print("Siz kiritgan matnlar bir xil emas")



# 15-question

# text_6 = input("Matn kiriting: ").strip()
# acronym = ""

# for i in text_6.split():
#     acronym += i[0].upper()

# print(f"Siz kiritgan matnning qisqartmasi: {acronym}")



# 16-question

# text_7 = input("Matn kiriting: ").strip()
# character = input("Qaysi harfni o'chirishni xohlaysiz: ").lower()

# print(f"rezultat matn: {text_7.lower().replace(character, '')}")



# 17-question

# text_8 = input("Matn kiriting: ").strip()
# vovels = "aeiou"

# for i in text_8:
#     if i in vovels:
#         text_8 = text_8.replace(i, "*")

# print(f"Natija: {text_8}")



# 18-question

# text_9 = input("matin kiriting: ").strip().split(" ")
# first_word = text_9[0]
# last_word = text_9[-1]

# print(f"Siz kiritgan matnning birinchi so'zi: {first_word}, oxirgi so'zi: {last_word}")
















#                                             Boolean Data Type Questions:



# 1-question

# username = input("Username: ").strip()
# password = input("Password: ").strip()

# if username and password:
#     print("Both are not empty")
# else:
#     print("Username or password is empty")



# 2-question

# num_0 = int(input("Iltimos son kiriting: "))
# num_1 = int(input("Iltimos son kiriting: "))

# if num_0 == num_1:
#     print("Siz kiritgan sonlar teng")
# else:
#     print("Siz kiritgan sonlar teng emas")



# 3-question

# num_2 = int(input("Iltimos son kiriting: "))

# if num_2 > 0 and num_2 % 2 == 0:
#     print("Siz kiritgan son musbat va juft son")
# else:
#     print("Siz kiritgan son musbat va juft son emas")



# 4-question

# num_3 = int(input("Iltimos son kiriting: "))
# num_4 = int(input("Iltimos son kiriting: "))
# num_5 = int(input("Iltimos son kiriting: "))

# if num_3 != num_4 and num_3 != num_5 and num_4 != num_5:
#     print("Siz kiritgan sonlar bir-biriga teng emas")
# else:
#     print("Siz kiritgan sonlar bir-biriga teng")



# 5-question

# text_10 = input("Matn kiriting: ").strip()
# text_11 = input("Matn kiriting: ").strip()

# if len(text_10) == len(text_11):
#     print("Siz kiritgan matnlar bir xil uzunlikda")
# else:
#     print("Siz kiritgan matnlar bir xil uzunlikda emas")




# 6-question



# num_6 = int(input("Iltimos son kiriting: "))

# if num_6 % 3 == 0 or num_6 % 5 == 0:
#     print("Siz kiritgan son 3 yoki 5 ga bo'linadi")
# else:
#     print("Siz kiritgan son 3 yoki 5 ga bo'linmaydi")



# 7-question



# num_7 = float(input("Enter first number: "))
# num_8 = float(input("Enter second number: "))

# if num_7 + num_8 > 50:
#     print("The sum is greater than 50")
# else:
#     print("The sum is not greater than 50")



# num = float(input("Enter a number: "))

# if 10 <= num <= 20:
#     print("The number is between 10 and 20")
# else:
#     print("The number is not between 10 and 20")