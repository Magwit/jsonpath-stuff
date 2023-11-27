import json
from jsonpath_ng.ext import parse


with open("./movies.json") as movies_json:
    movies = json.load(movies_json)

jp_expression = parse("$.movies[?(@.year < 1990)].title")

for match in jp_expression.find(movies):
    print(match.value)
