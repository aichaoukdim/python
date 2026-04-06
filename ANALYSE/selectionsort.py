def selection_sort(an):

    for i in range(len(an)):
        min_index = i

        for j in range(i + 1, len(an)):
            if an[j] < an[min_index]:
                min_index = j

        an[i], an[min_index] = an[min_index], an[i]

    return an

resultat = [64, 25, 12, 22, 11]

print(selection_sort(resultat))