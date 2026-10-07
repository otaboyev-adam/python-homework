import csv


def read_grades(filename):
    students = []
    with open(filename, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["Grade"] = float(row["Grade"])
            students.append(row)
    return students


def calculate_averages(students):
    subjects = {}
    for student in students:
        subject = student["Subject"]
        if subject not in subjects:
            subjects[subject] = []
        subjects[subject].append(student["Grade"])

    averages = {}
    for subject, grades in subjects.items():
        average = round(sum(grades) / len(grades), 2)
        if average == int(average):
            average = int(average)
        averages[subject] = average
    return averages


def write_averages(averages, filename):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Subject", "Average Grade"])
        for subject, average in averages.items():
            writer.writerow([subject, average])



try:
    students = read_grades("grades.csv")
except FileNotFoundError:
    print("grades.csv was not found. Run the program from the student_grades folder.")
else:
    averages = calculate_averages(students)

    print("Average grades:")
    for subject, average in averages.items():
        print(f"{subject}: {average}")

    write_averages(averages, "average_grades.csv")
    print("Saved to average_grades.csv")
