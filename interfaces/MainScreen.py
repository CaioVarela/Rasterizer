import tkinter as tk
from tkinter import ttk
from interfaces.LineInterface import LineInterface
from interfaces.PolygonInterface import PolygonInterface  
from interfaces.HermiteCurveInterface import HermiteCurveInterface

class MainScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("Rasterizador - Home")
        
        # Definindo o tamanho da janela principal
        self.root.geometry("600x400")  # Largura x Altura
        
        # Botão para Rasterização de Retas
        self.line_button = ttk.Button(root, text="Rasterizar Retas", command=self.open_line_drawer, width=30)
        self.line_button.pack(padx=20, pady=20, fill=tk.X)

        # Botão para Rasterização de Polígonos
        self.polygon_button = ttk.Button(root, text="Rasterizar Polígonos", command=self.open_polygon_drawer, width=30)
        self.polygon_button.pack(padx=20, pady=20, fill=tk.X)

        # Botão para Rasterização de Curvas
        self.curve_button = ttk.Button(root, text="Rasterizar Curvas", command=self.open_curve_drawer, width=30)
        self.curve_button.pack(padx=20, pady=20, fill=tk.X)
        pass

    def open_line_drawer(self):
        line_window = tk.Toplevel(self.root)
        LineInterface(line_window)

    def open_polygon_drawer(self):
        polygon_window = tk.Toplevel(self.root)
        PolygonInterface(polygon_window)

    def open_curve_drawer(self):
        curve_window = tk.Toplevel(self.root)
        HermiteCurveInterface(curve_window)
