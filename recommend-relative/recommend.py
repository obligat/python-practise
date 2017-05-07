import computeNearestNeighbor


def recommend(username, users):
    nearest = computeNearestNeighbor.computeNearestNeighbor(username, users)[0][1]
    recommendations = []
    neighborRatings = users[nearest]
    userRatings = users[username]
    for artist in neighborRatings:
        if not artist in userRatings:
            recommendations.append((artist, neighborRatings[artist]))
    return sorted(recommendations, key=lambda artistTuple: artistTuple[1], reverse=True)


print recommend("Dan", computeNearestNeighbor.manhattan.users)
