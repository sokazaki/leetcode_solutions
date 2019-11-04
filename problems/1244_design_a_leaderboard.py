# O(1) init, addScore, reset / O(N) top Time Complecity Solution with Hashmap

import collections

class Leaderboard:

    def __init__(self):
        self.leaderboard = collections.Counter()

    def addScore(self, playerId, score):
        self.leaderboard[playerId] += score

    def top(self, K):
        return sum(val for _, val in self.leaderboard.most_common(K))

    def reset(self, playerId):
        self.leaderboard[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId, score)
# param_2 = obj.top(K)
# obj.reset(playerId)
