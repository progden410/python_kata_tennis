PLAYER_1 = "Player 1"
PLAYER_2 = "Player 2"


class TennisGame:
    score_map: list[str] = ["love", "15", "30", "40"]
    p1score: int = 0
    p2score: int = 0

    def score(self, player):
        if player == PLAYER_1:
            self.p1score += 1
        if player == PLAYER_2:
            self.p2score += 1

    def score_string(self) -> str:


        if self.p1score == self.p2score and self.p1score <= 3:
            return "%s-all" % self.score_map[self.p1score]
        elif self.p1score == self.p2score:
            return "Deuce"

        if self.p1score <= 3 and self.p2score <= 3:
            return "%s-%s" % (self.score_map[self.p1score], self.score_map[self.p2score])

        if self.p1score > 3 or self.p2score > 3:
            if abs(self.p1score - self.p2score) < 2:
                return "%s Advance." % self.get_winner()
            else:
                return "%s win." % self.get_winner()

    def get_winner(self):
        return PLAYER_1 if self.p1score > self.p2score \
            else PLAYER_2
