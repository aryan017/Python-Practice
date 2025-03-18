from power import pheonix,Ice_Pheonix,Golden_Crow

class Character:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
class Male_Characters(Character,pheonix,Ice_Pheonix,Golden_Crow):
    def __init__(self,name,age,nature,gender):
        super().__init__(name,age)
        self.nature=nature
        self.gender=gender
    
    def Villain_or_Hero(self):
        print(self.nature)
    
    def power_Inheritance(self):
        if self.Villain_or_Hero()=='good':
            return f"Have inheritances of {self.bloodline()}"
            
        
class Female_Characters(Character,pheonix,Ice_Pheonix,Golden_Crow):
    def __init__(self,name,age,nature,gender):
        super().__init__(name,age)
        self.nature=nature
        self.gender=gender
        
    def Villain_or_Hero(self):
        return self.nature
        
    