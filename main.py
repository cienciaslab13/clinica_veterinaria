import flet as ft

from gui.dashboard import mostrar_dashboard
from gui.clientes import mostrar_clientes
from gui.mascotas import mostrar_mascotas


def main(page: ft.Page):

    page.title = "Clínica Veterinaria"

    contenido = ft.Container()

    #Cambio de pantalla al seleccionar una opción en la barra de navegación
    def cambiar_pantalla(e):

        if e.control.selected_index == 0:
            contenido.content = mostrar_dashboard(page)

        elif e.control.selected_index == 1:
            contenido.content = mostrar_clientes(page)

        elif e.control.selected_index == 2:
            contenido.content = mostrar_mascotas(page)

        page.update()

    # Configuración de la barra de navegación
    navigation_bar = ft.NavigationBar(
        selected_index=0,
        on_change=cambiar_pantalla,
        destinations=[
            ft.NavigationBarDestination(
                icon=ft.Icons.HOME,
                label="Inicio"
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.PERSON,
                label="Clientes"
            ),
            ft.NavigationBarDestination(
                icon=ft.Icons.PETS,
                label="Mascotas"
            )
        ]
    )

    contenido.content = mostrar_dashboard(page)

    page.add(
        navigation_bar,
        contenido
        
    )


ft.run(main)
