from src.exceptions import NumeroDebeSerPositivo

def ingrese_numero():
    try:
        num= int(input("Ingrese un numero: "))
        if num<0:
            raise NumeroDebeSerPositivo()
        return num
    except ValueError:
        raise ValueError("El numero debe ser valido.")
    

def main():
    while True:
        try:
            num=ingrese_numero()
            print(f"Numero valido: {num}")
        except NumeroDebeSerPositivo as error1:
            print(f"Error: {error1}")
        except ValueError as error2:
            print(f"Error: {error2}")
        
        continuar= input(f"¿Desea continuar?(Marque 1 para continuaro, caso contrario ingrese cualquier caracter): ")
        if continuar!=1:
            break
        
if __name__=="__main__":
    main()