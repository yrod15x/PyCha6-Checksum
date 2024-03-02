class Checksum:
    def __init__(self) -> None:
        self._numero = ''
    
    def entrada_dato(self):
        while True:
            self._numero = input('Ingrese un numero entrero >> ')
            try:
                num = int(self._numero)
                break
            except Exception as e:
                print('El dato ingresado no es nunumero')
                print(e)