import sys

def multiplicacao_formatada(num1, num2):
    resultado = num1 * num2
    num1_str = str(num1)
    num2_str = str(num2)
    
    unidade = num2_str[-1]
    dezena = num2_str[-2] if len(num2_str) > 1 else '0'
    
    parciais = [
        num1 * int(unidade),
        num1 * int(dezena) * 10
    ]
    
    print(f"  {num1_str}")
    print(f"x {num2_str}")
    print("______")
    for parcial in parciais:
        print(f" {parcial}")
    print("______")
    print(f"{resultado}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python script.py <numero1> <numero2>")
    else:
        try:
            num1 = int(sys.argv[1])
            num2 = int(sys.argv[2])
            multiplicacao_formatada(num1, num2)
        except ValueError:
            print("Por favor, insira números inteiros válidos.")

#python multiplicacao.py 3458 43
