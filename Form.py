# ---------------------------------------------------------
# Descripción
# ---------------------------------------------------------
# Creación de un formulario para cargar y consultar artículos.
#
# La base de esté código se tomó de
# https://www.tutorialesprogramacionya.com/pythonya/detalleconcepto.php?punto=88&codigo=89&inicio=75
# ---------------------------------------------------------


# ---------------------------------------------------------
# Librerías a usar
# ---------------------------------------------------------
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
# import Items
# ---------------------------------------------------------


# ---------------------------------------------------------
# Clase a usar
# ---------------------------------------------------------
class Form:
    # -----------------------------------------------------
    def __init__(self):
        # -------------------------------------------------
        # # Inicialización de la clase Items y la ventana principal
        # self.item = Items.Items()

        # Creación de la ventana principal y el cuaderno de pestañas
        self.window = tk.Tk()

        # Configuración de la ventana principal
        self.window.title("Item Management")

        # Evita que la ventana se pueda redimensionar
        self.window.resizable(False, False)

        # Creación del cuaderno de pestañas
        self.notebook = ttk.Notebook(self.window)
        # -------------------------------------------------

        # -------------------------------------------------
        # Creación de las pestañas del cuaderno
        self.frame_new_item()
        self.frame_find_item()
        self.frame_all_items()
        # -------------------------------------------------

        # -------------------------------------------------
        # Posicionamiento del cuaderno en la ventana principal
        self.notebook.grid(column=0, row=0, padx=10, pady=10)

        # Mostrar la ventana principal
        # Esto inicia el bucle principal de la interfaz gráfica
        self.window.mainloop()

    # -----------------------------------------------------

    # -----------------------------------------------------
    def frame_new_item(self):
        self.page1 = ttk.Frame(self.notebook)
        self.notebook.add(self.page1, text="Load Items")
        self.label_frame1 = ttk.LabelFrame(self.page1, text="Item")
        self.label_frame1.grid(column=0, row=0, padx=5, pady=10)

        self.label1 = ttk.Label(self.label_frame1, text="Description:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.description_load = tk.StringVar()
        self.entry_description = ttk.Entry(
            self.label_frame1, textvariable=self.description_load
        )
        self.entry_description.grid(column=1, row=0, padx=4, pady=4)
        self.entry_description.focus()

        self.label2 = ttk.Label(self.label_frame1, text="Price:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.price_load = tk.StringVar()
        self.entry_price = ttk.Entry(self.label_frame1, textvariable=self.price_load)
        self.entry_price.grid(column=1, row=1, padx=4, pady=4)

        self.button1 = ttk.Button(
            self.label_frame1, text="Confirm", command=self.add_item
        )
        self.button1.grid(column=1, row=2, padx=4, pady=4)

    # -----------------------------------------------------

    # -----------------------------------------------------
    def add_item(self):
        data = (self.description_load.get(), self.price_load.get())
        self.item.add(data)
        mb.showinfo("Information", "Data has been loaded")
        self.description_load.set("")
        self.price_load.set("")

    # -----------------------------------------------------

    # -----------------------------------------------------
    def frame_find_item(self):
        self.page2 = ttk.Frame(self.notebook)
        self.notebook.add(self.page2, text="Query by Code")
        self.label_frame2 = ttk.LabelFrame(self.page2, text="Item")
        self.label_frame2.grid(column=0, row=0, padx=5, pady=10)

        self.label1 = ttk.Label(self.label_frame2, text="Code:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.code = tk.StringVar()
        self.entry_code = ttk.Entry(self.label_frame2, textvariable=self.code)
        self.entry_code.grid(column=1, row=0, padx=4, pady=4)

        self.label2 = ttk.Label(self.label_frame2, text="Description:")

        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.description = tk.StringVar()
        self.entry_description = ttk.Entry(
            self.label_frame2, textvariable=self.description, state="readonly"
        )
        self.entry_description.grid(column=1, row=1, padx=4, pady=4)
        self.label3 = ttk.Label(self.label_frame2, text="Price:")
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.price = tk.StringVar()
        self.entry_price = ttk.Entry(
            self.label_frame2, textvariable=self.price, state="readonly"
        )
        self.entry_price.grid(column=1, row=2, padx=4, pady=4)
        self.button1 = ttk.Button(
            self.label_frame2, text="Consult", command=self.consult
        )
        self.button1.grid(column=1, row=3, padx=4, pady=4)

    # -----------------------------------------------------

    # -----------------------------------------------------
    def consult(self):
        data = (self.code.get(),)
        response = self.item.query(data)
        if len(response) > 0:
            self.description.set(response[0][0])
            self.price.set(response[0][1])
        else:
            mb.showerror("Error", "Item not found")
            self.description.set("")
            self.price.set("")

    # -----------------------------------------------------

    # -----------------------------------------------------
    def frame_all_items(self):
        self.page3 = ttk.Frame(self.notebook)
        self.notebook.add(self.page3, text="Full List")
        self.label_frame3 = ttk.LabelFrame(self.page3, text="Items")
        self.label_frame3.grid(column=0, row=0, padx=5, pady=10)

        self.text_area = st.ScrolledText(self.label_frame3, width=40, height=10)
        self.text_area.grid(column=0, row=0, padx=4, pady=4)

        self.button2 = ttk.Button(
            self.label_frame3, text="Show Full List", command=self.show_full_list
        )
        self.button2.grid(column=0, row=1, padx=4, pady=4)

    # -----------------------------------------------------

    # -----------------------------------------------------
    def show_full_list(self):
        response = self.item.get_all()
        self.text_area.delete("1.0", tk.END)
        for row in response:
            self.text_area.insert(
                tk.END, f"Code: {row[0]}\nDescription: {row[1]}\nPrice: {row[2]}\n\n"
            )


# ---------------------------------------------------------


# ---------------------------------------------------------
# Ejecución del programa
if __name__ == "__main__":
    form = Form()
# ---------------------------------------------------------
