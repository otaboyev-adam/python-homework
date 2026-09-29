
# 1-question


# def convert_celsius_to_fahrenheit(celsius):
#     return celsius * 9 / 5 + 32


# celsius = float(input("Haroratni Celsiusda kiriting: "))
# fahrenheit = round(convert_celsius_to_fahrenheit(celsius), 2)

# print(f"Siz kiritgan harorat Fahrenheitda {fahrenheit} daraja bo'ladi")



# def convert_fahrenheit_to_celsius(fahrenheit):
#     return  (fahrenheit - 32) * 5 / 9


# fahrenheit = float(input("Haroratni fahrenheit kiriting: "))
# celsius= round(convert_fahrenheit_to_celsius(fahrenheit), 2)

# print(f"Siz kiritgan harorat celsiusda {celsius} daraja bo'ladi")








# 2-question


# def invest(amount, rate, years):
#     for year in range(1, years + 1):
#         amount += amount * rate
#         print(f'Year {year}: ${round(amount)}')


# invest(1000, 0.06, 5)










# 3-question


# def find_factors(number):
#     for factor in range(1, number + 1):
#         if number % factor == 0:
#             print(f"{factor} is a factor of {number}")


# number = int(input("Butun musbat son kiriting: "))

# if number > 0:
#     find_factors(number)
# else:
#     print("Musbat son kiriting.")








# 4 - question 

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]


def enrollment_stats(universities):
    enrollments = []
    tuitions = []

    for university in universities:
        enrollments.append(university[1])
        tuitions.append(university[2])

    return enrollments, tuitions


def mean(values):
    return sum(values) / len(values)


def median(values):
    values = sorted(values)
    middle = len(values) // 2

    if len(values) % 2 == 1:
        return values[middle]
    else:
        return (values[middle - 1] + values[middle]) / 2


enrollments, tuitions = enrollment_stats(universities)

total_students = sum(enrollments)
total_tuition = sum(tuitions)

student_mean = mean(enrollments)
student_median = median(enrollments)

tuition_mean = mean(tuitions)
tuition_median = median(tuitions)


print("*" * 30)
print(f"Total students: {total_students:,}")
print(f"Total tuition: $ {total_tuition:,}")
print()
print(f"Student mean: {student_mean:,.2f}")
print(f"Student median: {student_median:,}")
print()
print(f"Tuition mean: $ {tuition_mean:,.2f}")
print(f"Tuition median: $ {tuition_median:,}")
print("*" * 30)



# 5 - question 


def is_prime(n):
    if n < 2:
        return False

    for divisor in range(2, int(n ** 0.5) + 1):
        if n % divisor == 0:
            return False

    return True