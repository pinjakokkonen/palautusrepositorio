LOVE = 0
FIFTEEN = 1
THIRTY = 2
FORTY = 3
GAME_POINT = 4
ADVANTAGE1 = 1
ADVANTAGE2 = -1
WIN = 2

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1

    def deuce(self):
        if self.player1_score == LOVE:
            return "Love-All"
        elif self.player1_score == FIFTEEN:
            return "Fifteen-All"
        elif self.player1_score == THIRTY:
            return "Thirty-All"
        else:
            return "Deuce"

    def game_result(self):
        result = self.player1_score - self.player2_score

        if result == ADVANTAGE1:
            return "Advantage player1"
        elif result == ADVANTAGE2:
            return "Advantage player2"
        elif result >= WIN:
            return "Win for player1"
        else:
            return "Win for player2"

    def score_currently(self):
        score = ""
        temp_score = 0
        for i in range(FIFTEEN, FORTY):
            if i == FIFTEEN:
                temp_score = self.player1_score
            else:
                score += "-"
                temp_score = self.player2_score

            if temp_score == LOVE:
                score += "Love"
            elif temp_score == FIFTEEN:
                score += "Fifteen"
            elif temp_score == THIRTY:
                score += "Thirty"
            elif temp_score == FORTY:
                score += "Forty"
        return score

    def get_score(self):
        if self.player1_score == self.player2_score:
            return self.deuce()
        elif self.player1_score >= GAME_POINT or self.player2_score >= GAME_POINT:
            return self.game_result()
        else:
            return self.score_currently()