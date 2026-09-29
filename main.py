import flet as ft

from gui.dashboard import mostrar_dashboard
from gui.clientes import mostrar_clientes
from gui.mascotas import mostrar_mascotas
from gui.login import mostrar_login


def main(page: ft.Page):

    page.title = "Clínica Veterinaria"
    page.padding = 0

    # -------------------------------------------------
    # CONTENEDOR PRINCIPAL
    # -------------------------------------------------

    contenido = ft.Container(
        expand=True
    )

    # -------------------------------------------------
    # CAMBIO DE PANTALLAS DEL SISTEMA
    # -------------------------------------------------

    def cambiar_pantalla(e):

        if e.control.selected_index == 0:

            contenido.content = mostrar_dashboard(page)

        elif e.control.selected_index == 1:

            contenido.content = mostrar_clientes(page)

        elif e.control.selected_index == 2:

            contenido.content = mostrar_mascotas(page)

        page.update()

    # -------------------------------------------------
    # BARRA DE NAVEGACIÓN
    # -------------------------------------------------

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

    # -------------------------------------------------
    # MOSTRAR SISTEMA DESPUÉS DEL LOGIN
    # -------------------------------------------------

    def mostrar_sistema(usuario):

        contenido.content = mostrar_dashboard(page)

        page.controls.clear()

        page.add(
            contenido,
            navigation_bar
        )

        page.update()

        print(
            f"Usuario autenticado: "
            f"{usuario.nombre} - {usuario.rol}"
        )

    # -------------------------------------------------
    # MOSTRAR LOGIN AL INICIAR
    # -------------------------------------------------

    login = mostrar_login(
        page,
        mostrar_sistema
    )

    page.add(login)


# -----------------------------------------------------
# EJECUTAR APLICACIÓN
# -----------------------------------------------------

ft.run(main)

