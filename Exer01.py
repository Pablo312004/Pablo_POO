class Animal:
    def emitir_som(self):
        pass
    
    def comer(self):
        pass
    
    def atividade(self):
        pass
    
    def __str__(self):
        return "Um animal genérico"


class Leão(Animal):
    def emitir_som(self):
        return "O leão ruge poderosamente!"
    
    def comer(self):
        return "O leão devora sua presa com voracidade."
    
    def atividade(self):
        return "O leão patrulha seu território com majestade."


class Pinguim(Animal):
    def emitir_som(self):
        return "O pinguim emite um som parecido com um trompete."
    
    def comer(self):
        return "O pinguim saboreia peixes frescos capturados na água gelada."
    
    def atividade(self):
        return "O pinguim desliza pelo gelo em busca de seu parceiro para dançar."


class Macaco(Animal):
    def emitir_som(self):
        return "O macaco grita e vocaliza com entusiasmo."
    
    def comer(self):
        return "O macaco mastiga frutas maduras com gosto."
    
    def atividade(self):
        return "O macaco pula de galho em galho, explorando seu habitat."


class Tartaruga(Animal):
    def emitir_som(self):
        return "A tartaruga emite um som suave, quase imperceptível."
    
    def comer(self):
        return "A tartaruga mastiga lentamente folhas verdes e tenras."
    
    def atividade(self):
        return "A tartaruga se move com calma e tranquilidade pelo solo, explorando seu ambiente."    


# Teste das classes
animais = [Leão(), Pinguim(), Macaco(), Tartaruga()]

for animal in animais:
    print(animal)
    print("Som:", animal.emitir_som())
    print("Comer:", animal.comer())
    print("Atividade:", animal.atividade())
    print()