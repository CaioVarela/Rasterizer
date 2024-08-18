import numpy as np

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class HermiteCurveService:
    def __init__(self, points, tangents):
        if len(points) != len(tangents):
            raise ValueError("A quantidade de pontos deve ser a mesma que a de tangentes.")
        self.points = points
        self.tangents = tangents

    def CurveCalculator(self, pointsCount, p1, t1, p2, t2):
        t = np.linspace(0, 1, pointsCount + 1)

        h00 = 2 * t**3 - 3 * t**2 + 1
        h01 = -2 * t**3 + 3 * t**2
        h10 = t**3 - 2 * t**2 + t
        h11 = t**3 - t**2

        x = h00 * p1.x + h01 * p2.x + h10 * t1.x + h11 * t2.x
        y = h00 * p1.y + h01 * p2.y + h10 * t1.y + h11 * t2.y

        return x, y

    def CoordinatesNormalizer(self, x, y):
        minX, maxX = np.min(x), np.max(x)
        minY, maxY = np.min(y), np.max(y)
        
        rangeX = maxX - minX
        rangeY = maxY - minY

        rangeX = rangeX if rangeX != 0 else 1
        rangeY = rangeY if rangeY != 0 else 1

        x = 2 * (x - minX) / rangeX - 1
        y = 2 * (y - minY) / rangeY - 1

        return x, y

    def ResolutionScalonatizer(self, x, y, resolution):
        width, height = resolution

        x = (x + 1) / 2 * width
        y = (y + 1) / 2 * height

        return x, y

    def LineRasterizer(self, x1, y1, x2, y2):
        points = []
        dx = x2 - x1
        dy = y2 - y1
        steps = int(max(abs(dx), abs(dy)))

        if steps == 0:
            return [(x1, y1)]

        incX = dx / steps
        incY = dy / steps

        x = x1
        y = y1

        for _ in range(steps + 1):
            points.append((round(x), round(y)))
            x += incX
            y += incY

        return points

    def TangentsNormalizer(self):
        tangents = np.array([(t.x, t.y) for t in self.tangents])
        minX, maxX = np.min(tangents[:, 0]), np.max(tangents[:, 0])
        minY, maxY = np.min(tangents[:, 1]), np.max(tangents[:, 1])

        rangeX = maxX - minX
        rangeY = maxY - minY

        rangeX = rangeX if rangeX != 0 else 1
        rangeY = rangeY if rangeY != 0 else 1

        tangents[:, 0] = 2 * (tangents[:, 0] - minX) / rangeX - 1
        tangents[:, 1] = 2 * (tangents[:, 1] - minY) / rangeY - 1

        return [Point(x, y) for x, y in tangents]

    def CurveDrawer(self, segmentsCount, resolution, axis):
        pointsCount = segmentsCount

        if len(self.points) < 2:
            print("Adicione mais pontos para gerar a curva.")
            return

        normalizerTangents = self.TangentsNormalizer()

        width, height = resolution
        imageCombined = np.zeros((height, width), dtype=np.uint8)

        for i in range(len(self.points) - 1):
            x, y = self.CurveCalculator(pointsCount, self.points[i], normalizerTangents[i], self.points[i + 1], normalizerTangents[i + 1])
            x, y = self.CoordinatesNormalizer(x, y)
            x, y = self.ResolutionScalonatizer(x, y, resolution)

            for j in range(len(x) - 1):
                segmentsPoints = self.LineRasterizer(x[j], y[j], x[j + 1], y[j + 1])
                for px, py in segmentsPoints:
                    if 0 <= int(round(py)) < height and 0 <= int(round(px)) < width:
                        imageCombined[int(round(py)), int(round(px))] = 1

        axis.clear()
        axis.imshow(imageCombined, cmap='Reds', origin='lower')
        axis.set_title("Curva(s) de Hermite Rasterizada(s)")
        axis.set_xlim(0, width)
        axis.set_ylim(0, height)
        axis.set_aspect('equal', adjustable='box')
        axis.grid(True)
