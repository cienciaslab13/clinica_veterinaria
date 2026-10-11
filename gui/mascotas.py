import flet as ft

from funciones import listar_mascotas, buscar_cliente
from gui.mascota_form import mostrar_formulario_mascota


def mostrar_mascotas(page: ft.Page):

    mascotas = listar_mascotas()

    filas = []

    tabla = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Especie")),
            ft.DataColumn(ft.Text("Raza")),
            ft.DataColumn(ft.Text("Edad")),
            ft.DataColumn(ft.Text("Dueño")),
            ft.DataColumn(ft.Text("Acciones"))

        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(mascota.nombre)),
                    ft.DataCell(ft.Text(mascota.especie)),
                    ft.DataCell(ft.Text(mascota.raza)),
                    ft.DataCell(ft.Text(str(mascota.edad))),
                    ft.DataCell(ft.Text(buscar_cliente(mascota.cliente_id).nombre if buscar_cliente(mascota.cliente_id) else "Desconocido")),
                    ft.DataCell(ft.Row(
                        controls=[
                            ft.IconButton(icon=ft.Icons.EDIT, on_click=lambda e, mascota=mascota: abrir_formulario(e, mascota)), 
                            ft.IconButton(icon=ft.Icons.DELETE, bgcolor=ft.Colors.RED, on_click=lambda e, id_mascota=mascota.id: eliminar_mascota(e, id_mascota))]))
                ]
            ) for mascota in mascotas
        ]
    )

    def eliminar_mascota(e, id_mascota):
        from funciones import eliminar_mascota
        #Mostrar mensaj e de confirmacion antes de eliminar
        dialogo_confirmacion = ft.AlertDialog(
            modal=True,
            title=ft.Text("Confirmar eliminación"),
            content=ft.Text("¿Estás seguro de que deseas eliminar esta mascota?"),
            actions=[
                ft.TextButton("Cancelar", on_click=lambda e: page.pop_dialog()),
                ft.TextButton("Eliminar", on_click=lambda e: [page.pop_dialog(), eliminar_mascota(id_mascota), actualizar_mascotas()])
            ]
        )
        page.show_dialog(dialogo_confirmacion)

    def actualizar_mascotas():
        mascotas = listar_mascotas()
        tabla.rows.clear()
        for mascota in mascotas:
            tabla.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(mascota.nombre)),
                        ft.DataCell(ft.Text(mascota.especie)),
                        ft.DataCell(ft.Text(mascota.raza)),
                        ft.DataCell(ft.Text(str(mascota.edad))),
                        ft.DataCell(ft.Text(buscar_cliente(mascota.cliente_id).nombre if buscar_cliente(mascota.cliente_id) else "Desconocido")),
                        ft.DataCell(ft.Row(
                            controls=[
                                ft.IconButton(icon=ft.Icons.EDIT, on_click=lambda e, mascota=mascota: abrir_formulario(e, mascota)), 
                                ft.IconButton(icon=ft.Icons.DELETE, bgcolor=ft.Colors.RED, on_click=lambda e, id_mascota=mascota.id: eliminar_mascota(e, id_mascota))]
                        ))
                    ]
                )
            )
        page.update()

    #Metodo para abrir el formulario de nueva mascota
    def abrir_formulario(e, mascota=None):
        if mascota:
            formulario = mostrar_formulario_mascota(
                page,
                actualizar_mascotas,
                mascota
            )
            dialogo = ft.AlertDialog(
                modal=True,
                title=ft.Text("Editar mascota"),
                content=formulario
            )
        else:
            formulario = mostrar_formulario_mascota(
                page,
                actualizar_mascotas
            )
            dialogo = ft.AlertDialog(
                modal=True,
                title=ft.Text("Nueva mascota"),
                content=formulario
            )
        page.show_dialog(dialogo)
        #page.update()


    boton_nuevo = ft.Button(
    "Nueva mascota",
    icon=ft.Icons.ADD,
     on_click=abrir_formulario
    ) 
    

    return ft.Column(
        controls=[
            
            ft.Text(
                "Mascotas",
                size=28,
                weight=ft.FontWeight.BOLD
            ),
            boton_nuevo,
            tabla
        ]
    )
