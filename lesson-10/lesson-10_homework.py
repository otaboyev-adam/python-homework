import random

import requests

WEATHER_KEY = "50235d690969f7d41c13c58e86abcfcc"
MOVIE_KEY = "157d8f72cc19c32a7275767c4c538ceb"


def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": WEATHER_KEY, "units": "metric"}

    try:
        response = requests.get(url, params=params, timeout=10)
    except requests.exceptions.RequestException:
        print("Could not connect to the weather service.")
        return

    if response.status_code == 401:
        print("The API key is wrong or not activated yet.")
        return
    if response.status_code == 404:
        print("City not found.")
        return
    if response.status_code != 200:
        print("Something went wrong. Status code:", response.status_code)
        return

    data = response.json()
    print()
    print("Weather in", data["name"] + ",", data["sys"]["country"])
    print("Description:", data["weather"][0]["description"])
    print("Temperature:", data["main"]["temp"], "C")
    print("Feels like:", data["main"]["feels_like"], "C")
    print("Humidity:", data["main"]["humidity"], "%")
    print("Pressure:", data["main"]["pressure"], "hPa")
    print("Wind speed:", data["wind"]["speed"], "m/s")


def task1():
    get_weather("Tashkent")


def get_genres():
    url = "https://api.themoviedb.org/3/genre/movie/list"
    params = {"api_key": MOVIE_KEY}

    try:
        response = requests.get(url, params=params, timeout=10)
    except requests.exceptions.RequestException:
        print("Could not connect to the movie service.")
        return None

    if response.status_code != 200:
        print("Could not get the genres. Status code:", response.status_code)
        return None

    return {
        genre["name"].lower(): genre["id"]
        for genre in response.json()["genres"]
    }


def recommend_movie(genre_id):
    url = "https://api.themoviedb.org/3/discover/movie"
    params = {
        "api_key": MOVIE_KEY,
        "with_genres": genre_id,
        "sort_by": "popularity.desc",
        "page": random.randint(1, 5),
    }

    try:
        response = requests.get(url, params=params, timeout=10)
    except requests.exceptions.RequestException:
        print("Could not connect to the movie service.")
        return

    if response.status_code != 200:
        print("Could not get movies. Status code:", response.status_code)
        return

    movies = response.json()["results"]
    if not movies:
        print("No movies found for this genre.")
        return

    movie = random.choice(movies)
    print()
    print("We recommend:", movie["title"])
    print("Release date:", movie["release_date"])
    print("Rating:", movie["vote_average"], "/ 10")
    print("Overview:", movie["overview"])


def task2():
    genres = get_genres()
    if genres is None:
        return

    print("\nAvailable genres:", ", ".join(name.title() for name in genres))
    choice = input("Enter a genre: ").strip().lower()
    if choice not in genres:
        print("There is no such genre.")
        return

    recommend_movie(genres[choice])


if __name__ == "__main__":
    task1()
    task2()
