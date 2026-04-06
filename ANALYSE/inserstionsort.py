def insertion_sort(an):
    for i in range(1, len(an)):
        key = an[i]
        j = i - 1

        while j >= 0 and an[j] > key:
            an[j + 1] = an[j]
            j = j - 1

        an[j + 1] = key

    return an

resultat = [64, 25, 12, 22, 11]

print(insertion_sort(resultat))