#Algoritmo de Simulação Teoria do Automatos de Conway Projeto Mastertech
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
# Inicializar a grade para o Jogo da Vida de Conway
grid_size = 10
grid = np.random.choice([0, 1], size=(grid_size, grid_size))

# Função de atualização para a animação
def update(data):
    global grid
    new_grid = grid.copy()
    for i in range(grid_size):
        for j in range(grid_size):
            # Contar vizinhos vivos
            total = (grid[i, (j-1)%grid_size] + grid[i, (j+1)%grid_size] +
                     grid[(i-1)%grid_size, j] + grid[(i+1)%grid_size, j] +
                     grid[(i-1)%grid_size, (j-1)%grid_size] + grid[(i-1)%grid_size, (j+1)%grid_size] +
                     grid[(i+1)%grid_size, (j-1)%grid_size] + grid[(i+1)%grid_size, (j+1)%grid_size])
            
            # Aplicar as regras do Jogo da Vida
            if grid[i, j] == 1:
                if (total < 2) or (total > 3):
                    new_grid[i, j] = 0
            else:
                if total == 3:
                    new_grid[i, j] = 1
    mat.set_data(new_grid)
    grid[:] = new_grid
    return [mat]

# Configuração da animação
fig, ax = plt.subplots()
mat = ax.matshow(grid, cmap="binary")

# Atribuir a animação a uma variável e salvar como GIF
ani = animation.FuncAnimation(fig, update, interval=200, save_count=50)
ani.save("automato.gif", writer="pillow")
