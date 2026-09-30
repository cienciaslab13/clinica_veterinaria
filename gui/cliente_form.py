import flet as ft

from funciones import crear_cliente


def mostrar_formulario_cliente(page: ft.Page, on_guardado):
    #Campos del formulario
    nombre = ft.TextField(
        label="Nombre"
    )

    telefono = ft.TextField(
        label="Teléfono"
    )

    correo = ft.TextField(
        label="Correo"
    )

    #metodo para guardar los datos del cliente

    def guardar(e):
        nombre_cliente = nombre.value
        telefono_cliente = telefono.value
        correo_cliente = correo.value

        crear_cliente(
            nombre_cliente,
            telefono_cliente,
            correo_cliente
        )
        mensaje.value = "Cliente registrado correctamente."
        mensaje.color = ft.Colors.GREEN
        page.update()
        on_guardado()

    mensaje = ft.Text()
    #Boton guardar
    boton_guardar = ft.Button(
    "Guardar",
    icon=ft.Icons.SAVE,
    on_click=guardar
    )

    #Boton cerrar
    boton_cerrar = ft.Button(
        "Cerrar",
        icon=ft.Icons.CLOSE,
        on_click=lambda e: page.pop_dialog()
    )

    return ft.Column(
    controls=[
        ft.Text(
            "Nuevo cliente",
            size=24,
            weight=ft.FontWeight.BOLD
        ),

        nombre,
        telefono,
        correo,
        mensaje,
        ft.Row(
            controls=[
                        boton_guardar,
                        boton_cerrar
            ], spacing=10
        )
    ],
    spacing=15
    )



