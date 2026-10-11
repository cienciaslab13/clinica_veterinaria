import flet as ft

from funciones import crear_mascota, buscar_cliente


def mostrar_formulario_mascota(page: ft.Page, on_guardado, mascota=None):
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

    if mascota:
        nombre.value = mascota.nombre
        especie.value = mascota.especie
        raza.value = mascota.raza
        edad.value = str(mascota.edad)
        cliente_id.value = buscar_cliente(mascota.cliente_id).nombre

    #metodo para guardar los datos del cliente

    def guardar(e):
        nombre_mascota = nombre.value
        especie_mascota = especie.value
        raza_mascota = raza.value
        edad_mascota = edad.value
        cliente_id_mascota = cliente_id.value

        if mascota:
            # Actualizar mascota existente
            from funciones import actualizar_mascota
            actualizar_mascota(
                mascota.id,
                nombre_mascota,
                especie_mascota,
                raza_mascota,
                edad_mascota,
                cliente_id_mascota
            )
            mensaje.value = "Mascota actualizada correctamente."
        else:
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



