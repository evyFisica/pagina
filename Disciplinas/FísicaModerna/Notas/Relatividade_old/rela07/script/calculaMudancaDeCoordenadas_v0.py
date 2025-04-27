import numpy as np
import matplotlib.pyplot as plt
from matplotlib.transforms import Affine2D

# Configurações iniciais
beta = 0.5
gamma = 1 / np.sqrt(1 - beta**2)
angulo = np.degrees(np.arctan(beta))  # Converte radianos para graus

# Coordenadas do evento P no sistema S
Px = 3.0
Pw = 2.5

# Cálculo das coordenadas transformadas em S'
Pxl = gamma * (Px - beta * Pw)
Pwl = gamma * (Pw - beta * Px)

# Configuração da figura
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal')
ax.set_xlim(-0.5, 6.5)
ax.set_ylim(-0.5, 6.5)

# Desenha eixos do sistema S
ax.arrow(0, 0, 6.5, 0, head_width=0.15, color='black', label='x')
ax.arrow(0, 0, 0, 6.5, head_width=0.15, color='black', label='w')

# Desenha eixos do sistema S'
# Eixo x'
ax.arrow(0, 0, 6.5*np.cos(np.radians(angulo)), 6.5*np.sin(np.radians(angulo)), 
         head_width=0.15, color='red', label="x'")
# Eixo w'
ax.arrow(0, 0, -6.5*np.sin(np.radians(angulo)), 6.5*np.cos(np.radians(angulo)), 
         head_width=0.15, color='blue', label="w'")

# Função para desenhar as marcas de calibração
def draw_calibration(ax, angle, scale, color, direction):
    for r in range(1, 7):
        # Calcula posição da marca
        x = r * np.cos(np.radians(angle)) * scale
        y = r * np.sin(np.radians(angle)) * scale
        if direction == 'x':
            # Linha perpendicular ao eixo x'
            perp_angle = angle - 90
        else:
            # Linha perpendicular ao eixo w'
            perp_angle = angle + 90
            
        # Comprimento da marca (proporcional ao raio)
        length = 0.05 * r
        dx = length * np.cos(np.radians(perp_angle))
        dy = length * np.sin(np.radians(perp_angle))
        
        ax.plot([x, x + dx], [y, y + dy], color=color, lw=0.8)

# Desenha marcas de calibração para x' e w'
draw_calibration(ax, angulo, gamma, 'red', 'x')
draw_calibration(ax, 90 - angulo, gamma, 'blue', 'w')

# Desenha o evento P e suas projeções
ax.plot(Px, Pw, 'ko', markersize=5)
ax.plot([Px, Px], [0, Pw], 'k--', alpha=0.5)
ax.plot([0, Px], [Pw, Pw], 'k--', alpha=0.5)

# Desenha coordenadas transformadas em S'
# Projeção em x'
xl = gamma * (Px - beta*Pw)
x_transf = xl * np.cos(np.radians(angulo)) * gamma
y_transf = xl * np.sin(np.radians(angulo)) * gamma
ax.plot([x_transf, Px], [y_transf, Pw], 'r--', alpha=0.5)
ax.text(x_transf, y_transf, f'{xl:.2f}', color='red', 
        ha='right', va='bottom', rotation=angulo)

# Projeção em w'
wl = gamma * (Pw - beta*Px)
x_transf_w = wl * np.sin(np.radians(angulo)) * gamma
y_transf_w = wl * np.cos(np.radians(angulo)) * gamma
ax.plot([x_transf_w, Px], [y_transf_w, Pw], 'b--', alpha=0.5)
ax.text(x_transf_w, y_transf_w, f'{wl:.2f}', color='blue', 
        ha='left', va='top', rotation=90 - angulo)

# Configurações finais
plt.legend(loc='upper left')
plt.grid(alpha=0.3)
plt.show()
