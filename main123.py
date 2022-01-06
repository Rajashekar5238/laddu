import json
from collections import defaultdict

f = open("E:\\python\\assignments\\imdb_assignment\\imdb_assignment\\imdb_movies.json", 'r')
a = json.load(f)
# print(a)
d = defaultdict(list)
for i in a:
    d[i['director']].append(i['name'])
b = max(d, key=lambda x: len(d[x]))
print("The top director with maximum number of movies -->", b)

d1 = defaultdict(list)
for i in a:
    # print(i)
    for j in i['genre']:
        d1[j.strip(' ')].append(i['99popularity'])
c = max(d1, key=lambda x: sum(d1[x]))
print('The popular genre watched by most of the audience -->', c)


print("The top ten movies, according to imdb score -->")
d2 = defaultdict(list)
for i in a:
    d2[i['name']].append(i["imdb_score"])
e = sorted(d2, key=lambda x: d2[x], reverse=True)
#for i in range:
for i in range(0,len(e)):
    if i>9:
        break
    else:
        print(e[i])
print("The least watched movie based on their imdb score -->", e[-1])

d3 = defaultdict(list)
for i in range(len(a)):
    if i >99:
        break
    else:
        d3[a[i]['director']].append(a[i]['imdb_score'])
g = max(d3, key=lambda x: sum(d3[x]))
print("The best director in the first hundred movies -->",g)
