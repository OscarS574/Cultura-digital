def transformar_numero(n):
    if n % 2 == 0:
        return n  # Si es par, se queda igual
    else:
        return (n * 2) - 1  # Si es impar, se transforma

def main():
    suma_total = 0
    print("Transformación y suma de los primeros 10 números naturales:")

    for i in range(1, 11): # El rango en Python llega hasta uno antes del final (1 al 10)
        valor_transformado = transformar_numero(i)
        print(f"Número original: {i}, transformado: {valor_transformado}")
        suma_total += valor_transformado

    print(f"La suma total es: {suma_total}")

if __name__ == "__main__":
    main()
