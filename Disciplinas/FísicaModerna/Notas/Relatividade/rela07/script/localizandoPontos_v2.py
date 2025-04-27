import matplotlib.pyplot as plt
import math as m
from sympy import symbols, Rational, sqrt, simplify, N, pprint, init_printing, sin, cos, tan, pi
from sympy.abc import x, w, beta

# Inicializa impressão simbólica bonita
init_printing()

# Função simbólica para transformação de Lorentz
def minkowski_transform_sym(x_val, w_val, beta_val):
    gamma = 1 / sqrt(1 - beta**2)
    x_prime_expr = gamma * (x - beta * w)
    w_prime_expr = gamma * (w - beta * x)

    subs_dict = {x: x_val, w: w_val, beta: beta_val}
    x_prime_sym = simplify(x_prime_expr.subs(subs_dict))
    w_prime_sym = simplify(w_prime_expr.subs(subs_dict))

    x_prime_num = float(N(x_prime_sym))
    w_prime_num = float(N(w_prime_sym))

    return x_prime_sym, w_prime_sym, x_prime_num, w_prime_num

# Entrada dos dados simbólicos

def input_rational(prompt):
    val = input(prompt).strip().replace(',', '.')
    try:
        return Rational(val)  # Converte decimal ou string diretamente em fração
    except Exception:
        print("Entrada inválida. Use um número decimal (ex: 2.5) ou fração (ex: 5/2).")
        return input_rational(prompt)

print("Digite os valores como frações (ex: 5/2) ou decimais (ex: 2.5)")
xA = input_rational("Digite xA: ")
wA = input_rational("Digite wA (ctA): ")
xB = input_rational("Digite xB: ")
wB = input_rational("Digite wB (ctB): ")

bandeira = True
while bandeira:
    try:
        angle_deg = float(input("Digite o ângulo entre x e x' (em graus): ").replace(',', '.'))
        theta_rad = angle_deg * pi / 180  # simbólico
        beta_val = tan(theta_rad)
        if abs(beta_val) >= 1:
            print("*********************************************************")
            print("O valor de beta = tan(θ) deve ser menor que 1 (|v| < c).")
            print("Digite outro valor")
        else:
            bandeira = False
    except Exception:
        print("Entrada inválida. Digite um número válido para o ângulo.")

gamma_val = 1 / sqrt(1 - beta_val**2)

# Transformações simbólicas e numéricas
xAp_sym, wAp_sym, xAp, wAp = minkowski_transform_sym(xA, wA, beta_val)
xBp_sym, wBp_sym, xBp, wBp = minkowski_transform_sym(xB, wB, beta_val)

print("Coordenadas de A' (simbólicas):")
pprint(xAp_sym)
pprint(wAp_sym)
print("Coordenadas de A' (numéricas):", xAp, wAp)

print("Coordenadas de B' (simbólicas):")
pprint(xBp_sym)
pprint(wBp_sym)
print("Coordenadas de B' (numéricas):", xBp, wBp)

# Converte valores para desenho
rmax = 7
numerical_theta = float(N(theta_rad))

# Plotagem
fig, ax = plt.subplots(figsize=(8, 8))
ax.axis('off')
ax.set_aspect('equal')
ax.set_xlim(-0.5, rmax + 0.25)
ax.set_ylim(-0.5, rmax + 0.25)

# Eixos S
ax.arrow(0, 0, rmax, 0, head_width=0.15, color='blue', label='x')
ax.arrow(0, 0, 0, rmax, head_width=0.15, color='blue', label='w')

# Eixos S'
ax.arrow(0, 0, rmax * m.cos(numerical_theta), rmax * m.sin(numerical_theta), head_width=0.15, color='red')
ax.arrow(0, 0, rmax * m.sin(numerical_theta), rmax * m.cos(numerical_theta), head_width=0.15, color='red')

# Eventos em S
ax.plot([float(xA)], [float(wA)], 'ko', markersize=6)
ax.plot([float(xB)], [float(wB)], 'ko', markersize=6)
ax.plot([float(xA), float(xA)], [0, float(wA)], 'k--', alpha=0.5)
ax.plot([float(xB), float(xB)], [0, float(wB)], 'k--', alpha=0.5)
ax.plot([0, float(xA)], [float(wA), float(wA)], 'k--', alpha=0.5)
ax.plot([0, float(xB)], [float(wB), float(wB)], 'k--', alpha=0.5)

plt.show()
