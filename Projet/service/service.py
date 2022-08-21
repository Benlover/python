#IMPORTATION DES MODULES
from email.policy import default
from operator import le
from typing import ClassVar
from modele.station import Station
from modele.commande import Commande
import logging

class Petrole:
    s_lalue = dict
    s_tabarre = {}
    s_clercine = {}
    s_petionville = {}
    stationGenerale: list= []
    nomStation: str = ''
    capacite_Gazoline: int = 0
    capacite_diesel: int =0 
    station : Station
    diesel: ClassVar[int]
    gazoline: ClassVar[int]
    def __init__(self):
          self.s_lalue = dict({
              'nomStation': self.nomStation,
              'capacite_Gazoline':self.capacite_Gazoline,
              'capacite_diesel': self.capacite_diesel
          })
          self.s_clercine= dict({
              'nomStation': self.nomStation,
              'capacite_Gazoline':self.capacite_Gazoline,
              'capacite_diesel': self.capacite_diesel
          })
          self.s_tabarre = dict({
            'nomStation': self.nomStation,
              'capacite_Gazoline':self.capacite_Gazoline,
              'capacite_diesel': self.capacite_diesel
          }) 
          self.s_petionville = dict({
               'nomStation': self.nomStation,
              'capacite_Gazoline':self.capacite_Gazoline,
              'capacite_diesel': self.capacite_diesel
          })
          self.stationGenerale = []
          station : Station()
     

    def enregistrerStation(self):
        self.nomStation = Petrole.choixStation(message =' Choisir une station svp !!')
        try:
            self.capacite_Gazoline:int = int(input('Saisir la capacité de gazoline !!:'))
        except ValueError as e:
            logging.error(e)      
        try:
             self.capacite_diesel:int = int(input('Saisir la capacité de diesel !! :'))
        except ValueError as e:
            logging.error(e) 

