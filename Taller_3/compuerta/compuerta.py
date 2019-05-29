'''Este módulo contiene el código fuente para crear compuertas lógicas.
   Define una clase padre (Compuerta) y dos clases hijas (CompuertaAND
   y CompuertaOR) así como sus atributos y métodos.
'''


class Compuerta():
    '''La clase Compuerta contiene la definición básica de una compuerta
       lógica, sus atributos (entradas y salida) así como los métodos para
       las asignación y consulta de los atributos

    Args:
        __entrada_a (str): Entada A de Compuerta. Debe ser 1 o 0
        __entrada_b (str): Entada B de Compuerta. Debe ser 1 o 0
        __salida_x (str): Salida X de Compuerta luego de operar
                          entradas A y B. Debe ser 1 o 0
    '''

    __entrada_a = ''
    __entrada_b = ''
    __salida_x = ''

    def set_entrada_a(self, valor_a):
        '''Asignar el valor ingresado (valor_a) al atributo __entrada_a de la
           compuerta. Se valida que sea un valor válido (1 o 0)

        Args:
            valor_a (int): valor que se asignar a entrada A de la compuerta

        Returns:
            salida (boolean): resultado de asignación de valor
        '''
        if valor_a not in ('1', '0'):
            salida = False
        else:
            self.__entrada_a = valor_a
            salida = True
        return salida

    def get_entrada_a(self):
        '''Consulta el valor de la entrada A de la compuerta. Retorna el
           valor de __entrada_a

        Returns:
            __entrada_a (int): valor asignado a entrada A de la compuerta
        '''
        return self.__entrada_a

    def set_entrada_b(self, valor_b):
        '''Asignar el valor ingresado (valor_b) al atributo __entrada_b de la
           compuerta. Se valida que sea un valor válido (1 o 0)

        Args:
            valor_b (int): valor que se asigna a entrada B de la compuerta

        Returns:
            salida (boolean): resultado de asignación de valor
        '''
        if valor_b not in ('1', '0'):
            salida = False
        else:
            self.__entrada_b = valor_b
            salida = True
        return salida

    def get_entrada_b(self):
        '''Consulta el valor de la entrada B de la compuerta. Retorna el
           valor de __entrada_b

        Returns:
            __entrada_b (int): valor asignado a entrada B de la compuerta
        '''
        return self.__entrada_b

    def set_salida_x(self, valor_x):
        '''Asignar el valor ingresado (valor_x) al atributo __salida_x de la
           compuerta. Se valida que sea un valor válido (1 o 0)

        Args:
            valor_x (int): valor que se asigna a salida X de la compuerta

        Returns:
            salida (boolean): resultado de asignación de valor
        '''
        if valor_x not in ('1', '0'):
            salida = False
        else:
            self.__salida_x = valor_x
            salida = True
        return salida

    def get_salida_x(self):
        '''Consulta el valor de la salida de la compuerta. Retorna el
           valor de __salida_x

        Returns:
            __salida_x (int): resultado de operar las entradas de la compuerta
        '''
        return self.__salida_x


class CompuertaAND(Compuerta):
    '''La clase CompuertaAND es hija de la clase Compuerta, además de los
       atributos y métodos de la clase padre, contiene el método Operar
       que define el funcionamiento de una compuerta lógica AND

    Args:
        __entrada_a (int): Entada A de Compuerta. Debe ser 1 o 0
        __entrada_b (int): Entada B de Compuerta. Debe ser 1 o 0
        __salida_x (int): Salida X de Compuerta luego de operar
                          entradas A y B. Debe ser 1 o 0
    '''
    def operar(self):
        '''Realiza las operaciones lógicas de la compuerta AND tomando
           como parámetros las entradas (A y B) de la compuerta y el
           resultado lo asigna a la salida de la compuerta (__salida_x)
        '''
        if self.get_entrada_a() == '1' and self.get_entrada_b() == '1':
            self.set_salida_x('1')
        else:
            self.set_salida_x('0')


class CompuertaOR(Compuerta):
    '''La clase CompuertaOR es hija de la clase Compuerta, además de los
       atributos y métodos de la clase padre, contiene el método Operar
       que define el funcionamiento de una compuerta lógica OR

    Args:
        __entrada_a (int): Entada A de Compuerta. Debe ser 1 o 0
        __entrada_b (int): Entada B de Compuerta. Debe ser 1 o 0
        __salida_x (int): Salida X de Compuerta luego de operar
                          entradas A y B. Debe ser 1 o 0
    '''

    def operar(self):
        '''Realiza la operaciones lógicas de la compuerta OR tomando
           como parámetros las entradas (A y B) de la compuerta y el
           resultado lo asigna a la salida de la compuerta (__salida_x)
        '''
        if self.get_entrada_a() == '0' and self.get_entrada_b() == '0':
            self.set_salida_x('0')
        else:
            self.set_salida_x('1')
