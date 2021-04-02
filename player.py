 class Player:

def __init__(self,nom):
    self.__nom=nom
          
    def get_nom(self): #[Encapsulation] 
        return self.__nom
  
    def __str__(self):
         
        return f"Le nom de joueur est: {self.__nom} "