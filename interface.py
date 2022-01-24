class _Animal:

    def correr(self):
        pass
    
    def andar(self):
        pass

class _Cachorro(_Animal):

    def correr(self):
        print('correr')
    
    def andar(self):
        print('andar')

class _Gato(_Animal):

    def correr(self):
        print('correr')

#duck typings
#Animal.__mro__
#Gato.__mro__
#issubclass(Gato, Animal)

#class define como um objeto se comporta
#metaclass define como uma classe se comporta

#type é uma metaclass das classes
#metaclass define como uma classe se comporta
# >>> type(Animal)
# <class 'type'>
# >>> type(object)
# <class 'type'>
# >>> type(str)
# <class 'type'>

#permitindo que se faça coisas extra

#dunder methods

class ParserMeta(type):
    """A Parser metaclass that will be used for parser class creation.
    """
    def __instancecheck__(cls, instance):
        return cls.__subclasscheck__(type(instance))

    def __subclasscheck__(cls, subclass):
        return (hasattr(subclass, 'correr') and 
                callable(subclass.correr) and 
                hasattr(subclass, 'andar') and 
                callable(subclass.andar))

class Animal(metaclass=ParserMeta):
    pass

class Cachorro(Animal):

    def correr(self):
        print('correr')
    
    def andar(self):
        print('andar')

class Gato(Animal):

    def correr(self):
        print('correr')

#virtual base classes
class Galinha:
    def correr(self):
        print('correr')
    
    def andar(self):
        print('andar')

# >>> from interface import Animal, Cachorro, Gato
# >>> issubclass(Gato, Animal)
# False
# False
# >>> issubclass(Cachorro, Animal)
# True
# True
# >>> 


# Formal Interfaces

# sobrescreve __subclasshook__() in place of .__instancecheck__() and .__subclasscheck__(),

import abc

class Carro(metaclass=abc.ABCMeta):
    pass #usar sem metodos antes de mostrar com metodos

    @abc.abstractmethod
    def ligar(self):
        """Load in the data set"""
        raise NotImplementedError

    @abc.abstractmethod
    def parar(self):
        """Load in the data set"""
        raise NotImplementedError

class Uno(Carro):

    def ligar(self):
        print('correr')
    
    def parar(self):
        print('andar')

class Corsa(Carro):

    def ligar(self):
        print('correr')

#virtual base classes
class Hilux:
    def correr(self):
        print('correr')
    
    def andar(self):
        print('andar')

Carro.register(Hilux)

# >>> from interface import Carro, Uno, Corsa, Hilux
# >>> issubclass(Hilux, Carro)
# True
# >>> 

# >>> from interface import Carro, Uno, Corsa, Hilux
# >>> Uno()
# <interface.Uno object at 0x7fedc8cb83d0>
# >>> Corsa()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: Can't instantiate abstract class Corsa with abstract method parar
# >>>