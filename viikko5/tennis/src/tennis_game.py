class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):
        if self.m_score1 == self.m_score2:
            return self.draw()
        if self.m_score1 >= 4 or self.m_score2 >= 4:
            return self.score_passes_four()
        return f"{self.regular_score(self.m_score1)}-{self.regular_score(self.m_score2)}"

    def draw(self):
        draw_scores = {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All"}
        return draw_scores.get(self.m_score1, "Deuce")

    def score_passes_four(self):
        minus_result = self.m_score1 - self. m_score2
        if minus_result == 1:
            score = "Advantage player1"
        elif minus_result == -1:
            score = "Advantage player2"
        elif minus_result >= 2:
            score = "Win for player1"
        else:
            score = "Win for player2"
        return score

    def regular_score(self, score):
        temp_score = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"}
        return temp_score.get(score)
