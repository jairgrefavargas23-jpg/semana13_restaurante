# restaurante_app — Semana 13

> Proyecto de **Bryan Jair Grefa Alvarado**, para la asignatura de Programación
> Orientada a Objetos (Universidad Estatal Amazónica). Esta entrega corresponde
> a la Semana 13: *Conceptos fundamentales de interfaces gráficas de usuario*.

---

> El restaurante **El Fogón** organiza su personal por turnos (mañana, tarde y
> noche) y su menú por tipo de plato. Hasta ahora, todo el sistema funcionaba
> por consola. Esta semana se da el primer paso hacia una interfaz gráfica
> construida con **Tkinter**, siguiendo la misma estructura simplificada que
> el proyecto docente *Biblioteca App*, pero adaptada al dominio del
> restaurante.

## Alcance de esta entrega

No se trasladan todavía todas las funciones desarrolladas en semanas
anteriores. Se trabaja únicamente con dos piezas de información:

- **Productos** del menú, con su categoría y valor calórico aproximado.
- **Personal**, identificado por turno, que también sirve para simular el
  acceso al sistema mediante usuario y contraseña.

El resto de funcionalidades (ventas, gestión de turnos) se incorporará en
próximas semanas.

## Diagrama de evolución

```
                ANTES                              AHORA
   Personal -> CLI -> Servicios          Personal -> GUI -> Eventos
                 -> Modelos -> JSON                    -> Servicios
                                                        -> Modelos -> JSON
```

## Estructura del proyecto

```
restaurante_app/
├── datos/
│   ├── productos.json
│   └── usuarios.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── main.py
└── README.md
```

## Qué hace cada capa

> `modelos/` — define `Producto` (con categoría y calorías) y `Usuario` (con
> turno de trabajo), ambos con validaciones mediante `property`.
>
> `servicios/archivo_servicio.py` — lee y escribe los archivos JSON de
> `datos/`, sin conocer reglas del negocio.
>
> `servicios/restaurante_servicio.py` — convierte los datos JSON en objetos,
> valida el acceso del personal y responde a las consultas que necesita la
> interfaz.
>
> `ui/` — `LoginView` y `MainView`, construidas con Tkinter; solicitan la
> información a `RestauranteServicio` en lugar de leer los JSON directamente.
>
> `main.py` — crea la única ventana principal y controla el cambio entre
> vistas.

## Flujo de la aplicación

```
Inicio -> LoginView -> RestauranteServicio valida el acceso -> MainView
MainView -> Productos | Personal | Turnos (pendiente) | Ventas (pendiente)
MainView -> Cerrar sesion -> LoginView
```

El cambio entre vistas ocurre dentro de la misma ventana, sin crear ventanas
adicionales ni más de un `mainloop()`.

## Credenciales de acceso (demostración)

| Usuario | Contraseña |
|---|---|
| `bgrefa` | `fogon2026` |
| `admin` | `admin987` |

> La contraseña debe combinar al menos una letra y un número, según la
> validación definida en el modelo `Usuario`.

## Cómo ejecutar

```bash
cd restaurante_app
python main.py
```

Requiere Python 3.10 o superior, con Tkinter disponible en la instalación.

## Pruebas realizadas

> Se ejecutó `main.py` y la aplicación abrió sin errores, mostrando primero
> `LoginView`. Se probaron campos vacíos y credenciales incorrectas,
> confirmando que ambos casos muestran un mensaje de error visual sin cerrar
> la aplicación. Con credenciales válidas se desplegó `MainView` dentro de la
> misma ventana. La opción **Productos** mostró el menú cargado desde
> `productos.json`, incluyendo las calorías por porción. La opción
> **Personal** mostró la información cargada desde `usuarios.json`,
> incluyendo el turno asignado a cada persona. Finalmente, **Cerrar sesión**
> devolvió correctamente a `LoginView` sin abrir una ventana adicional.

## Nota educativa sobre autenticación

El acceso implementado en esta etapa es una simulación con fines académicos.
Las contraseñas se guardan en JSON sin cifrado; esto no sería adecuado para
un sistema real.
