import flet as ft

from funciones import crear_mascota


def mostrar_formulario_mascota(page: ft.Page, on_guardado):
    #Campos del formulario
    nombre = ft.TextField(
        label="Nombre"
    )

    especie = ft.TextField(
        label="Especie"
    )

    raza = ft.TextField(
        label="Raza"
    )

    edad = ft.TextField(
        label="Edad"
    )

    cliente_id = ft.TextField(
        label="ID del Cliente"
    )

    #metodo para guardar los datos del cliente

    def guardar(e):
        nombre_mascota = nombre.value
        especie_mascota = especie.value
        raza_mascota = raza.value
        edad_mascota = edad.value
        cliente_id_mascota = cliente_id.value

        crear_mascota(
            nombre_mascota,
            especie_mascota,
            raza_mascota,
            edad_mascota,
            cliente_id_mascota
        )
        mensaje.value = "Mascota registrada correctamente."
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
            "Nueva mascota",
            size=24,
            weight=ft.FontWeight.BOLD
        ),

        nombre,
        especie,
        raza,
        edad,
        cliente_id,
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



