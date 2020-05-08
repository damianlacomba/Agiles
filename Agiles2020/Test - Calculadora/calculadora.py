class Calculadora:
    
    total=0
    
    def valor(self):
        return self.total



    def sumar(self,cadena):
        if len(cadena)==0:
            return 0
        else:
            if (cadena[:2]=="//"):
                ini_cad = cadena.find("\n")
                delimiter=cadena[2:ini_cad]
                split1 = cadena[ini_cad+1:].split(delimiter)
            else:
                delimiter=','
                split1 = cadena.split(delimiter)
            lista_num = []
            for i in split1:
                if i != '\n':
                    lista_num.append(i)
            
            suma = 0
            negativos = []
            for i in lista_num:
                nro = round(float(i))
                if(nro<0):
                    negativos.append(nro)
                elif (nro<=1000):
                    suma = suma + nro
                    self.total= suma
            if len(negativos)>0:
                raise ValueError("Se ingreso el número negativo {}".format(negativos))

   

            

            

   

     






