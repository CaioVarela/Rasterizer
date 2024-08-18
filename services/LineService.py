import numpy as np

def normalize_point(x, y, x_min, x_max, y_min, y_max):
    """
    Normaliza um ponto (x, y) para o intervalo [-1, 1] com base nos intervalos fornecidos.
    """
    x_normalized = 2 * (x - x_min) / (x_max - x_min) - 1
    y_normalized = 2 * (y - y_min) / (y_max - y_min) - 1
    return x_normalized, y_normalized

def rasterize_line(x0, y0, x1, y1, width, height):
    """
    Rasteriza uma linha entre (x0, y0) e (x1, y1) em uma imagem de resolução (width, height).
    """
    x0, y0 = normalize_point(x0, y0, -1, 1, -1, 1)
    x1, y1 = normalize_point(x1, y1, -1, 1, -1, 1)
    
    x0 = int((x0 + 1) * (width - 1) / 2)
    y0 = int((y0 + 1) * (height - 1) / 2)
    x1 = int((x1 + 1) * (width - 1) / 2)
    y1 = int((y1 + 1) * (height - 1) / 2)
    
    image = np.zeros((height, width), dtype=np.uint8)
    
    dx = x1 - x0
    dy = y1 - y0
    steps = max(abs(dx), abs(dy))
    
    if steps == 0:
        if 0 <= x0 < width and 0 <= y0 < height:
            image[y0, x0] = 1
        return image
    
    steps = int(steps)
    x_inc = dx / steps
    y_inc = dy / steps
    
    x = x0
    y = y0
    
    for _ in range(steps + 1):
        if 0 <= int(round(y)) < height and 0 <= int(round(x)) < width:
            image[int(round(y)), int(round(x))] = 1
        x += x_inc
        y += y_inc
    
    return image

# def plot_normalized_lines(segments, ax):
#     """
#     Plota segmentos de reta em um espaço normalizado [-1, 1].
#     """
#     ax.clear()
#     for (x0, y0), (x1, y1) in segments:
#         ax.plot([x0, x1], [y0, y1], marker='o')
    
#     ax.set_xlim(-1, 1)
#     ax.set_ylim(-1, 1)
#     ax.set_aspect('equal')
#     ax.set_title('Espaço Normalizado')

def plot_rasterized_image(segments, width, height, ax):
    """
    Plota a imagem rasterizada com todos os segmentos de reta.
    """
    combined_image = np.zeros((height, width), dtype=np.uint8)
    for (x0, y0), (x1, y1) in segments:
        image = rasterize_line(x0, y0, x1, y1, width, height)
        combined_image = np.maximum(combined_image, image)
    
    ax.clear()
    ax.imshow(combined_image, cmap='Reds', origin='lower')
    ax.set_title('Rasterização da(s) Reta(s)')
