# Tercera preentrega Proyecto Django - Web intemedia

El proyecto de web intermedia incluye las funcionalidades para registrar rubros, articulos, clientes y proveedores asi como realizar la busqueda de articulos por codigo en la pantalla principal.

# Pasos para ejecutar:
1. Clona el repositorio en la terminal de tu maquina local: 
git clone https://github.com/VirginiaVega/Tercera-pre-entrega-Vega-Virginia.git

2. Instala las dependencias del proyecto: 
pip install –r requirements.txt 

3. Activa el entorno virtual: 
source venv1/Scripts/activate

4. Inicia el servidor:
python manage.py runserver

5. Accede desde el navegador al inicio del proyecto:
http://localhost:8000/inicio/

# Funcionalidades:

1. Pagina de inicio / Buscar articulos por codigo:
- URL /inicio/ O haciendo click en "inicio" en la barra de navegacion
- Descripcion: Es la pagina principal del proyecto donde se visualiza un titulo y debajo se puede buscar articulos por codigo. Por ejemplo puede buscar el codido C201 para ver debajo en una tabla el articulo "Agua mineral" con su respectivo precio y codigo previamente ingresado.

2. Registro de articulos:
- URL /art/ O haciendo click en "Articulos" en la barra de navegacion
- Descripcion: En esta pagina se puede realizar el registro de articulos, ingresando un codigo en formato texto, una descripcion en formato texto y un precio en formato decimal. Es obligatorio completar todos los campos y presionar el boton "Enviar" para realizar el registro del articulo. Podes realizar el registro de un articulo y luego buscarlo en la pagina de inicio, para comprobar que se creo exitosamente.

3. Registro de rubros:
- URL /rub/ O haciendo click en "Rubros" en la barra de navegacion
- Descripcion: En esta pagina se puede realizar el registro de rubros, ingresando un codigo en formato texto y una descripcion en el mismo formato. Es obligatorio completar todos los campos y presionar el boton "Enviar" para realizar el registro del rubro.

4. Registro de clientes:
- URL /cli/ O haciendo click en "Clientes" en la barra de navegacion
- Descripcion: En esta pagina se puede realizar el registro de clientes, ingresando un nombre en formato texto, un email en formato Email, un telefono y una direccion en formato texto. Es obligatorio completar todos los campos y presionar el boton "Enviar" para realizar el registro del cleinte.

5. Registro de proveedores:
- URL /prov/ O haciendo click en "Proveedores" en la barra de navegacion
- Descripcion: En esta pagina se puede realizar el registro de proveedores, ingresando un nombre en formato texto, un email en formato Email, un telefono y una direccion en formato texto. Es obligatorio completar todos los campos y presionar el boton "Enviar" para realizar el registro del proveedor.

# Acceso al panel de administracion:
Inicia sesion con tu usuario para acceder al panel de administracion de Django y ver la base de datos:
Accede desde el navegador al login de administracion: http://localhost:8000/admin/
- Nombre de usuario: usuario1
- Contraseña: coderhouse


