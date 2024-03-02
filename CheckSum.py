class Checksum:
    def __init__(self) -> None:
        self._numero = ''
        self.__resultado = 0
    
    def entrada_dato(self)->None:
        while True:
            self._numero = input('Ingrese un numero entrero >> ')
            try:
                num = int(self._numero)
                break
            except Exception as e:
                print('El dato ingresado no es nunumero')
                print(e)
        print()

    def __ejecutar_checksum(self)->None:
        suma = []
        for index, val in enumerate(self._numero):
           suma.append(int(val) * (index + 1))
        self.__resultado = sum(suma) % 10
        
    def mostrar_checksum(self)->int:
        self.__ejecutar_checksum()
        return self.__resultado