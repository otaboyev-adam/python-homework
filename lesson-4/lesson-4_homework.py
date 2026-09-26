# Question 1


# list1 = [1, 1, 2]
# list2 = [2, 3, 4]
# uncommon_list_1 = []

# for i in list1:
#     if i not in list2:
#         uncommon_list_1.append(i)

# for j in list2:
#     if j not in list1:
#         uncommon_list_1.append(j)

# print(uncommon_list_1)










# 2-Question


# n = int(input("Birorta son kiriting: "))

# for i in range(n):
#     print(i ** 2)







# 3-Question 


# txt = "abcabcadabcdeabcdefabcdefg"
# result = ''

# for i in range(len(txt)):
#     result += txt[i]
#     if (i + 1) % 3 == 0:
#         if txt[i] not in "aeiou" and i != len(txt) - 1:
#             result += "_"

# print(result)








# 4-question 


# import random

# while True:
#     secret = random.randint(1, 100)
#     win = False

#     for attempt in range(10):
#         guess = int(input("Guess the number: "))

#         if guess > secret:
#             print("Too high!")

#         elif guess < secret:
#             print("Too low!")

#         else:
#             print("You guessed it right!")
#             win = True
#             break

#     if win:
#         break

    # again = input("You lost. Want to play again? ")

    # if again in ["Y", "YES", "y", "yes", "ok"]:
    #     continue
#     else:
#         break







# 5-question


# password = input("Enter password: ")

# has_upper = False

# for char in password:
#     if char.isupper():
#         has_upper = True

# if len(password) < 8:
#     print("Password is too short.")

# elif not has_upper:
#     print("Password must contain an uppercase letter.")

# else:
#     print("Password is strong.")








# 6-question


# for num in range(2, 101):

#     is_prime = True

#     for i in range(2, num):

#         if num % i == 0:
#             is_prime = False
#             break

#     if is_prime:
#         print(num)






# bonus question


# import random


# while True:
#     computer = 0
#     human = 0

#     while computer < 5 and human < 5:
#         choice_c = random.choice(["rock", "paper", "scissors"])
#         choice_h = input("rock & paper (rock/paper/scissors): ").lower()

#         if choice_c == choice_h:
#             print("Draw!")

#         elif (
#             choice_h == "rock" and choice_c == "scissors"
#             or choice_h == "paper" and choice_c == "rock"
#             or choice_h == "scissors" and choice_c == "paper"
#         ):
#             print("You Won!")
#             human += 1
        
#         else:
#             print("Computer Won!")
#             computer += 1

#         print(f"scores:\nComputer: {computer},\nYou: {human}")

    
#     again = input("You lost. Want to play again? ")

#     if again in ["Y", "YES", "y", "yes", "ok"]:
#         continue
    
#     else:
#         print("Game Over!")
#         break