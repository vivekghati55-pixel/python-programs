class batsman:
    def set_batsman(self, total_runs, total_sixes, matches):
        self.total_runs = total_runs
        self.total_sixes = total_sixes
        self.matches = matches
    def display_batsman(self):
        print("Cricketer Details:")
        print("Total Runs:", self.total_runs)
        print("Total Sixes:", self.total_sixes)
        print("Matches Played:", self.matches)     

class bowler:
    def set_bowler(self, total_wickets, total_maidens):
        self.total_wickets = total_wickets
        self.total_maidens = total_maidens
    def display_bowler(self):
        print("Total Wickets:", self.total_wickets)
        print("Total Maidens:", self.total_maidens)

class allrounder(batsman, bowler):
    def set_allrounder(self,no_of_catches):
        self.no_of_catches = no_of_catches
    def display_allrounder(self):
        print("Number of Catches:", self.no_of_catches)


cricket_player = allrounder()
cricket_player.set_batsman(5000, 200, 100)
cricket_player.set_bowler(150, 20)
cricket_player.set_allrounder(50)
cricket_player.display_batsman()
cricket_player.display_bowler()
cricket_player.display_allrounder()