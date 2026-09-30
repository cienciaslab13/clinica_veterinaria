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
            ft.DataColumn(ft.Text("Dueño"))
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(mascota.nombre)),
                    ft.DataCell(ft.Text(mascota.especie)),
                    ft.DataCell(ft.Text(mascota.raza)),
                    ft.DataCell(ft.Text(str(mascota.edad))),
                    ft.DataCell(ft.Text(buscar_cliente(mascota.cliente_id).nombre if buscar_cliente(mascota.cliente_id) else "Desconocido"))
                ]
            ) for mascota in mascotas
        ]
    )

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
                        ft.DataCell(ft.Text(buscar_cliente(mascota.cliente_id).nombre if buscar_cliente(mascota.cliente_id) else "Desconocido"))
                    ]
                )
            )
        page.update()

    #Metodo para abrir el formulario de nueva mascota
    def abrir_formulario(e):
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
