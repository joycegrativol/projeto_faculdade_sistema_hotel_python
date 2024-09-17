import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class Hotel:
    def __init__(self, num_quartos):
        self.num_quartos = num_quartos
        self.quartos_disponiveis = num_quartos
        self.reservas = {}

    def reservar_quarto(self, quarto, nome_cliente):
        if quarto > self.num_quartos or quarto <= 0:
            return "Número de quarto inválido."
        if quarto in self.reservas:
            return "Quarto já reservado."
        if self.quartos_disponiveis <= 0:
            return "Não há quartos disponíveis."

        self.reservas[quarto] = nome_cliente
        self.quartos_disponiveis -= 1
        return f"Quarto {quarto} reservado para {nome_cliente}."

    def cancelar_reserva(self, quarto):
        if quarto not in self.reservas:
            return "Nenhuma reserva encontrada para este quarto."

        del self.reservas[quarto]
        self.quartos_disponiveis += 1
        return f"Reserva do quarto {quarto} cancelada."

    def listar_reservas(self):
        if not self.reservas:
            return "Nenhuma reserva atual."

        reservas_listadas = "\n".join(f"Quarto {quarto}: {nome}" for quarto, nome in self.reservas.items())
        return reservas_listadas

class HotelApp:
    def __init__(self, root):
        self.hotel = Hotel(num_quartos=10)
        self.root = root
        self.root.title("Sistema de Reservas de Hotel")

        # Configurar o estilo
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Arial', 10), padding=10)
        self.style.configure('TLabel', font=('Arial', 12))
        self.style.configure('TEntry', font=('Arial', 12))
        self.style.configure('TFrame', background='#f0f0f0')

        self.create_widgets()

    def create_widgets(self):
        # Frame principal
        frame = ttk.Frame(self.root, padding="10")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Labels
        ttk.Label(frame, text="Número do Quarto:").grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
        ttk.Label(frame, text="Nome do Cliente:").grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

        # Entry widgets
        self.quarto_entry = ttk.Entry(frame, width=20)
        self.quarto_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)
        self.nome_entry = ttk.Entry(frame, width=20)
        self.nome_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)

        # Buttons
        ttk.Button(frame, text="Reservar Quarto", command=self.reservar_quarto).grid(row=2, column=0, padx=10, pady=10, columnspan=2)
        ttk.Button(frame, text="Cancelar Reserva", command=self.cancelar_reserva).grid(row=3, column=0, padx=10, pady=10, columnspan=2)
        ttk.Button(frame, text="Listar Reservas", command=self.listar_reservas).grid(row=4, column=0, padx=10, pady=10, columnspan=2)

    def reservar_quarto(self):
        try:
            quarto = int(self.quarto_entry.get())
            nome_cliente = self.nome_entry.get()
            resultado = self.hotel.reservar_quarto(quarto, nome_cliente)
            messagebox.showinfo("Resultado", resultado)
        except ValueError:
            messagebox.showerror("Erro", "Número do quarto inválido.")

    def cancelar_reserva(self):
        try:
            quarto = int(self.quarto_entry.get())
            resultado = self.hotel.cancelar_reserva(quarto)
            messagebox.showinfo("Resultado", resultado)
        except ValueError:
            messagebox.showerror("Erro", "Número do quarto inválido.")

    def listar_reservas(self):
        reservas = self.hotel.listar_reservas()
        messagebox.showinfo("Reservas Atuais", reservas)

if __name__ == "__main__":
    root = tk.Tk()
    app = HotelApp(root)
    root.mainloop()
