import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from services.HermiteCurveService import Point, HermiteCurveService

class HermiteCurveInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Curva de Hermite")

        # Configuração da figura e eixos para gráficos
        self.figure, (self.ax1) = plt.subplots(1, figsize=(12, 6))
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.pontos_entries = []
        self.tangentes_entries = []

        self.create_widgets()
        self.update_plots()
        pass

    def create_widgets(self):
        self.control_frame = ttk.Frame(self.root)
        self.control_frame.pack(side=tk.BOTTOM, fill=tk.X)

        # Layout de entrada para pontos e tangentes
        self.ponto_frame = tk.LabelFrame(self.control_frame, text="Pontos e Tangentes", padx=10, pady=10)
        self.ponto_frame.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Adicionar entradas iniciais
        self.add_entry_row()

        tk.Button(self.control_frame, text="Adicionar Ponto/Tangente", command=self.add_entry_row).grid(row=1, column=0, columnspan=4, pady=5)

        # Resolução
        tk.Label(self.control_frame, text="Resolução").grid(row=2, column=0, padx=10, pady=5)
        self.resolution_var = tk.StringVar(value="100x100")
        resolutions = ["100x100", "300x300", "800x600", "1920x1080"]
        resolution_menu = ttk.Combobox(self.control_frame, textvariable=self.resolution_var, values=resolutions)
        resolution_menu.grid(row=2, column=1, padx=5, pady=5)

        # Quantidade de segmentos
        tk.Label(self.control_frame, text="Quantidade de Segmentos").grid(row=2, column=2, padx=10, pady=5)
        self.num_segments_var = tk.IntVar(value=3)
        tk.Spinbox(self.control_frame, from_=1, to_=100, textvariable=self.num_segments_var).grid(row=2, column=3, padx=5, pady=5)

        # Botão de Plotar
        tk.Button(self.control_frame, text="Plotar Curva", command=self.curveDrawer).grid(row=3, column=0, columnspan=4, pady=10)

    def add_entry_row(self):
        row_count = len(self.pontos_entries)

        # Adicionar linha para pontos
        x_entry = tk.Entry(self.ponto_frame, width=10)
        y_entry = tk.Entry(self.ponto_frame, width=10)
        tk.Label(self.ponto_frame, text=f"Ponto {row_count + 1} (x, y)").grid(row=row_count, column=0, padx=5, pady=5)
        x_entry.grid(row=row_count, column=1, padx=5, pady=5)
        y_entry.grid(row=row_count, column=2, padx=5, pady=5)
        self.pontos_entries.append((x_entry, y_entry))

        # Adicionar linha para tangentes
        x_entry_t = tk.Entry(self.ponto_frame, width=10)
        y_entry_t = tk.Entry(self.ponto_frame, width=10)
        tk.Label(self.ponto_frame, text=f"Tangente {row_count + 1} (x, y)").grid(row=row_count, column=3, padx=5, pady=5)
        x_entry_t.grid(row=row_count, column=4, padx=5, pady=5)
        y_entry_t.grid(row=row_count, column=5, padx=5, pady=5)
        self.tangentes_entries.append((x_entry_t, y_entry_t))

    def validar_entrada(self):
        pontos = []
        tangentes = []

        try:
            for (x_entry, y_entry) in self.pontos_entries:
                x = x_entry.get().strip()
                y = y_entry.get().strip()
                if x and y:
                    x = float(x)
                    y = float(y)
                    if not (-1 <= x <= 1 and -1 <= y <= 1):
                        raise ValueError(f"Os valores devem estar no intervalo [-1, 1].")
                    pontos.append(Point(x, y))

            for (x_entry, y_entry) in self.tangentes_entries:
                x = x_entry.get().strip()
                y = y_entry.get().strip()
                if x and y:
                    x = float(x)
                    y = float(y)
                    if not (-1 <= x <= 1 and -1 <= y <= 1):
                        raise ValueError(f"Os valores devem estar no intervalo [-1, 1].")
                    tangentes.append(Point(x, y))

            return pontos, tangentes
        except ValueError as e:
            messagebox.showerror("Erro", f"Dados inválidos: {e}")
            return None, None

    def curveDrawer(self):
        pontos, tangentes = self.validar_entrada()
        if pontos is None or tangentes is None:
            return

        try:
            resolution_str = self.resolution_var.get()
            resolution = tuple(map(int, resolution_str.split("x")))
            num_segments = self.num_segments_var.get()

            curva = HermiteCurveService(pontos, tangentes)
            self.ax1.clear()
            curva.curveDrawer(num_segments=num_segments, resolution=resolution, ax1=self.ax1)
            self.canvas.draw()
        except ValueError as e:
            messagebox.showerror("Erro", f"Dados inválidos: {e}")

    def update_plots(self):
        self.ax1.clear()
        self.canvas.draw()
