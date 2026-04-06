import requests
import matplotlib.pyplot as plt

url = "https://jsonplaceholder.typicode.com/comments"
response = requests.get(url)
comments = response.json()

counts = {}

for comment in comments:
    post_id = comment["postId"]
    if post_id in counts:
        counts[post_id] += 1
    else:
        counts[post_id] = 1

ids = list(counts.keys())[:10]
values = [counts[i] for i in ids]

plt.bar(ids, values)
plt.xlabel('Utilisateurs')
plt.ylabel('Nombre de commentaires')
plt.title('Nombre de posts par utilisateur')

plt.show()