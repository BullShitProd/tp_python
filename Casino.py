from player import Player
from roulette import Roulette


class Casino:

    def __init__(self):
        self.roulette = Roulette()
        self.player = None
        print("=== BIENVENUE SUR LE SUPER CASINO ===")
        self.menuPlayer()

    # Get int for input user
    def getValueUser(self, text):
        while True:
            try:
                x  = int(input(text))
                return x
                break
            except ValueError:
                print("Oops! Ceci n'est pas un nombre. Recommencer")

    # First Menu
    def menuPlayer(self):

        print("- MENU -")
        print("")
        print("1. S'enregistrer")
        print("2. Se deconnecter")

        chose = self.getValueUser("Veuillez entrez la valeur de votre action : ")

        if chose == 1:
            self.playerEnter()
            self.MenuGame()

        elif chose == 2:
            print("Vous quittez le casino")
        else:
            self.menuPlayer()


    #Create User
    def playerEnter(self):
        name = input("Donner votre nom de joueur : ")
        self.player = Player(name)
        print("Bienvenue " + name)

    def playerLeave(self):
        self.player = None

    def playerSold(self):
        print("Votre solde est de : " + str(self.player.sold))

    #Second Menu : Game
    def MenuGame(self):

        print("=== Menu de Jeu ===")
        print("1. Lancer une partie")
        print("2. Voir votre solde")
        print("3. Se déconnecter")

        chose = self.getValueUser("Veuillez entrez la valeur de votre action : ")

        if chose == 1:
            self.playRoulette()
        elif chose == 2:
            self.playerSold()
            self.MenuGame()
        elif chose == 3:
            self.playerLeave()
            self.menuPlayer()
        else:
            self.MenuGame()

    #demande à l'utilisateur combien il veut parier. Vérifie si cela est possible
    def chosePrice(self):
        chosePrice = self.getValueUser("Vous voulez parier combien ?")

        if chosePrice > self.player.sold:
            return self.chosePrice()

        return chosePrice

    # Joue la roulette (demande à l'utilisateur et affiche le résultat
    def playRoulette(self):

        choseNumber = self.getValueUser("Veuillez choisir votre case entre 0 et 49 (compris) :")
        price = self.chosePrice()

        #roulette
        caseRoulette = self.roulette.launch()
        moduloColor = 1
        if caseRoulette["color"] == "black":
            moduloColor = 0

        print("La roulette tourne...")
        print("1...")
        print("2...")
        print("3...")
        print("Le numéro gagnant est le " + str(caseRoulette["number"]) + " de couleur : " + caseRoulette["color"])
        print("")



        #Correspondance chiffre
        if choseNumber == caseRoulette["number"]:
            print("Votre nombre et le meme que celui de la roulette :" + str(choseNumber))
            print("Vous avez donc gagné le gros lot !")
            self.player.addSold(price * 3)
            self.playerSold()
        elif choseNumber%2 == moduloColor:
            print("Votre nombre et de meme couleur que celui de la roulette :" + caseRoulette["color"])
            self.player.addSold(price * 0.5)
        else:
            print("Vous avez perdu")
            self.player.removeSold(price)


        self.retry()

    #Permet de relancer rapidement une partie ou de retourner au menu de jeu
    def retry(self):

        if self.player.sold <= 0:
            print("Vous n'avez plus assez d'argent, vous devez quittez le casino")
            self.playerLeave()
            self.menuPlayer()

        chose = self.getValueUser("Voulez vous recommencer ? (1 = oui, 0 = non) ?")

        if chose == 1:
            self.playRoulette()
        elif chose == 0:
            self.MenuGame()
        else:
            self.retry()










