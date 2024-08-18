import tkinter as tk
from tkinter import ttk
from interfaces.LineInterface import LineInterface
from interfaces.PolygonInterface import PolygonInterface  
from interfaces.HermiteCurveInterface import HermiteCurveInterface

class MainScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Rasterizador - Home")
        
        self.root.geometry("400x200")
        
        self.lineButton = ttk.Button(root, text="Retas", command=self.OpenLineWindow, width=30)
        self.lineButton.pack(padx=20, pady=20, fill=tk.X)

        self.curveButton = ttk.Button(root, text="Curvas", command=self.OpenCurveWindow, width=30)
        self.curveButton.pack(padx=20, pady=20, fill=tk.X)

        self.polygonButton = ttk.Button(root, text="Polígonos", command=self.OpenPolygonWindow, width=30)
        self.polygonButton.pack(padx=20, pady=20, fill=tk.X)

        pass

    def OpenLineWindow(self):
        lineWindow = tk.Toplevel(self.root)
        LineInterface(lineWindow)

    def OpenPolygonWindow(self):
        polygonWindow = tk.Toplevel(self.root)
        PolygonInterface(polygonWindow)

    def OpenCurveWindow(self):
        curveWindow = tk.Toplevel(self.root)
        HermiteCurveInterface(curveWindow)
