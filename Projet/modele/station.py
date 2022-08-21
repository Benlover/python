class Station:
    nomStation: str
    capacite_Gazoline: int
    capacite_diesel:int

    def __init__(self, nomStation: str = '', capacite_Gazoline: int = 0,capacite_diesel: int = 0):
        self.nomStation = nomStation
        self.capacite_Gazoline = capacite_Gazoline
        self.capacite_diesel = capacite_diesel