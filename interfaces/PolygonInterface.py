import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from services.PolygonService import PolygonServices

class PolygonInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Interface de Desenho de Polígonos")

        # Resolução padrão
        self.resolutions = {
            "100x100": (100, 100),
            "300x300": (300, 300),
            "800x600": (800, 600),
            "1920x1080": (1920, 1080)
        }
        self.current_resolution = self.resolutions["100x100"]

        # Criação da figura e do eixo
        self.figure, self.ax1 = plt.subplots(figsize=(8, 6))
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.create_widgets()
        self.update_plots()
        pass

    def create_widgets(self):
        self.control_frame = ttk.Frame(self.root)
        self.control_frame.pack(side=tk.BOTTOM, fill=tk.X)

        # Menu suspenso para seleção do polígono
        self.shape_var = tk.StringVar(value='Triângulo Equilátero 1')
        shapes = ['Triângulo Equilátero 1', 'Triângulo Equilátero 2', 'Quadrado 1', 'Quadrado 2', 'Hexágono 1', 'Hexágono 2']
        shape_menu = ttk.Combobox(self.control_frame, textvariable=self.shape_var, values=shapes)
        shape_menu.grid(row=0, column=1, padx=5, pady=5)

        # Menu suspenso para seleção da resolução
        ttk.Label(self.control_frame, text="Resolução").grid(row=1, column=0, padx=10, pady=5)
        self.resolution_var = tk.StringVar(value="800x600")
        resolution_menu = ttk.Combobox(self.control_frame, textvariable=self.resolution_var, values=list(self.resolutions.keys()))
        resolution_menu.grid(row=1, column=1, padx=5, pady=5)
        resolution_menu.bind("<<ComboboxSelected>>", self.update_plots)

        # Botão para mostrar o polígono
        show_button = ttk.Button(self.control_frame, text="Mostrar Polígono", command=self.update_plots)
        show_button.grid(row=2, column=0, columnspan=2, pady=5)

    def update_plots(self, event=None):
        # Limpa o eixo antes de adicionar novos gráficos
        self.ax1.clear()

        # Atualiza a resolução com base na seleção do menu
        selected_resolution = self.resolution_var.get()
        self.current_resolution = self.resolutions[selected_resolution]
        width, height = self.current_resolution

        # Atualiza o gráfico com a imagem do polígono
        shape = self.shape_var.get()
        vertices = PolygonServices.get_polygon_vertices(shape)
        image = PolygonServices.scanline(vertices, width, height)
        
         # Exibe a imagem na tela
        self.ax1.imshow(image, cmap='gray', origin='lower')
        self.ax1.set_title(f"{shape} ({selected_resolution})")
        self.ax1.set_xlabel(f'X (0 to {width})')
        self.ax1.set_ylabel(f'Y (0 to {height})')
        self.ax1.axis('on')
        
        # Atualiza o canvas
        self.canvas.draw()