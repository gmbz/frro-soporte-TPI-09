# Checklist Sobre Buenas Prácticas Desarrollando en Python

El siguiente checklist permite una fácil detección de malas prácticas y posibles correcciones.

## General

- [x] Se respecta la convención de nombres típica de Python (PascalCase para clases, snake_case en todo lo demás).
- [ ] **No** se utilizan variables globales.
- [x] Se respeta el formato estandar de Python PEP8 mediante la aplicación Flake8.
- [x] Todo dato sensible debe guardarse de manera segura (en un hash o similar).

## Web

- [x] Utiliza errores HTTP (403, 404, etc).
- [x] Es multiusuario (puede usarse desde una ventana común y una de incógnito de manera independiente).


## Opcional

- [ ] Utilizar un Framework de Front-End (Vue, React, Angular).
- [ ] Incorporar soporte para múltiples idiomas (L10N y/o I18N).
- [ ] Utilizar Test Unitarios (Pytest).
- [ ] Incorporar Autorización (Roles).
- [ ] El sitio debe ser Responsive o Adaptative (verse bien en dispositivos móviles).