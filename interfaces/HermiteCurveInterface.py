import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from services.HermiteCurveService import Point, HermiteCurveService

class HermiteCurveInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Rasterizador - Curva de Hermite")

        self.figure, (self.axis) = plt.subplots(1, figsize=(12, 6))
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.entryPoints = []
        self.entryTangents = []

        self.CreateInterface()
        self.UpdateGraphics()
        pass

    def CreateInterface(self):
        self.frameControl = ttk.Frame(self.root)
        self.frameControl.pack(side=tk.BOTTOM, fill=tk.X)

        self.framePoint = tk.Frame(self.frameControl, padx=10, pady=10)
        self.framePoint.grid(row=1, column=0, columnspan=4, padx=10)

        self.AddEntryRow()

        ttk.Button(self.frameControl, text="Adicionar Ponto e Tangente", command=self.AddEntryRow).grid(row=0, column=0, columnspan=4, pady=15)

        tk.Label(self.frameControl, text="Resolução").grid(row=2, column=0, padx=10, pady=5)
        self.resolution = tk.StringVar(value="100x100")
        resolutionOptions = ["100x100", "300x300", "800x600", "1920x1080"]
        resolutionCombobox = ttk.Combobox(self.frameControl, textvariable=self.resolution, values=resolutionOptions)
        resolutionCombobox.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.frameControl, text="Quantidade de Segmentos de Retas").grid(row=2, column=2, padx=10, pady=5)
        self.segmentsCount = tk.IntVar(value=3)
        tk.Spinbox(self.frameControl, from_=1, to_=100, textvariable=self.segmentsCount).grid(row=2, column=3, padx=5, pady=5)

        ttk.Button(self.frameControl, text="Gerar Curva", command=self.CurveDrawer).grid(row=2, column=4, columnspan=4, padx=10,pady=10)

    def AddEntryRow(self):
        columnCount = len(self.entryPoints)

        xPoint = tk.Entry(self.framePoint, width=10)
        yPoint = tk.Entry(self.framePoint, width=10)
        tk.Label(self.framePoint, text=f"Ponto {columnCount + 1} (x, y)").grid(row=1, column=columnCount*3, padx=5, pady=5)
        xPoint.grid(row=1, column=(columnCount*3)+1, padx=5, pady=5)
        yPoint.grid(row=1, column=(columnCount*3)+2, padx=5, pady=5)
        self.entryPoints.append((xPoint, yPoint))

        txPoint = tk.Entry(self.framePoint, width=10)
        tyPoint = tk.Entry(self.framePoint, width=10)
        tk.Label(self.framePoint, text=f"Tangente {columnCount + 1} (x, y)").grid(row=2, column=columnCount*3, padx=5, pady=5)
        txPoint.grid(row=2, column=(columnCount*3)+1, padx=5, pady=5)
        tyPoint.grid(row=2, column=(columnCount*3)+2, padx=5, pady=5)
        self.entryTangents.append((txPoint, tyPoint))

    def EntryValidation(self):
        points = []
        tangents = []

        try:
            for (xPoint, yPoint) in self.entryPoints:
                x = xPoint.get().strip()
                y = yPoint.get().strip()
                if x and y:
                    x = float(x)
                    y = float(y)
                    if not (-1 <= x <= 1 and -1 <= y <= 1):
                        raise ValueError(f"Os Pontos devem estar entre [-1, 1].")
                    points.append(Point(x, y))

            for (txPoint, tyPoint) in self.entryTangents:
                x = txPoint.get().strip()
                y = tyPoint.get().strip()
                if x and y:
                    x = float(x)
                    y = float(y)
                    if not (-1 <= x <= 1 and -1 <= y <= 1):
                        raise ValueError(f"As Tangentes devem estar entre [-1, 1].")
                    tangents.append(Point(x, y))

            return points, tangents
        except ValueError as e:
            messagebox.showerror("Erro", f"Dados Inválidos: {e}")
            return None, None

    def CurveDrawer(self):
        points, tangents = self.EntryValidation()
        if points is None or tangents is None:
            return

        try:
            resolutionString = self.resolution.get()
            resolution = tuple(map(int, resolutionString.split("x")))
            segmentsCount = self.segmentsCount.get()

            curve = HermiteCurveService(points, tangents)
            self.axis.clear()
            curve.CurveDrawer(segmentsCount=segmentsCount, resolution=resolution, axis=self.axis)
            self.canvas.draw()
        except ValueError as e:
            messagebox.showerror("Erro", f"Dados inválidos: {e}")

    def UpdateGraphics(self):
        self.axis.clear()
        self.canvas.draw()
