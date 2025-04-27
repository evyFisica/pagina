import math
import matplotlib.pyplot as plt

def minkowski_transform(x, w, angle_deg):
    theta_rad = math.radians(angle_deg)
    beta = math.tan(theta_rad)
    if abs(beta) >= 1:
        raise ValueError("O valor de beta = tan(θ) deve ser menor que 1 (|v| < c).")
    gamma = 1 / math.sqrt(1 - beta**2)
    x_prime = gamma * (x - beta * w)
    w_prime = gamma * (w - beta * x)
    return x_prime, w_prime

# Entradas do usuário
xA = float(input("Digite xA: "))
wA = float(input("Digite wA (ctA): "))
xB = float(input("Digite xB: "))
wB = float(input("Digite wB (ctB): "))
angle_deg = float(input("Digite o ângulo entre x e x' (em graus): "))

# Transformação
xA_p, wA_p = minkowski_transform(xA, wA, angle_deg)
xB_p, wB_p = minkowski_transform(xB, wB, angle_deg)

print(f"A' = ({xA_p:.3f}, {wA_p:.3f})")
print(f"B' = ({xB_p:.3f}, {wB_p:.3f})")

# Gráfico
plt.figure(figsize=(8, 8))
plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.scatter(xA, wA, color='blue', label="A em S")
plt.scatter(xB, wB, color='green', label="B em S")
plt.scatter(xA_p, wA_p, color='red', marker='x', label="A em S'")
plt.scatter(xB_p, wB_p, color='orange', marker='x', label="B em S'")
plt.plot([0, 5], [0, 5 * math.tan(math.radians(angle_deg))], 'r--', label="Eixo x'")
plt.plot([0, -5 * math.tan(math.radians(angle_deg))], [0, 5], 'b--', label="Eixo w'")
plt.xlabel("x")
plt.ylabel("w = ct")
plt.title(f"Transformação de Lorentz (ângulo = {angle_deg}°)")
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()
