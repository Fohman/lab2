#  Wzorowane na przykładzie Rona Zacharskiego


from math import sqrt

users = {"Ania": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bonia":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
         "Celina": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
         "Dominika": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Ela": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
         "Fruzia":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Gosia": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Hela": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
        }

def manhattan(rating1, rating2):
    """Oblicz odległość w metryce taksówkowej między dwoma  zbiorami ocen
    :type rating1: object
    :type rating2: object
       danymi w postaci: {'The Strokes': 3.0, 'Slightly Stoopid': 2.5}
       Zwróć -1, gdy zbiory nie mają wspólnych elementów"""


    osoba1 = rating1.keys()
    osoba2 = rating2.keys()
    distance = 0
    porownanie = False

    for klucz in osoba1:
        if klucz in rating2.keys():
            porownanie = True
            distance = distance + abs(rating2[klucz] - rating1[klucz])

    if porownanie:
        return distance
    else:
        return -1

def testManhattan(rating1, rating2, distance):
    if manhattan(rating1, rating2) == distance:
        return True
    else:
        return False
    #manhattan(users['Ania'], users['Dominika'])
    #manhattan(users['Celina'], users['Hela'])
    pass

def computeNearestNeighbor(username, users):
    """dla danego użytkownika username, zwróć ze słownika users nazwę użytkownika o najbliższych preferencjach"""
    nameOfNearestNeighbor = ""
    distances = []
    # TODO: wpisz kod

    for imie2 in users:
        distance = 0
        if username!=imie2:
            distance = manhattan(users[username], users[username])
            distances.append((distance, imie2))

    return sorted(distances)
    return nameOfNearestNeighbor

def recommend(username, users):
    """Zwróć listę rekomendacji dla użytkownika"""
    # znajdź preferencje najbliższego sąsiada



    # zarekomenduj użytkownikowi wykonawcę, którego jeszcze nie ocenił, a zrobił to jego najbliższy sąsiad
    # TODO: wpisz kod

    nearestName = computeNearestNeighbor(username, users)[0][1]
    print username
    print 'Najblizszy sasiad to: %s' %nearestName
    recommendations = []
    ratingOfNearest = users[nearestName]
    print ('jego rekomendacje to: ')
    print (ratingOfNearest)


    userRating = users[username]

    for artist in ratingOfNearest:
        if not artist in userRating:
            recommendations.append((artist, ratingOfNearest[artist]))
    # using the fn sorted for variety - sort is more efficient
    return sorted(recommendations, key=lambda artistTuple: artistTuple[1], reverse = True)

# przykłady

print( recommend('Gosia', users))
