class Tournament():
    def __init__(self, **kwargs):
        self.title = kwargs['title'] #Jet Duel RB 1x1
        self.team_size = kwargs['team_size'] #1x1
        #self.registration_spots = kwargs['registration_spots'] # 60 | these values are derived from a single value and will need to be handled
        self.registrations = kwargs['registrations'] #10 registrations

        self.battle_mode = kwargs['battle_mode'] #AB, RB, SB
        self.tournament_type = kwargs['tournament_type'] #SE (single elim)
        self.region = kwargs['region'] # EU, SEA, NA
        self.date = kwargs['tournament_date'] #May 1, 24, 17:50 UTC - May 1, 24, 19:50 UTC | why yes, this will have to be handled too <3
        self.detail_id = kwargs['detail_id']
    
    def __str__(self):
        return self.title 

class TournamentDetail(): #through table with references to those other tables? Most likely overkill
    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.maps = kwargs['maps'] #own table
        #self.nations = kwargs['nations'] #own table
        #self.vehicles = kwargs['vehicles'] #own table
        self.nation_vehicles = kwargs['nation_vehicles']
        self.prize_pool = kwargs['prize_pool']

    def __str__(self):
        return f"Tournament Detail:  {self.id}"



    


