import flet as ft
from gui.cliente_form import mostrar_formulario_cliente

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
    def actualizar_clientes():
        clientes = listar_clientes()
        tabla.rows.clear()
        for cliente in clientes:
            tabla.rows.append(
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(cliente.nombre)),
                        ft.DataCell(ft.Text(cliente.telefono)),
                        ft.DataCell(ft.Text(cliente.correo))
                    ]
                )
            )
        page.update()

    #Metodo para abrir el formulario de nuevo cliente
    def abrir_formulario(e):
        formulario = mostrar_formulario_cliente(
            page,
            actualizar_clientes
        )
        dialogo = ft.AlertDialog(
            modal=True,
            title=ft.Text("Nuevo cliente"),
            content=formulario
        )
        page.show_dialog(dialogo)
        #page.update()


    boton_nuevo = ft.Button(
    "Nuevo cliente",
    icon=ft.Icons.ADD,
     on_click=abrir_formulario
    )   



    return ft.Column(
        controls=[
            ft.Text(
                "Clientes",
                size=28,
                weight=ft.FontWeight.BOLD
            ),
           # boton_nuevo,
            tabla
        ]
    )

