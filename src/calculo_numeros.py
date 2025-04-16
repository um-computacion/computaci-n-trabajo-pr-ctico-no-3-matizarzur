from src.exceptions import NumeroDebeSerPositivo

def ingrese_numero():
    try:
        num= int(input("Ingrese un numero: "))
        if num<0:
            raise NumeroDebeSerPositivo()
        return num
    except ValueError:
        raise ValueError("El numero debe ser valido.")