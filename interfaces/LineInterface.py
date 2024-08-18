import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from services.LineService import RasterizeImage

class LineInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Rasterizador - Reta")
        
        self.resolutions = {
            "100x100": (100, 100),
            "300x300": (300, 300),
            "800x600": (800, 600),
            "1920x1080": (1920, 1080)
        }
        self.currentResolution = self.resolutions["100x100"]

        self.figure, (self.axis) = plt.subplots(1, figsize=(12, 6))
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        self.segments = []
        
        self.CreateInterface()
        self.UpdateGraphics()
        pass

    def CreateInterface(self):        
        self.frameControl = ttk.Frame(self.root)
        self.frameControl.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.firstXEntry = ttk.Entry(self.frameControl, width=10)
        self.firstXEntry.grid(row=0, column=1, padx=5, pady=5)
        
        self.firstYEntry = ttk.Entry(self.frameControl, width=10)
        self.firstYEntry.grid(row=1, column=1, padx=5, pady=5)
        
        self.secondXEntry = ttk.Entry(self.frameControl, width=10)
        self.secondXEntry.grid(row=0, column=5, padx=5, pady=5)
        
        self.secondYEntry = ttk.Entry(self.frameControl, width=10)
        self.secondYEntry.grid(row=1, column=5, padx=5, pady=5)
        
        ttk.Label(self.frameControl, text="Primeiro X:").grid(row=0, column=0, padx=5, pady=5)
        ttk.Label(self.frameControl, text="Primeiro Y:").grid(row=1, column=0, padx=5, pady=5)

        ttk.Label(self.frameControl, text="Segundo X:").grid(row=0, column=4, padx=5, pady=5)
        ttk.Label(self.frameControl, text="Segundo Y:").grid(row=1, column=4, padx=5, pady=5)
        
        self.addButton = ttk.Button(self.frameControl, text="Adicionar Reta", command=self.AddSegment)
        self.addButton.grid(row=0, column=8, columnspan=2, padx=10, pady=5)
        
        self.clearButton = ttk.Button(self.frameControl, text="Limpar Retas", command=self.ClearSegments)
        self.clearButton.grid(row=1, column=8, columnspan=2, padx=10, pady=5)
        
        ttk.Label(self.frameControl, text="Resolução:").grid(row=0, column=12, padx=10, pady=5)
        self.resolution = tk.StringVar(value="800x600")
        resolutionCombobox = ttk.Combobox(self.frameControl, textvariable=self.resolution, values=list(self.resolutions.keys()))
        resolutionCombobox.grid(row=0, column=13, padx=5, pady=5)
        
        self.refreshGraphicsButton = ttk.Button(self.frameControl, text="Atualizar Gráficos", command=self.UpdateGraphics)
        self.refreshGraphicsButton.grid(row=1, column=12, columnspan=2, padx=10, pady=5)

    def AddSegment(self):
        try:
            firstX = float(self.firstXEntry.get())
            firstY = float(self.firstYEntry.get())
            secondX = float(self.secondXEntry.get())
            secondY = float(self.secondYEntry.get())
            self.segments.append(((firstX, firstY), (secondX, secondY)))
            self.UpdateGraphics()
        except ValueError:
            messagebox.showerror("Erro", "Valores Inválidos! Insira os dados corretamente.")

    def ClearSegments(self):
        self.segments = []
        self.UpdateGraphics()

    def UpdateGraphics(self):
        self.axis.clear()
        
        selectedResolution = self.resolution.get()
        self.currentResolution = self.resolutions[selectedResolution]
        
        rasterizedImage = RasterizeImage(self.segments, *self.currentResolution)

        self.axis.clear()
        self.axis.imshow(rasterizedImage, cmap='Reds', origin='lower')
        self.axis.set_title('Reta(s) Rasterizada(s)')
        
        self.canvas.draw()
        