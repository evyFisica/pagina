import math as m
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.transforms import Affine2D

def minkowski_transform(x, w, beta):
    gamma = 1.0 / m.sqrt(1.0 - beta**2)
    x_prime = gamma * (x - beta * w)
    w_prime = gamma * (w - beta * x)
    return x_prime, w_prime

# Configurações iniciais
rmax  = 10

# Entradas do usuário
xA = float(input("Digite xA: "))
wA = float(input("Digite wA (ctA): "))
xB = float(input("Digite xB: "))
wB = float(input("Digite wB (ctB): "))

bandeira = True
while(bandeira):
    angle_deg = float(input("Digite o ângulo entre x e x' (em graus): "))
    theta_rad = m.radians(angle_deg)
    beta = m.tan(theta_rad)    
    gamma = 1.0 / m.sqrt(1.0 - beta**2)
    if abs(beta) >= 1:
        print("*********************************************************")
        print("O valor de beta = tan(θ) deve ser menor que 1 (|v| < c).")
        print("Digite outro valor")
    else:
        bandeira = False

# # Transformação
xAp, wAp = minkowski_transform(xA, wA, beta)
xBp, wBp = minkowski_transform(xB, wB, beta)

# print(xAp, wAp)
print(f"(xA', wA') = ({xAp:.2f}, {wAp:.2f})")
print(f"(xB', wB') = ({xBp:.2f}, {wBp:.2f})")

xAp_Sx, xAp_Sw = minkowski_transform(xAp, 0, -beta)
wAp_Sx, wAp_Sw = minkowski_transform(0, wAp, -beta)

# print(xAp_Sx, xAp_Sw)
# print(wAp_Sx, wAp_Sw)
print(f"(xA'_Sx, xA'_Sw) = ({xAp_Sx:.2f}, {xAp_Sw:.2f})")
print(f"(wA'_Sx, wA'_Sw) = ({wAp_Sx:.2f}, {wAp_Sw:.2f})")


xBp_Sx, xBp_Sw = minkowski_transform(xBp, 0, -beta)
wBp_Sx, wBp_Sw = minkowski_transform(0, wBp, -beta)

# print(xBp_Sx, xBp_Sw)
# print(wBp_Sx, wBp_Sw)
print(f"(xB'_Sx, xB'_Sw) = ({xBp_Sx:.2f}, {xBp_Sw:.2f})")
print(f"(wB'_Sx, wB'_Sw) = ({wBp_Sx:.2f}, {wBp_Sw:.2f})")

# Configuração da figura
fig, ax = plt.subplots(figsize=(8, 8))
ax.axis('off')  #remove o sistema de eixo proprio do matplotlib
ax.set_aspect('equal')
ax.set_xlim(-0.5, rmax+0.25)
ax.set_ylim(-0.5, rmax+0.25)

# Desenha eixos do sistema S
ax.arrow(0, 0, rmax, 0, head_width=0.15, color='blue', label='x')
ax.arrow(0, 0, 0, rmax, head_width=0.15, color='blue', label='w')

# Desenha eixos do sistema S'
# Eixo x'
ax.arrow(0, 0, rmax*m.cos(theta_rad), rmax*m.sin(theta_rad), head_width=0.15, color='red', label="x'")
# Eixo w'
ax.arrow(0, 0, rmax*m.sin(theta_rad), rmax*m.cos(theta_rad), head_width=0.15, color='red', label="w'")

# Desenha o evento A e B em S e suas projeções
ax.plot(xA, wA, 'ko', markersize=6)
ax.plot(xB, wB, 'ko', markersize=6)
ax.plot([xA, xA], [0, wA], 'k--', alpha=0.5)
ax.plot([xB, xB], [0, wB], 'k--', alpha=0.5)
ax.plot([0, xA], [wA, wA], 'k--', alpha=0.5)
ax.plot([0, xB], [wB, wB], 'k--', alpha=0.5)

# Desenha o evento A e B em S' e suas projeções
ax.plot([xA, xAp_Sx], [wA, xAp_Sw], '--', alpha=0.5, color="gray")
ax.plot([xA, wAp_Sx], [wA, wAp_Sw], '--', alpha=0.5, color="gray")
ax.plot([xB, xBp_Sx], [wB, xBp_Sw], '--', alpha=0.5, color="gray")
ax.plot([xB, wBp_Sx], [wB, wBp_Sw], '--', alpha=0.5, color="gray")

