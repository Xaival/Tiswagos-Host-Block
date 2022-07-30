# Tiswagos Host Block
Plantilla para creación minimalista.

![Logo](https://user-images.githubusercontent.com/54257745/181864346-d2715ceb-4c08-46c9-96c0-7c0503160c47.png)

![Muestra](https://user-images.githubusercontent.com/54257745/181864001-b310e047-cad4-4537-ab2e-f42390131494.png)


# Aviso
**¡¡¡El archivo de Python directamente no funcionará!!!**

No se puede ejecutar como administrador el archivo de python por lo que es necesario hacer un ejecutable.

Para que funcione es necesario convertirlo en un ejecutable con permisos de administrador.
Antes de convertirlo en ejecutable hay que tener en cuenta que los archivos deben de estar
en una carpeta llamada datos y en el programa se debe declarar con la siguiente forma.
`os.path.dirname(__file__)+"\datos\logo.ico"`

El ejecutable se ha creado a partir del archivo de Python usando https://github.com/Xaival/Interfaz-PyInstaller
