import numpy as np
import matplotlib.pyplot as plt

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class HermiteCurveService:
    def __init__(self, points, tangents):
        if len(points) != len(tangents):
            raise ValueError("O número de pontos tem que ser igual ao número de tangentes.")
        self.points = points
        self.tangents = tangents

    def curveCalculator(self, num_points, p1, t1, p2, t2):
        t = np.linspace(0, 1, num_points)
        h00 = 2 * t**3 - 3 * t**2 + 1
        h01 = -2 * t**3 + 3 * t**2
        h10 = t**3 - 2 * t**2 + t
        h11 = t**3 - t**2

        x = h00 * p1.x + h01 * p2.x + h10 * t1.x + h11 * t2.x
        y = h00 * p1.y + h01 * p2.y + h10 * t1.y + h11 * t2.y

        return x, y

    def coordinatesNormalizer(self, x, y):
        x_min, x_max = np.min(x), np.max(x)
        y_min, y_max = np.min(y), np.max(y)
        
        # Normalização para o intervalo [-1, 1]
        x_range = x_max - x_min
        y_range = y_max - y_min

        # Evita divisão por zero
        x_range = x_range if x_range != 0 else 1
        y_range = y_range if y_range != 0 else 1

        x = 2 * (x - x_min) / x_range - 1
        y = 2 * (y - y_min) / y_range - 1

        return x, y

    def resolutionScalonatizer(self, x, y, resolution):
        width, height = resolution
        x = (x + 1) / 2 * width
        y = (y + 1) / 2 * height
        return x, y

    def lineRasterizer(self, x1, y1, x2, y2):
        points = []
        dx = x2 - x1
        dy = y2 - y1
        steps = int(max(abs(dx), abs(dy)))

        if steps == 0:
            return [(x1, y1)]

        x_inc = dx / steps
        y_inc = dy / steps

        x = x1
        y = y1

        for _ in range(steps + 1):
            points.append((round(x), round(y)))
            x += x_inc
            y += y_inc

        return points

    def tangentsNormalizer(self):
        """Normaliza as tangents para o intervalo [-1, 1]."""
        tangents = np.array([(t.x, t.y) for t in self.tangents])
        x_min, x_max = np.min(tangents[:, 0]), np.max(tangents[:, 0])
        y_min, y_max = np.min(tangents[:, 1]), np.max(tangents[:, 1])

        x_range = x_max - x_min
        y_range = y_max - y_min

        # Evita divisão por zero
        x_range = x_range if x_range != 0 else 1
        y_range = y_range if y_range != 0 else 1

        tangents[:, 0] = 2 * (tangents[:, 0] - x_min) / x_range - 1
        tangents[:, 1] = 2 * (tangents[:, 1] - y_min) / y_range - 1

        return [Point(x, y) for x, y in tangents]

    def curveDrawer(self, num_segments, resolution, ax1):
        num_points = num_segments * 10 + 1  # Aumentar a densidade dos points para melhor visualização

        if len(self.points) < 2:
            print("Número insuficiente de pontos para gerar a curva.")
            return

        # Normalizar as tangentes
        tangents_normalizadas = self.tangentsNormalizer()

        # # Gráfico normalizado
        # for i in range(len(self.points) - 1):
        #     x, y = self.curveCalculator(num_points, self.points[i], tangents_normalizadas[i], self.points[i + 1], tangents_normalizadas[i + 1])
        #     x, y = self.coordinatesNormalizer(x, y)
        #     ax1.plot(x, y, 'k-', lw=1)

        # ax1.set_title("Espaço Normalizado")
        # ax1.set_xlim(-1, 1)
        # ax1.set_ylim(-1, 1)
        # ax1.set_aspect('equal', adjustable='box')
        # ax1.grid(True)

        # Gráfico rasterizado
        width, height = resolution
        combined_image = np.zeros((height, width), dtype=np.uint8)

        for i in range(len(self.points) - 1):
            x, y = self.curveCalculator(num_points, self.points[i], tangents_normalizadas[i], self.points[i + 1], tangents_normalizadas[i + 1])
            x, y = self.coordinatesNormalizer(x, y)
            x, y = self.resolutionScalonatizer(x, y, resolution)

            for j in range(len(x) - 1):
                points_segmento = self.lineRasterizer(x[j], y[j], x[j + 1], y[j + 1])
                for px, py in points_segmento:
                    if 0 <= int(round(py)) < height and 0 <= int(round(px)) < width:
                        combined_image[int(round(py)), int(round(px))] = 1

        ax1.clear()
        ax1.imshow(combined_image, cmap='Reds', origin='lower')
        ax1.set_title("Curva(s) de Hermite Rasterizada(s)")
        ax1.set_xlim(0, width)
        ax1.set_ylim(0, height)
        ax1.set_aspect('equal', adjustable='box')
        ax1.grid(True)
