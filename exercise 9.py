def findWinners(matches):
    players = {}
    winners, loosers = [], []

    for win, loss in matches:
        players[win] = players.get(win, 0)
        players[loss] = players.get(loss, 0) + 1

    for k, v in players.items():
        if v == 0:
            winners.append(k)
        elif v == 1:
            loosers.append(k)

    return [sorted(winners), sorted(loosers)]


# matches = [[2, 3], [1, 3], [5, 4], [6, 4]]
matches = [
    [1, 3],
    [2, 3],
    [3, 6],
    [5, 6],
    [5, 7],
    [4, 5],
    [4, 8],
    [4, 9],
    [10, 4],
    [10, 9],
]
yo = findWinners(matches)
print(yo)
