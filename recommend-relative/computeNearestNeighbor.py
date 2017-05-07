import manhattan
import math


def computeNearestNeighbor(username, users):
    distances = []
    for user in users:
        if user != username:
            distance = manhattan.manhattan(users[user], users[username])
            distances.append((distance, user))
    distances.sort()
    return distances


# print computeNearestNeighbor("Angelica", manhattan.users)
