
from service.service import Petrole

def menu()->str:
    print('************ GESTION MAX LONDON PETROVIC ************')
    print('1-Station')
    print('2-Commande')
    print('3-approvisionnement')
    print('4-vente')
    print('Presser <<q>> pour quitter')
    print('*******************************************************')
    return str (input('votre choix : '))


if __name__ == '__main__':

    choix: str = ''
    Petrole = Petrole()
    while True:
        choix = menu()
        match choix:
          case '1': 
              while True:
                 print('*********************Station***********')
                 autrechoix: str = input('\n a-Enregistrer une stations'
                                        '\n b-Afficher la liste des station'
                                        '\n c-modifier quantité gallon de gazoline et/ou de Diesel d’une station'
                                        '\n d-quitter'
                                        '\n **************************************************'
                                        '\n ==>')
                 match autrechoix:  
                     case 'a':
                        Petrole.enregistrerStation()
                     case 'b':
                         Petrole.afficherStation()
                     case 'c':
                         Petrole.ModifierCapacite()
                     case 'd':
                         pass
                     case default:
                         print('Mauvais Choix!!!!!')                                 
                
                      
          case '2':
              while True:
                print('*************** COMMANDE ****************')
                autrechoix: str = input('a-Enregistrer une stations'
                                           'b-Afficher la liste des station'
                                           'd-quitter')
                match autrechoix:
                     case 'a':
                         pass
                     case 'b':
                         pass
                     case 'c':
                         break
                     case default:
                         print('Mauvais Choix')         



          case '3':
              print('approvisionnement')
          case '4':
              print('vente')
          case 'q':
              break
          case default:
              print('mauvais choix')
