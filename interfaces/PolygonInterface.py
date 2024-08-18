import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from services.PolygonService import PolygonServices
from services.LineService import RasterizeImage

class PolygonInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Rasterizador - Polígonos")

        self.resolutions = {
            "100x100": (100, 100),
            "300x300": (300, 300),
            "800x600": (800, 600),
            "1920x1080": (1920, 1080)
        }
        self.currentResolution = self.resolutions["100x100"]

        self.figure, self.axis = plt.subplots(figsize=(8, 6))
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.CreateInterface()
        self.UpdateGraphics()

        pass

    def CreateInterface(self):
        self.frameControl = ttk.Frame(self.root)
        self.frameControl.pack(side=tk.BOTTOM, fill=tk.X)
        
        ttk.Label(self.frameControl, text="Polígono: ").grid(row=0, column=0, pady=5)
        self.polygonShape = tk.StringVar(value='Triângulo')
        polygonShapeOptions = ['Triângulo', 'Quadrado', 'Hexágono']
        polygonShapeCombobox = ttk.Combobox(self.frameControl, textvariable=self.polygonShape, values=polygonShapeOptions)
        polygonShapeCombobox.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Label(self.frameControl, text="Resolução: ").grid(row=0, column=2, padx=10, pady=5)
        self.resolution = tk.StringVar(value="100x100")
        resolutionCombobox = ttk.Combobox(self.frameControl, textvariable=self.resolution, values=list(self.resolutions.keys()))  # Substitua pelos valores reais
        resolutionCombobox.grid(row=0, column=3, padx=5, pady=5)
        
        ttk.Label(self.frameControl, text="Rotação: ").grid(row=0, column=4, padx=10, pady=5)
        self.rotation = tk.StringVar(value='0° Graus')
        rotationOptions = ['0° Graus', '30° Graus', '45° Graus', '60° Graus', '90° Graus', '120° Graus', '180° Graus', '270° Graus', '360° Graus']
        rotationCombobox = ttk.Combobox(self.frameControl, textvariable=self.rotation, values=rotationOptions)
        rotationCombobox.grid(row=0, column=5, padx=5, pady=5)

        self.isCleanable = tk.BooleanVar(value=False)
        ttk.Checkbutton(self.frameControl, text="Limpar tela ao plotar outra figura?", variable=self.isCleanable).grid(row=0, column=4, padx=10, pady=5)
         
        
        showPolygonButton = ttk.Button(self.frameControl, text="Mostrar Polígono", command=self.UpdateGraphics)
        showPolygonButton.grid(row=0, column=6, columnspan=2, padx=10, pady=5)

    def UpdateGraphics(self):
        self.axis.clear()

        selectedResolution = self.resolution.get()
        self.currentResolution = self.resolutions[selectedResolution]

        shape = self.polygonShape.get()
        rotation = PolygonServices.GetRotationByLabel(self.rotation.get())
        segments = PolygonServices.GetPolygonSegments(shape, rotation)
        rasterizedImage = RasterizeImage(segments, *self.currentResolution)
        
        self.axis.imshow(rasterizedImage, cmap='Reds', origin='lower')
        self.axis.set_title(f"{shape} ({selectedResolution})")
        self.axis.axis('on')
        
        self.canvas.draw()