#--------------------------  Novo pontos ---------------------------------------------

if (wA == wB):
    print ("Valor iguais de w no ponto A e B = ", wAp)
    wC = wAp / gamma + beta * xB
    xC = xB
    ax.plot(xB, wC, 'ko', markersize=6)
    
    wD = wBp / gamma + beta * xA
    xD = xA
    ax.plot(xA, wD, 'ko', markersize=6)
elif (xA == xB):
    print ("Valor iguais de x no ponto A e B = ", xAp)
    xC = xAp / gamma + beta * wB
    wC = wB
    print(xC, wC)
    ax.plot(xC, wC, 'ko', markersize=6)
    
    xD = xBp / gamma + beta * wA
    wD = wA
    print(xD, wD)
    ax.plot(xD, wD, 'ko', markersize=6)
    ax.plot([xA, xD], [wA, wD], '--', alpha=0.5, color="blue")
    ax.plot([xB, xD], [wB, wD], '--', alpha=0.5, color="blue")
else:
    print ("Nenhuma das coordenadas são iguais")
plt.show()

#ax.plot([0, Px], [Pw, Pw], 'k--', alpha=0.5)

# 
# for i in range(1, int(rmax)+1):
#     #marcas sobre o eixo x
#     # ax.plot([x1, x2], [y1, y2])
#     ax.plot([i, i], [0.0, -0.05], color='blue')
# 
#     #marcas sobre o eixo y
#     # ax.plot([x1, x2], [y1, y2])
#     ax.plot([0.0, -0.05], [i, i], color='blue')


#
# # Função para desenhar as marcas de calibração
# def draw_calibration(ax, angle, scale, color, direction):
#     for r in range(1, 7):
#         # Calcula posição da marca
#         x = r * np.cos(np.radians(angle)) * scale
#         y = r * np.sin(np.radians(angle)) * scale
#         if direction == 'x':
#             # Linha perpendicular ao eixo x'
#             perp_angle = angle - 90
#         else:
#             # Linha perpendicular ao eixo w'
#             perp_angle = angle + 90
#
#         # Comprimento da marca (proporcional ao raio)
#         length = 0.05 * r
#         dx = length * np.cos(np.radians(perp_angle))
#         dy = length * np.sin(np.radians(perp_angle))
#
#         ax.plot([x, x + dx], [y, y + dy], color=color, lw=0.8)
#
# # Desenha marcas de calibração para x' e w'
# draw_calibration(ax, angulo, gamma, 'red', 'x')
# draw_calibration(ax, 90 - angulo, gamma, 'blue', 'w')
#
# # Desenha o evento P e suas projeções
# ax.plot(Px, Pw, 'ko', markersize=5)
# ax.plot([Px, Px], [0, Pw], 'k--', alpha=0.5)
# ax.plot([0, Px], [Pw, Pw], 'k--', alpha=0.5)
#
# # Desenha coordenadas transformadas em S'
# # Projeção em x'
# xl = gamma * (Px - beta*Pw)
# x_transf = xl * np.cos(np.radians(angulo)) * gamma
# y_transf = xl * np.sin(np.radians(angulo)) * gamma
# ax.plot([x_transf, Px], [y_transf, Pw], 'r--', alpha=0.5)
# ax.text(x_transf, y_transf, f'{xl:.2f}', color='red',
#         ha='right', va='bottom', rotation=angulo)
#
# # Projeção em w'
# wl = gamma * (Pw - beta*Px)
# x_transf_w = wl * np.sin(np.radians(angulo)) * gamma
# y_transf_w = wl * np.cos(np.radians(angulo)) * gamma
# ax.plot([x_transf_w, Px], [y_transf_w, Pw], 'b--', alpha=0.5)
# ax.text(x_transf_w, y_transf_w, f'{wl:.2f}', color='blue',
#         ha='left', va='top', rotation=90 - angulo)
#
# # Configurações finais
# plt.legend(loc='upper left')
# plt.grid(alpha=0.3)
plt.show()
