import numpy as np
from matplotlib.path import Path
from scipy.ndimage import binary_fill_holes

class PolygonServices:
    def normalize_point(x, y, x_min, x_max, y_min, y_max):
        # """
        # Normaliza um ponto (x, y) para o intervalo [-1, 1] com base nos intervalos fornecidos.
        # """
        # x_normalized = 2 * (x - x_min) / (x_max - x_min) - 1
        # y_normalized = 2 * (y - y_min) / (y_max - y_min) - 1
        # return x_normalized, y_normalized
        return

    def scanline(vertices, width, height):
        # """
        # Rasteriza um polígono em uma imagem de resolução (width, height) usando o algoritmo de cruzamento.
        # """
        # # Normaliza os pontos
        # normalized_vertices = [PolygonServices.normalize_point(x, y, -1, 1, -1, 1) for x, y in vertices]
        # # Converte os pontos normalizados para a resolução da imagem
        # vertices = [(int((x + 1) * (width - 1) / 2), int((y + 1) * (height - 1) / 2)) for x, y in normalized_vertices]
        
        # # Cria uma imagem em branco
        # image = np.zeros((height, width), dtype=np.uint8)
        
        # # Cria um Path do matplotlib para o polígono
        # path = Path(vertices)
        
        # # Gera uma grade de coordenadas (x, y)
        # x, y = np.meshgrid(np.arange(width), np.arange(height))
        # points = np.vstack((x.ravel(), y.ravel())).T
        
        # # Verifica se os pontos estão dentro do polígono
        # grid = path.contains_points(points)
        
        # # Preenche a imagem com os pontos dentro do polígono
        # image[grid.reshape(height, width)] = 1
        
        # # Preenchimento usando flood-fill para lidar com qualquer lacuna interna
        # floodfill = binary_fill_holes(image).astype(np.uint8)
        
        # return floodfill
        return

    def generate_triangle(rotation=0):
        # """
        # Gera um triângulo equilátero.
        # """
        # angle = np.deg2rad(rotation)
        # cos_a = np.cos(angle)
        # sin_a = np.sin(angle)
        # vertices = [
        #     (0, 1),
        #     (np.sqrt(3)/2, -0.5),
        #     (-np.sqrt(3)/2, -0.5)
        # ]
        # rotated_vertices = [
        #     (x * cos_a - y * sin_a, x * sin_a + y * cos_a)
        #     for x, y in vertices
        # ]
        # return rotated_vertices
        return

    def generate_square(rotation=0):
        # """
        # Gera um quadrado.
        # """
        # angle = np.deg2rad(rotation)
        # cos_a = np.cos(angle)
        # sin_a = np.sin(angle)
        # vertices = [
        #     (-0.5, -0.5),
        #     (0.5, -0.5),
        #     (0.5, 0.5),
        #     (-0.5, 0.5)
        # ]
        # rotated_vertices = [
        #     (x * cos_a - y * sin_a, x * sin_a + y * cos_a)
        #     for x, y in vertices
        # ]
        # return rotated_vertices
        return

    def generate_hexagon(rotation=0):
        # """
        # Gera um hexágono regular.
        # """
        # angle = np.deg2rad(rotation)
        # cos_a = np.cos(angle)
        # sin_a = np.sin(angle)
        # vertices = [
        #     (np.cos(np.deg2rad(60 * i)), np.sin(np.deg2rad(60 * i)))
        #     for i in range(6)
        # ]
        # rotated_vertices = [
        #     (x * cos_a - y * sin_a, x * sin_a + y * cos_a)
        #     for x, y in vertices
        # ]
        # return rotated_vertices
        return

    def get_polygon_vertices(shape, rotation=0):
        # """
        # Retorna os vértices do polígono com base na forma e rotação.
        # """
        # if shape == 'Triângulo Equilátero 1':
        #     return PolygonServices.generate_triangle(rotation)
        # elif shape == 'Triângulo Equilátero 2':
        #     return PolygonServices.generate_triangle(rotation=30)
        # elif shape == 'Quadrado 1':
        #     return PolygonServices.generate_square(rotation)
        # elif shape == 'Quadrado 2':
        #     return PolygonServices.generate_square(rotation=45)
        # elif shape == 'Hexágono 1':
        #     return PolygonServices.generate_hexagon(rotation)
        # elif shape == 'Hexágono 2':
        #     return PolygonServices.generate_hexagon(rotation=30)
        # else:
        #     raise ValueError("Forma desconhecida")
        return
