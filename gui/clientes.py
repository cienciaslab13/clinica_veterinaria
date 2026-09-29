import flet as ft

from funciones import listar_clientes


def mostrar_clientes(page: ft.Page):

    clientes = listar_clientes()

    tabla = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Nombre")),
            ft.DataColumn(ft.Text("Teléfono")),
            ft.DataColumn(ft.Text("Correo"))
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(cliente.nombre)),
                    ft.DataCell(ft.Text(cliente.telefono)),
                    ft.DataCell(ft.Text(cliente.correo))
                ]
            ) for cliente in clientes
        ]
    )



    return ft.Column(
        controls=[
            ft.Text(
                "Clientes",
                size=28,
                weight=ft.FontWeight.BOLD
            ),
            tabla
        ]
    )

