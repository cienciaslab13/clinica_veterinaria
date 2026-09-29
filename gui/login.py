import flet as ft


def mostrar_login(page: ft.Page):

    usuario = ft.TextField(
        label="Usuario"
    )

    contraseña = ft.TextField(
        label="Contraseña",
        password=True
    )

    boton = ft.Button(
        "Ingresar"
    )

    return ft.Column(
        controls=[
            ft.Text(                                                                                                                                                 
                "Iniciar sesión",
                size=28,
                weight=ft.FontWeight.BOLD
            ),
            usuario,
            contraseña,
            boton
        ]
    )
