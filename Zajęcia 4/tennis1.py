class TennisGame1:
    SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_points += 1
        else:
            self.player2_points += 1

    def score(self):
        if self.player1_points == self.player2_points:
            return self.draw_score()
        if self.player1_points >= 4 or self.player2_points >= 4:
            return self.endgame_score()
        return self.normal_score()

    def draw_score(self):
        if self.player1_points >= 3:
            return "Deuce"
        return f"{self.SCORE_NAMES[self.player1_points]}-All"

    def endgame_score(self):
        difference = self.player1_points - self.player2_points
        if difference == 1:
            return f"Advantage {self.player1_name}"
        if difference == -1:
            return f"Advantage {self.player2_name}"
        if difference >= 2:
            return f"Win for {self.player1_name}"
        return f"Win for {self.player2_name}"

    def normal_score(self):
        return f"{self.SCORE_NAMES[self.player1_points]}-{self.SCORE_NAMES[self.player2_points]}"