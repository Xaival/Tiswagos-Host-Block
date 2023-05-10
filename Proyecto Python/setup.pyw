# Para Importar todas las clases de Tkinter
from tkinter import *
from tkinter import messagebox # Importar de cuadros de alerta

import os # Directorio y cosas del sistema
from io import open # Importar librería io
from requests import get # Importar librería de requests
import time # Importar librería para fecha

root = Tk() # Crear la variable ventana
root.title("Tiswagos Host Block") # Título de la ventana
root.iconbitmap(os.path.dirname(__file__)+"\datos\logo.ico") # Mostrar icono
root.config(bg="black", pady=20, padx=20) # Poner fondo negro
root.resizable(False, False) # No permite cambiar el alto y ancho

# Posicionar en el centro de la pantalla
AnchoVentana = 400 # Ancho ventana
AltoVentana = 175 # Alto ventana
PosX = root.winfo_screenwidth() // 2 - AnchoVentana // 2 # Calcular posición horizontal
PosY = root.winfo_screenheight() // 2 - AltoVentana # Calcular posición vertical

root.geometry(str(AnchoVentana)+ "x" +str(AltoVentana)+ "+" +str(PosX)+ "+" +str(PosY)) # Tamaño de ventana y posición inicial


# Funciones-------------------------------------------------------------------


#Ruta del host
rutaHosts=os.getenv('SystemRoot')+r"\System32\drivers\etc\hosts"


# Chequear el estado del archivo host
def CheckEstado():
    # Verificar que exista el archivo y que se tengan permisos de lectura
    if (os.access(rutaHosts,os.F_OK) and os.access(rutaHosts,os.R_OK)):

        # Extraer contenido del archivo
        hosts = open(rutaHosts,"r") #(R - Modo lectura)
        Lineas=hosts.readlines() # Guardar línea a línea
        hosts.close # Cerrar el archivo de texto

        # Estado de host
        EstadoBool=False

        for Linea in Lineas:
            # Si la línea contiene #AntiSpam Actualizado el
            if "#AntiSpam Actualizado el " in Linea:
                EstadoBool=True

                try: Estado.set(Linea.replace('#AntiSpam ', '').replace('\n', '')) # Mostrar línea
                except: Estado.set("Activado") # Mostrar línea
                
                icon.itemconfig(circle, fill='#16842a') # Cambiar icono
                break # Crerrar bucle
        
        # Si no contiene ninguna línea
        if not EstadoBool:
            Estado.set("Desactivado") # Mostrar línea
            icon.itemconfig(circle, fill='#fa6969') # Cambiar icono


# Funciones de los botones
def Desactive(): # Quita la lista de dominios
    try: # En caso de errores
        # Verificar que exista el archivo
        if (os.access(rutaHosts,os.F_OK)):
            # Verifica que se tengan permisos de escritura
            if(os.access(rutaHosts,os.W_OK)):

                # Extraer contenido del archivo
                hosts = open(rutaHosts,"r") #(R - Modo lectura)
                Lineas=hosts.readlines() # Guardar línea a línea
                hosts.close # Cerrar el archivo de texto


                # Quitar las líneas que contengan #AntiSpam
                NuevoTexto=""
                SaltoLinea=0
                
                for Linea in Lineas:
                    # Para quitar más de 2 saltos de líneas seguidos
                    if "\n" == Linea: SaltoLinea+=1
                    else: SaltoLinea=0

                    # Guardar líneas que cumplan las condiciones
                    if not "#AntiSpam" in Linea and 2 >= SaltoLinea:
                        NuevoTexto+=Linea

                # Reescribir archivo con NuevoTexto
                hosts = open(rutaHosts,"w") #(W - Modo escritura)
                hosts.write(NuevoTexto) # Añadir texto al archivo
                hosts.close # Cerrar el archivo de texto
        
    # Mensajes de errores
            else: messagebox.showerror(title="Error", message="No se ha podido acceder al archivo hosts.")
        else: messagebox.showerror(title="Error", message="El archivo hosts no está donde se suponía.")
    except: messagebox.showerror(title="Error", message="Se ha producido dado un error inesperado.")
    
    # Actualizar estado
    CheckEstado()


