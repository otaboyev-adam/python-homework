import csv
import json
import sqlite3

import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

from selenium.webdriver.common.by import By

#     Task 1 Weather

html = """<!DOCTYPE html>
<html>
<head>
    <title>Weather Forecast</title>
</head>
<body>
    <h4>5-Day Weather Forecast</h4>
    <table>
        <thead>
            <tr>
                <th>Day</th>
                <th>Temperature</th>
                <th>Condition</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Monday</td>
                <td>25°C</td>
                <td>Sunny</td>
            </tr>
            <tr>
                <td>Tuesday</td>
                <td>22°C</td>
                <td>Cloudy</td>
            </tr>
            <tr>
                <td>Wednesday</td>
                <td>18°C</td>
                <td>Rainy</td>
            </tr>
            <tr>
                <td>Thursday</td>
                <td>20°C</td>
                <td>Partly Cloudy</td>
            </tr>
            <tr>
                <td>Friday</td>
                <td>30°C</td>
                <td>Sunny</td>
            </tr>
        </tbody>
    </table>
</body>
</html>"""

with open("weather.html", "w", encoding="utf-8") as file:
    file.write(html)

with open("weather.html", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

rows = soup.find("tbody").find_all("tr")

days = []
temps = []
conditions = []



for row in rows:
    cells = row.find_all("td")
    days.append(cells[0].text.strip())
    temps.append(int(cells[1].text.replace("°C", "").strip()))
    conditions.append(cells[2].text.strip())



print("5-Day Weather Forecast")
for i in range(len(days)):
    print(days[i], "-", temps[i], "°C -", conditions[i])



highest = max(temps)
print("\nHighest temperature:", highest, "°C")
for i in range(len(days)):
    if temps[i] == highest:
        print("Day with the highest temperature:", days[i])





print("Sunny days:")
for i in range(len(days)):
    if conditions[i] == "Sunny":
        print("-", days[i])

average = sum(temps) / len(temps)
print("Average temperature:", round(average, 1), "°C")



























# Task 2 Job Scraper


conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()






cursor.execute("""CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    company TEXT,
    location TEXT,
    description TEXT,
    link TEXT,
    UNIQUE(title, company, location)
)""")




response = requests.get("https://realpython.github.io/fake-jobs/")
soup = BeautifulSoup(response.text, "html.parser")
cards = soup.find_all("div", class_="card-content")

new_jobs = 0
updated_jobs = 0

print("\nScraping jobs, please wait...")
for card in cards:
    title = card.find("h2", class_="title").text.strip()
    company = card.find("h3", class_="company").text.strip()
    location = card.find("p", class_="location").text.strip()
    link = card.find_all("a")[1]["href"]

    detail_response = requests.get(link)
    detail_soup = BeautifulSoup(detail_response.text, "html.parser")
    description = detail_soup.find("h2").find_next("p").text.strip()

    cursor.execute("SELECT description, link FROM jobs WHERE title = ? AND company = ? AND location = ?",
                   (title, company, location))
    old_job = cursor.fetchone()



    if old_job is None:
        cursor.execute("INSERT INTO jobs (title, company, location, description, link) VALUES (?, ?, ?, ?, ?)",
                       (title, company, location, description, link))
        new_jobs += 1
    elif old_job[0] != description or old_job[1] != link:
        cursor.execute("UPDATE jobs SET description = ?, link = ? WHERE title = ? AND company = ? AND location = ?",
                       (description, link, title, company, location))
        updated_jobs += 1

conn.commit()
print("Jobs found on the page:", len(cards))
print("New jobs added:", new_jobs)
print("Jobs updated:", updated_jobs)


def export_jobs(filter_by, value, filename):
    if filter_by == "location":
        cursor.execute("SELECT title, company, location, description, link FROM jobs WHERE location LIKE ?",
                       ("%" + value + "%",))
    else:
        cursor.execute("SELECT title, company, location, description, link FROM jobs WHERE company LIKE ?",
                       ("%" + value + "%",))
    result = cursor.fetchall()

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Company", "Location", "Description", "Link"])
        writer.writerows(result)

    return result






filter_by = input("\nFilter jobs by location or company: ").strip().lower()

if filter_by == "location" or filter_by == "company":
    value = input("Enter the " + filter_by + " to search for: ").strip()
    result = export_jobs(filter_by, value, "filtered_jobs.csv")
    print("Found", len(result), "job(s):")
    for job in result:
        print("-", job[0], "|", job[1], "|", job[2])
    print("Saved to filtered_jobs.csv")
else:
    print("Please type either location or company.")




conn.close()



















# Task 3 Laptops

driver = webdriver.Chrome()
driver.get("https://www.demoblaze.com/")
time.sleep(3)

driver.find_element(By.LINK_TEXT, "Laptops").click()
time.sleep(3)

laptops = []
names = []

for page in range(2):
    soup = BeautifulSoup(driver.page_source, "html.parser")
    cards = soup.find_all("div", class_="card")

    for card in cards:
        name = card.find("h4", class_="card-title").text.strip()
        price = card.find("h5").text.strip()
        description = card.find("p", class_="card-text").text.strip()

        if name not in names:
            names.append(name)
            laptops.append({"name": name, "price": price, "description": description})

    if page == 0:
        try:
            driver.find_element(By.ID, "next2").click()
            time.sleep(3)
        except Exception:
            print("The Next button could not be clicked.")
            break

driver.quit()

with open("laptops.json", "w", encoding="utf-8") as file:
    json.dump(laptops, file, indent=4)

print("\nSaved", len(laptops), "laptops to laptops.json")
for laptop in laptops:
    print(laptop["name"], "-", laptop["price"])
