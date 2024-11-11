class PlayerStats:
    
    def __init__(self, player_reader):
        self.players = player_reader.get_players()


    def top_by_nat(self, nationality):
        filtered = []
        for player in self.players:
            if player.nationality == "FIN":
                filtered.append(player)
            
        sorted_players = sorted(filtered, key=lambda p: p.points, reverse = True)
        return sorted_players