def Active(): # Quita y añade la lista de dominios
    try: # En caso de errores
        # Verificar que exista el archivo
        if (os.access(rutaHosts,os.F_OK)):
            # Verifica que se tengan permisos de escritura
            if(os.access(rutaHosts,os.W_OK)):

                # Extraer contenido del archivo
                hosts = open(rutaHosts,"r") #(R - Modo lectura)
                Lineas=hosts.readlines() # Guardar línea a línea
                hosts.close # Cerrar el archivo de texto


                # Quitar las líneas que contengan #AntiSpam
                NuevoTexto=""
                SaltoLinea=0
                
                for Linea in Lineas:
                    # Para quitar más de 2 saltos de líneas seguidos
                    if "\n" == Linea: SaltoLinea+=1
                    else: SaltoLinea=0

                    # Guardar líneas que cumplan las condiciones
                    if not "#AntiSpam" in Linea and 2 >= SaltoLinea:
                        NuevoTexto+=Linea


                # Agregar 2 nuevas líneas vacías
                NuevoTexto+="\n\n"
                
                # Agregar Fecha
                NuevoTexto+="#AntiSpam Actualizado el "+time.strftime('%Y-%m-%d %H:%M', time.localtime())+"\n"

                # Datos condicionales
                Referencia="#REF!"
                Intentos=0
                # Bucle que reintente 10 veces o hasta que conecte correctamente con la base de datos
                while Referencia=="#REF!" and Intentos<10:
                    # Extraer IPs de JSON
                    ListaJSON = get("https://raw.githubusercontent.com/Xaival/JSON/main/Tiswagos/Webs_Direccion.json").json()["values"]
                    
                    Referencia=ListaJSON[0]["Direccion"] # Guardar resultado de referencia
                    Intentos+=1 # Contar veces que se ha reintentado

                # Si al final no hay un fallo con la referencia
                if Referencia!="#REF!":

                    # Añadir IPs a NuevoTexto
                    for Linea in ListaJSON:
                        NuevoTexto+=Linea["Direccion"]+"\n"

                    # Reescribir archivo con NuevoTexto
                    hosts = open(rutaHosts,"w") #(W - Modo escritura)
                    hosts.write(NuevoTexto) # Añadir texto al archivo
                    hosts.close # Cerrar el archivo de texto
            
    # Mensajes de errores
                else: messagebox.showerror(title="Error", message="No se ha podido conectar a la base de datos.")
            else: messagebox.showerror(title="Error", message="No se ha podido acceder al archivo hosts.")
        else: messagebox.showerror(title="Error", message="El archivo hosts no está donde se suponía.")
    except: messagebox.showerror(title="Error", message="Se ha producido dado un error inesperado.")
    
    # Actualizar estado
    CheckEstado()


# Funciones-------------------------------------------------------------------
# Contenido-------------------------------------------------------------------


# Frame
ContDinamic=Frame(root, bg="black", pady=25, padx=30) # Declarar y configurar
ContDinamic.grid(row="0", column="0", columnspan="2",  sticky="nswe") # Mostrar
# Icono
icon=Canvas(ContDinamic, width=30, height=30, bg='black', highlightbackground='black') # Declarar y configurar
circle=icon.create_oval(4, 1, 30, 28, fill='#fa6969')
icon.grid(row="0", column="0", sticky="nse") # Mostrar
# Texto
Estado=StringVar(value="Desactivado")
text=Label(ContDinamic, textvariable=Estado, bg="black", fg="white", font=("Roboto", 12, "bold")) # Declarar y configurar
text.grid(row="0", column="1", sticky="nsw", padx=5) # Mostrar


# Botón
miButton=Button(root, text="Actualizar", font=("Roboto", 10, "bold"), pady=5, padx=5, bg="black", fg="white", command=Active) # Declarar y configurar
miButton.grid(row="1", column="0", sticky="nswe", pady=10, padx=10) # Mostrar
# Botón
miButton2=Button(root, text="Desactivar", font=("Roboto", 10, "bold"), pady=5, padx=5, bg="black", fg="white", command=Desactive) # Declarar y configurar
miButton2.grid(row="1", column="1", sticky="nswe", pady=10, padx=10) # Mostrar

# Configuración de columnas
root.columnconfigure(0, weight=True)
root.columnconfigure(1, weight=True)


# Contenido-------------------------------------------------------------------
# Funciones al iniciarse------------------------------------------------------

CheckEstado()

# Funciones al iniciarse------------------------------------------------------

root.mainloop() # Abrir ventana
