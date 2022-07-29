from model import PasswordModel
from utility import * 

class PasswordController:
    def __init__(self):
        self.__obj = PasswordModel()

    def process_password(self, strength):
        if strength == EASY:
            self.__obj.generate(LENGTH_S)
            return self.__obj.get_password()

#En esta parte del programa se llama a la contraseña creada en el archivo model.py y se crea una funcion 
#de procesamiento para la extension 'EASY'

