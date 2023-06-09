#Напишите класс Dragon (Дракон), экземпляр которого при инициализации принимaет......

class Dragon():
    def __init__(self, height, flammability, color):
        self.height = height
        self.flammability = flammability
        self.color = color
    
    def __str__(self):
        return f"Dragon with height {self.height}, danger {self.flammability} and color {self.color}."
    
    def __repr__(self):
        return f"Dragon({self.height, self.flammability, self.color})"
    
    def change_color(self):
        color = input("Введите  цвет: ")
        self.color = color
        return self
    
    def __call__(self, string):
        print(string * self.flammability)
    
    def __eq__(self, other):
        if self.height == other.height:
            height = True
        else:
            height = False
        if self.flammability == other.flammability:
            flammability = True
        else:
            flammability = False
        if self.color == other.color:
            color = True
        else:
            color = False
        result = [height, flammability, color]
        return result
    
    def __add__(self, other):
         new_color = min(self.color, other.color)
         new_height = (self.height + other.height)/2
         new_flammability = max(self.flammability, other.flammability)
         new_Dragon = Dragon(new_height, new_flammability, new_color)
         return(new_Dragon)
    
    def __sub__(self, num):
         num = int(input("Введите число: "))
         self.height = self.height - self.height // num
         self.flammability = self.flammability + self.flammability % num
         return self

Arman = Dragon(100, 5, "black")
Falkor = Dragon(132, 7, "yollow")
Dagahra = Dragon(284, 13, "green")
Saphira = Dragon(328, 15, "pink")
Ghidorah = Dragon(400, 25, "red")




