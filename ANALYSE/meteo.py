import requests
import matplotlib.pyplot as plt


villes = ["Azilal", "Casa", "Rabat", "Tanger"]
temperatures = []
humidites = []

for ville in villes:
    url = f"https://wttr.in/{ville}?format=j1"
    response = requests.get(url)
    data = response.json()

    temp = int(data["current_condition"][0]["temp_C"])
    hum = int(data["current_condition"][0]["humidity"])

    temperatures.append(temp)
    humidites.append(hum)


plt.bar(villes, temperatures)
plt.title("Température des villes")
plt.xlabel("Villes")
plt.ylabel("Température °C")
plt.show()

plt.pie(humidites, labels=villes, autopct='%1.1f%%')
plt.title("Répartition de l'humidité")
plt.show()


with open("meteo_report.txt", "w") as f:
    for i in range(len(villes)):
        phrase = f"La ville {villes[i]} a une température de {temperatures[i]}°C et une humidité de {humidites[i]}%.\n"
        f.write(phrase)
plt.figure()

plt.pie(humidites, labels=villes, autopct='%1.1f%%')

plt.title("Répartition de l'humidité")

plt.show()