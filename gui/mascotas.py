import flet as ft

from funciones import listar_mascotas, buscar_cliente


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
    

    return ft.Column(
        controls=[
            
            ft.Text(
                "Mascotas",
                size=28,
                weight=ft.FontWeight.BOLD
            ),
            tabla
        ]
    )
