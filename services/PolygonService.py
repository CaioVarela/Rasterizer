import math

class PolygonServices:
    def RotatePolygon(segments, angle):
        radians = math.radians(angle)
        rotatedSegments = []

        for segment in segments:
            (firstX, firstY), (secondX, secondY) = segment
        
            newFirstX = firstX * math.cos(radians) - firstY * math.sin(radians)
            newFirstY = firstX * math.sin(radians) + firstY * math.cos(radians)
            newStart = (newFirstX, newFirstY)
        
            newSecondX = secondX * math.cos(radians) - secondY * math.sin(radians)
            newSecondY = secondX * math.sin(radians) + secondY * math.cos(radians)
            newEnd = (newSecondX, newSecondY)
        
            rotatedSegments.append((newStart, newEnd))
    
        return rotatedSegments

    def GenerateTriangle(rotation=0):
        triangleSegments = [((0.0, 0.0), (1.0, 0.0)), ((0.0, 0.0), (0.5, 1.0)), ((0.5, 1.0), (1.0, 0.0))]

        return PolygonServices.RotatePolygon(triangleSegments, rotation)

    def GenerateSquare(rotation=0):
        squareSegments = [
            ((-0.5, -0.5), (0.5, -0.5)),
            ((0.5, -0.5), (0.5, 0.5)),
            ((0.5, 0.5), (-0.5, 0.5)),
            ((-0.5, 0.5), (-0.5, -0.5))
        ]

        return PolygonServices.RotatePolygon(squareSegments, rotation)

    def GenerateHexagon(rotation=0):
        hexagonSegments = [
            ((1.0, 0.0), (0.5, math.sqrt(3)/2)),
            ((0.5, math.sqrt(3)/2), (-0.5, math.sqrt(3)/2)),
            ((-0.5, math.sqrt(3)/2), (-1.0, 0.0)),
            ((-1.0, 0.0), (-0.5, -math.sqrt(3)/2)),
            ((-0.5, -math.sqrt(3)/2), (0.5, -math.sqrt(3)/2)),
            ((0.5, -math.sqrt(3)/2), (1.0, 0.0))
        ]

        return PolygonServices.RotatePolygon(hexagonSegments, rotation)
    
    def GetRotationByLabel(rotationLabel):
        if rotationLabel == '0° Graus':
            return 0
        elif rotationLabel == '30° Graus':
            return 30
        elif rotationLabel == '45° Graus':
            return 45
        elif rotationLabel == '60° Graus':
            return 60
        elif rotationLabel == '90° Graus':
            return 90
        elif rotationLabel == '120° Graus':
            return 120
        elif rotationLabel == '180° Graus':
            return 180
        elif rotationLabel == '270° Graus':
            return 270
        elif rotationLabel == '360° Graus':
            return 360
        else:
            raise ValueError("Grau de Rotação Inexistente!")

    def GetPolygonSegments(polygonShape, rotation=0):
        if polygonShape == 'Triângulo':
            return PolygonServices.GenerateTriangle(rotation)
        elif polygonShape == 'Quadrado':
            return PolygonServices.GenerateSquare(rotation)
        elif polygonShape == 'Hexágono':
            return PolygonServices.GenerateHexagon(rotation)
        else:
            raise ValueError("Tipo de Polígono Inexistente!")
