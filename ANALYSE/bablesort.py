def Anonyme(an):

    for i in range(len(an)):
        for j in range(len(an) - i - 1):

            if an[j] > an[j+1]:
                p = an[j+1]
                an[j+1] = an[j]
                an[j] = p

    return an
    with open("numbers.txt", "r") as f:
    contenu = f.read()
    an = list(map(int, contenu.split()))

# ترتيب اللائحة
resultat = Anonyme(an)

print(resultat)

