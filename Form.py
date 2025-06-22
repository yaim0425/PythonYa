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
# ---------------------------------------------------------
import Items
# ---------------------------------------------------------



# ---------------------------------------------------------
# Clase a usar
# ---------------------------------------------------------
class Form:
    # -----------------------------------------------------
    def __init__(self):
        # -------------------------------------------------
        # Inicialización de la clase Items y la ventana principal
        self.item = Items.Items()

        # Creación de la ventana principal, estableciendo título y tamaño
        # y evitando que se pueda redimensionar
        self.window = tk.Tk()
        self.window.title("Item Management")
        self.window.resizable(False, False)

        # Creación del cuaderno de pestañas
        self.notebook = ttk.Notebook(self.window)
        # -------------------------------------------------

        # -------------------------------------------------
        # Creación de las pestañas del cuaderno
        self.tab_new_item()
        self.tab_find_item()
        self.tab_all_items()
        # -------------------------------------------------

        # -------------------------------------------------
        # Posicionamiento del cuaderno en la ventana principal
        self.notebook.grid(column=0, row=0, padx=10, pady=10)

        # Mostrar la ventana principal
        # Esto inicia el bucle principal de la interfaz gráfica
        self.window.mainloop()

    # -----------------------------------------------------





    # -----------------------------------------------------
    def tab_new_item(self):
        # Creación de la pestaña para nuevos artículos
        self.page1 = ttk.Frame(self.notebook)
        self.notebook.add(self.page1, text=" New items ")

        # Creación del marco de etiqueta para el artículo
        self.label_frame1 = ttk.LabelFrame(self.page1, text="Item")
        self.label_frame1.grid(column=0, row=0, padx=5, pady=10)

        # Creación de la etiqueta y entrada para el nombre
        self.label = ttk.Label(self.label_frame1, text="Name:")
        self.label.grid(column=0, row=0, padx=4, pady=4)
        self.new_name = tk.StringVar()
        self.entry_new_name = ttk.Entry(self.label_frame1, textvariable=self.new_name)
        self.entry_new_name.grid(column=1, row=0, padx=4, pady=4)
        self.entry_new_name.focus()

        # Creación de la etiqueta y entrada para el precio
        self.label = ttk.Label(self.label_frame1, text="Price:")
        self.label.grid(column=0, row=1, padx=4, pady=4)
        self.new_price = tk.StringVar()
        self.entry_new_price = ttk.Entry(self.label_frame1, textvariable=self.new_price)
        self.entry_new_price.grid(column=1, row=1, padx=4, pady=4)

        # Creación del botón para confirmar la carga del artículo
        self.button = ttk.Button(self.label_frame1, text="Confirm", command=self.add_item)
        self.button.grid(column=1, row=2, padx=4, pady=4)

    # -----------------------------------------------------

    # -----------------------------------------------------
    def tab_find_item(self):
        # Creación de la pestaña para consultar artículos por código
        self.page2 = ttk.Frame(self.notebook)
        self.notebook.add(self.page2, text=" Consult by ID ")

        # Creación del marco de etiqueta para el artículo
        self.label_frame2 = ttk.LabelFrame(self.page2, text="Item")
        self.label_frame2.grid(column=0, row=0, padx=5, pady=10)

        # Creación de la etiqueta y entrada para el código
        self.label = ttk.Label(self.label_frame2, text="ID:")
        self.label.grid(column=0, row=0, padx=4, pady=4)
        self.id_find_item = tk.StringVar()
        self.entry_id_find_item = ttk.Entry(self.label_frame2, textvariable=self.id_find_item)
        self.entry_id_find_item.grid(column=1, row=0, padx=4, pady=4)

        # Creación de las etiquetas y entradas para el nombre y precio
        self.label = ttk.Label(self.label_frame2, text="Name:")
        self.label.grid(column=0, row=1, padx=4, pady=4)
        self.name_find_item = tk.StringVar()
        self.entry_name_find_item = ttk.Entry(self.label_frame2, textvariable=self.name_find_item, state="readonly")
        self.entry_name_find_item.grid(column=1, row=1, padx=4, pady=4)

        # Creación de la etiqueta y entrada para el precio
        self.label = ttk.Label(self.label_frame2, text="Price:")
        self.label.grid(column=0, row=2, padx=4, pady=4)
        self.price_find_item = tk.StringVar()
        self.entry_price_find_item = ttk.Entry(self.label_frame2, textvariable=self.price_find_item, state="readonly")
        self.entry_price_find_item.grid(column=1, row=2, padx=4, pady=4)

        # Creación del botón para consultar el artículo por código
        self.button = ttk.Button(self.label_frame2, text="Consult", command=self.consult)
        self.button.grid(column=1, row=3, padx=4, pady=4)

    # -----------------------------------------------------

    # -----------------------------------------------------
    def tab_all_items(self):
        # Creación de la pestaña para mostrar todos los artículos
        self.page3 = ttk.Frame(self.notebook)
        self.notebook.add(self.page3, text=" Full list ")

        # Creación del marco de etiqueta para los artículos
        self.label_frame3 = ttk.LabelFrame(self.page3, text="Items")
        self.label_frame3.grid(column=0, row=0, padx=5, pady=10)

        # Creación del área de texto para mostrar los artículos
        self.text_area = st.ScrolledText(self.label_frame3, width=40, height=10)
        self.text_area.grid(column=0, row=0, padx=4, pady=4)

        # Creación del botón para mostrar todos los artículos
        self.button = ttk.Button(self.label_frame3, text="Show full list", command=self.show_all_items)
        self.button.grid(column=0, row=1, padx=4, pady=4)

    # -----------------------------------------------------





    # -----------------------------------------------------
    def add_item(self):
        # Verifica que los campos no estén vacíos
        if not self.new_name.get() or not self.new_price.get():
            mb.showerror("Error", "Please fill in all fields")
            self.entry_new_name.focus()
            return 
        
        # Verifica que el precio sea un número válido
        try:
            float(self.new_price.get())
        except ValueError:
            mb.showerror("Error", "Price must be a valid number")
            self.entry_new_price.focus()
            return

        # Verifica que el nombre no exista ya en la base de datos
        all_items = self.item.get_all()
        for item in all_items:
            if item[1].lower() == self.new_name.get().lower():
                mb.showerror("Error", "Item already exists")
                self.entry_new_name.focus()
                return

        # Agrega el artículo a la base de datos
        self.item.add((self.new_name.get(), self.new_price.get()))
        mb.showinfo("Information", "Data has been loaded")
        self.new_name.set("")
        self.new_price.set("")
        self.entry_new_name.focus()

    # -----------------------------------------------------

    # -----------------------------------------------------
    def consult(self):
        # Consulta el artículo por ID
        response = self.item.get_id((self.id_find_item.get(),))
        if len(response) > 0:
            # Se encontró el artículo
            self.name_find_item.set(response[0][0])
            self.price_find_item.set(response[0][1])
        else:
            # No se encontró el artículo
            mb.showerror("Error", "Item not found")
            self.name_find_item.set("")
            self.price_find_item.set("")
        self.entry_id_find_item.focus()

    # -----------------------------------------------------

    # -----------------------------------------------------
    def show_all_items(self):
        # Limpia el área de texto antes de mostrar los artículos
        response = self.item.get_all()
        self.text_area.delete("1.0", tk.END)

        # Verifica si hay artículos para mostrar
        if len(response) == 0:
            mb.showinfo("Information", "No items found")
            return

        # Formatea y muestra los artículos en el área de texto
        lista = []
        for row in response:
            texto = "\n".join([
                "ID: " + str(row[0]),
                "Name: " + row[1],
                "Price: " + str(row[2])
            ])
            lista.append(texto)
        self.text_area.insert(tk.END, "\n\n".join(lista))

# ---------------------------------------------------------