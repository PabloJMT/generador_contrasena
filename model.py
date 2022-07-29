from entity import Password 
from random import randint, choice
from utility import * 

class PasswordModel:
    def __init__(self):
        self.__obj = Password() #llamamos la clase password del archivo entity.py
        self.__password = None #especificamos que password no tiene valor inicial


    def generate(self,length):
        self.__password = [] #en este campo es donde se guarada la contrasena

        for i in range(length):
            char_type = randint(1,100) #En cada ciclo se generá un numero entre 1 y 100, randint regresa un numero entero
 
            if char_type <= LETTER:
                char = choice(self.__obj.letters)
            elif char_type <= PUNCTUATION:
                char = choice(self.__obj.digits)
            else: 
                char = choice(self.__obj.punctuation)
                #El uso de choice es necesario para escoger un elemento de la lista
        
            
            self.__password.append(char)
   
    def get_password(self):
        return ''.join(self.__password) #En esta funcion regresa la contraseña generada