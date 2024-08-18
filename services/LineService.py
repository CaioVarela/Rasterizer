import numpy as np

def NormalizePoint(x, y, minX, maxX, minY, maxY):
    normalizedX = 2 * (x - minX) / (maxX - minX) - 1
    normalizedY = 2 * (y - minY) / (maxY - minY) - 1
    return normalizedX, normalizedY

def Rasterize_line(firstX, firstY, secondX, secondY, width, height):
    firstX, firstY = NormalizePoint(firstX, firstY, -1, 1, -1, 1)
    secondX, secondY = NormalizePoint(secondX, secondY, -1, 1, -1, 1)
    
    firstX = int((firstX + 1) * (width - 1) / 2)
    firstY = int((firstY + 1) * (height - 1) / 2)
    secondX = int((secondX + 1) * (width - 1) / 2)
    secondY = int((secondY + 1) * (height - 1) / 2)
    
    image = np.zeros((height, width), dtype=np.uint8)
    
    dx = secondX - firstX
    dy = secondY - firstY
    steps = max(abs(dx), abs(dy))
    
    if steps == 0:
        if 0 <= firstX < width and 0 <= firstY < height:
            image[firstY, firstX] = 1
        return image
    
    steps = int(steps)
    incX = dx / steps
    incY = dy / steps
    
    x = firstX
    y = firstY
    
    for _ in range(steps + 1):
        if 0 <= int(round(y)) < height and 0 <= int(round(x)) < width:
            image[int(round(y)), int(round(x))] = 1
        x += incX
        y += incY
    
    return image

def RasterizeImage(segments, width, height):
    imageCombined = np.zeros((height, width), dtype=np.uint8)

    for (firstX, firstY), (secondX, secondY) in segments:
        image = Rasterize_line(firstX, firstY, secondX, secondY, width, height)
        imageCombined = np.maximum(imageCombined, image)
        
    return imageCombined