#Verifier si cette station n\'existe pas deja  
#           
        # for listeS in self.stationGenerale:
        #     if listeS.nomStation == self.nomStation:
        #         self.stationGenerale.remove(listeS)
        #         break
        match self.nomStation:
            case 'lalue':
                self.s_lalue.update({
                'nomStation': self.nomStation,
                'capacite_Gazoline':self.capacite_Gazoline,
                'capacite_diesel': self.capacite_diesel
                })
                
                self.stationGenerale.append(self.s_lalue)
            case 'tabarre':
                self.s_tabarre.update({
                'nomStation': self.nomStation,
                'capacite_Gazoline':self.capacite_Gazoline,
                'capacite_diesel': self.capacite_diesel
                })
                self.stationGenerale.append(self.s_tabarre)   
            case 'clercine':
                self.s_clercine.update({
                'nomStation': self.nomStation,
                'capacite_Gazoline':self.capacite_Gazoline,
                'capacite_diesel': self.capacite_diesel
                })
                self.stationGenerale.append(self.s_clercine)  
            case 'Petion-ville':
                self.s_petionville.update({
                'nomStation': self.nomStation,
                'capacite_Gazoline':self.capacite_Gazoline,
                'capacite_diesel': self.capacite_diesel
                })
                self.stationGenerale.append(self.s_petionville)

        print('Save avec succes') 

       

    def afficherStation(self):
        stat:str = Petrole.choixStation(message='Choisir une station a aficher svp' )

        match stat:

            case 'lalue':
                Petrole.afficher(self.s_lalue)
            case 'tabarre':
                Petrole.afficher(self.s_tabarre)
            case 'clercine':
                Petrole.afficher(self.s_clercine)
            case 'Petion-ville':
                Petrole.afficher(self.s_petionville)
            case default:
                print('Mauvais choix')    

    def afficherStations(self):
        if len(self.stationGenerale)>0:
          for staG in self.stationGenerale:
            print(staG) 
        else:
            print('List empty')    
    @staticmethod         
    def afficher(dicGenerale:dict):
      
             print('***************************************************')
             print(f" \n Station :{dicGenerale.get('nomStation')}"
                   f"\n capacite de stackage de gazoline {dicGenerale.get('capacite_Gazoline')} "
                   f"\n capacité de stockage gazoline :{dicGenerale.get('capacite_diesel')}"
             )  
             print('*************************************************************')


    def ModifierCapacite(self):
        self.nomStation = Petrole.choixStation(message='Choisir une station svp')
        match self.nomStation:
            case 'lalue':
                if len(self.s_lalue)>0:
                    Petrole.gazoline= self.s_lalue.get('capacite_Gazoline')
                    Petrole.diesel = self.s_lalue.get('capacite_diesel')

                    #Appeller la methode Saisir donnees
                    Petrole.donnes()
                    self.s_lalue.update({
                    'nomStation': self.nomStation,
                    'capacite_Gazoline':Petrole.gazoline,
                    'capacite_diesel':Petrole.diesel
                     })
                    self.s_lalue.update(self.s_lalue)
                else:
                    print('')
                       
            case 'tabarre':
                if len(self.s_tabarre)>0:
                    Petrole.gazoline= self.s_lalue.get('capacite_Gazoline')
                    Petrole.diesel = self.s_lalue.get('capacite_diesel')

                        #Appeller la methode Saisir donnees
                    Petrole.donnes()
                    self.s_lalue.update({
                        'nomStation': self.nomStation,
                        'capacite_Gazoline':Petrole.gazoline,
                        'capacite_diesel': Petrole.diesel
                        })
                    self.s_lalue.update(self.s_lalue)
            case 'clercine':
                if len(self.s_clercine)>0:
                    Petrole.gazoline= self.s_lalue.get('capacite_Gazoline')
                    Petrole.diesel = self.s_lalue.get('capacite_diesel')
                     #Appeller la methode Saisir donnees
                    Petrole.donnes()
                    self.s_lalue.update({
                        'nomStation': self.nomStation,
                        'capacite_Gazoline':Petrole.gazoline,
                        'capacite_diesel': Petrole.diesel
                        })
                    self.s_lalue.update(self.s_lalue)

            case 'Petion-ville':
                if len(self.s_petionville)>0:
                    Petrole.gazoline= self.s_lalue.get('capacite_Gazoline')
                    Petrole.diesel = self.s_lalue.get('capacite_diesel')
                     #Appeller la methode Saisir donnees
                    Petrole.donnes()
                    self.s_lalue.update({
                        'nomStation': self.nomStation,
                        'capacite_Gazoline':Petrole.gazoline,
                        'capacite_diesel': Petrole.diesel
                        })
                    self.s_lalue.update(self.s_lalue)
        print('Modifier avec Succes')        
            #   case default:
            #     print('Mauvais Choix ????')

    @staticmethod
    def choose_essence()->str:
        return input('\n a-GAZOLINE'
                     '\n b-DIESEL'
                     '\n c-LES DEUX'
                     '\n d-PRESSER POUR QUITTER'
                     '\n =====>')
           
    

    @staticmethod
    def choixStation( message: str)->str:
        while True:
            station:str = input(f'******{message}********\n'
                                 '\n a- lalue'
                                '\n b-tabarre'
                                '\n c-clercine'
                                '\n d-Petion-ville'
                                '\n ===>:')
            match station.lower():
                        case 'a':
                            return 'lalue'
                        case 'b':
                             return 'tabarre'
                        case 'c':
                            return 'clercine'
                        case 'Petion-ville':
                            return ''
                        case default:
                           print('Mauvais Choix')   
    @staticmethod                       
    def donnes():
        while True:
            Type_essence:str = Petrole.choose_essence()
            match Type_essence:
                case 'a':
                    Petrole.gazoline= int(input('Saisir la nouvelle capacite de gazoline svp !!!'))
                case 'b':
                    Petrole.diesel = int(input('Saisir la nouvelle capacite de diesel svp !!!'))
                case 'c':
                   Petrole.gazoline = int(input('Saisir la nouvelle capacite de gazoline svp !!!'))
                   Petrole.diesel = int(input('Saisir la nouvelle capacite de diesel svp !!!'))
                
                case default:
                    break

if __name__ == '__main__':    

    Petrole = Petrole()
    Petrole.enregistrerStation()
    Petrole.afficherStations()

