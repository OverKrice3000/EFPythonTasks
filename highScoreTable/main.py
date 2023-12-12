from typing import List


class HighScoreTable:
    scores: List[int]
    __limit: int

    def __init__(self, limit: int):
        self.__limit = limit
        self.scores = []

    def update(self, score: int):
        self.scores.append(score)
        self.scores.sort(reverse=True)
        if len(self.scores) > self.__limit:
            self.scores.pop(self.__limit)

    def reset(self):
        self.scores = []

if __name__ == '__main__':
    highScoreTable = HighScoreTable(3)
