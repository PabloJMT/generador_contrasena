from string import ascii_letters, digits, punctuation 

class Password:
    def __init__(self):
        self.__letters = ascii_letters
        self.__digits = digits
        self.__punctuation  = punctuation 

    @property
    def letters(self):
        return self.__letters

    @property
    def digits(self):
        return self.__digits

    @property
    def punctuation(self):
        return self.__punctuation

        