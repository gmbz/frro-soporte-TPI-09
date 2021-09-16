# NOMBRE_DEL_PROYECTO

Este es un archivo que debe completarse con los datos utilizados en el TPI. Este archivo puede modificarse en el tiempo, no obstante siempre debe mantenerse en un estado consistente con el desarrollo.

**Importante:** Este archivo debe mantenerse en formato Markdown (.md) y sólo se tendrá en cuenta la versión disponible en GIT.

## Descripción del proyecto

En este proyecto se llevará a cabo el desarrollo de una aplicacion web que corresponde a una red social de películas, donde los usuarios podrán acceder a la información de la película que desee y comentarla y calificarla.

## Modelo de Dominio

![Modelo de dominio](img/modelo-de-dominio.png)

## Bosquejo de Arquitectura

Definir la arquitectura del sistema y como interactuan sus diferentes componentes. Utilizar el Paquete **Office** de Draw.io o similar. [Ejemplo Online]().

## Requerimientos

Definir los requerimientos del sistema.

|REQ|Descripción|
|:---:|:---|
|01|Registrar nuevo usuario|
|02|Autenticar usuario|
|03|Registrar nuevo comentario|
|04|Eliminar comentario|
|05|Mostrar lista películas populares|
|06|Agregar película a lista Mis Favoritos|
|07|Buscar pelicula por nombre|
|08|Cambiar imagen de perfil de usuario|
|09|Valorar comentario de otro usuario (upvote o downvote)|
|10|Mostrar informacion de película|
|11|Mostrar últimos estrenos|
|12|Mostrar tendencias|
|13|Crear listas personalizadas|
|14|Mostrar información de actores/productores|
|15|Mostrar películas filtradas por año de estreno|
|16|Mostrar películas filtradas por género|

### Funcionales

Listado y descripción breve de los requerimientos funcionales.

### No Funcionales

Listado y descripción breve de los requerimientos no funcionales. Utilizar las categorias dadas:

### Portability

**Obligatorios**

- El sistema debe funcionar correctamente en múltiples navegadores (Sólo Web).
- El sistema debe ejecutarse desde un único archivo .py llamado app.py (Sólo Escritorio).

### Security

**Obligatorios**

- Todas las contraseñas deben guardarse con encriptado criptográfico (SHA o equivalente).
- Todas los Tokens / API Keys o similares no deben exponerse de manera pública.

### Maintainability

**Obligatorios**

- El sistema debe diseñarse con la arquitectura en 3 capas. (Ver [checklist_capas.md](checklist_capas.md))
- El sistema debe utilizar control de versiones mediante GIT.
- El sistema debe estar programado en Python 3.8 o superior.

### Reliability

### Scalability

**Obligatorios**

- El sistema debe funcionar desde una ventana normal y una de incógnito de manera independiente (Sólo Web).
  - Aclaración: No se debe guardar el usuario en una variable local, deben usarse Tokens, Cookies o similares.

### Performance

**Obligatorios**

- El sistema debe funcionar en un equipo hogareño estándar.

### Reusability

### Flexibility

**Obligatorios**

- El sistema debe utilizar una base de datos SQL o NoSQL

## Stack Tecnológico

Definir que tecnologías se van a utilizar en cada capa y una breve descripción sobre por qué se escogió esa tecnologia.

### Capa de Datos

- SQLITE3
- SQLALCHEMY 1.4.7

Se utilizó una base de datos sqlite3 y como ORM se utilizó sqlalchemy para manejar la base de datos debido a las facilidades que nos brinda esta herramienta y otro motivo fue para aprender nuevas tecnologías.

### Capa de Negocio

Para obtener la información de las películas, consumimos la API de TMDB, la cual es una API pública. Para realizar las consultas se necesita una "api key", la cual solicitamos y utilizamos
Api key: 25398bd0f8e1460f3769b59bfbf5eea6

### Capa de Presentación

- Flask.
- HTML5.
- BOOTSTRAP4.
- CSS3.

Optamos por la utilización de Flask para la capa de presentación debido a nuestra falta de experiencia con python necesitabamos un framework con una curva de aprendizaje baja. También, gracias a que Flask utiliza Jinja2 para el manejo de datos en las plantillas HTML, nos facilita mostrar la información en la web.
Al ser inexpertos en el frontend, creemos que lo mejor es utilizar clases bootrstrap para la estética de la web y refinar cosas puntuales con nuestro escaso conocimiento de css.