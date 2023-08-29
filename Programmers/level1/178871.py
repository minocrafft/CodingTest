"""
달리기 경주

link: https://programmers.co.kr/learn/courses/30/lessons/178871
"""


def solution(players: list, callings: list):
    player_dict = {player: i for i, player in enumerate(players)}

    for player in callings:
        rank = player_dict[player]
        front = players[rank - 1]

        player_dict[player] -= 1
        player_dict[front] += 1

        players[rank - 1 : rank + 1] = reversed(players[rank - 1 : rank + 1])

    return players


players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]

print(solution(players, callings))
