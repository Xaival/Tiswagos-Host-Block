# Aviso
**¡¡¡El archivo de Python directamente no funcionará!!!**

Para poder editar el archivo hosts es necesario ejecutar como administrador, por lo que es necesario convertir en un ejecutable antes de poder usarlo.

**Tampoco funcionara en sistemas de 32 bits**

<br>

# Tiswagos Host Block
Aplicación para añadir una lista de páginas para bloquear usando el archivo Host.

Puedes ver la lista de URLs bloqueadas [aquí](https://tiswagos-liri.tumblr.com/antispam).

![Logo](https://user-images.githubusercontent.com/54257745/181864346-d2715ceb-4c08-46c9-96c0-7c0503160c47.png)

![Muestra](https://user-images.githubusercontent.com/54257745/181864001-b310e047-cad4-4537-ab2e-f42390131494.png)

<br><br>

# Hacer ejecutable
## Imágenes
Antes de convertirlo en ejecutable hay que tener en cuenta que los archivos como el logo deben de estar dentro del ejecutable.

`os.path.dirname(__file__)+"\datos\logo.ico"`

<br>

## Ejecutable
El ejecutable se ha creado a partir del archivo de Python usando https://github.com/Xaival/Interfaz-PyInstaller

![Config EXE](https://user-images.githubusercontent.com/54257745/181864945-8af20248-f276-4a77-a7e9-4d20c040d1a7.png)
