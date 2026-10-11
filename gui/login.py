import flet as ft

from funciones import buscar_usuario


def mostrar_login(page: ft.Page, on_login_success):
    intentos = 0

    usuario = ft.TextField(
        label="Usuario",
        width=300,
        autofocus=True
    )

    contraseña = ft.TextField(
        label="Contraseña",
        password=True,
        can_reveal_password=True,
        width=300
    )

    mensaje = ft.Text(
        color=ft.Colors.RED
    )

    def ingresar(e):
        nonlocal intentos

        usuario_encontrado = buscar_usuario(
            usuario.value,
            contraseña.value
        )

        if usuario_encontrado:

            if usuario_encontrado.rol == "Administrador":
                mensaje.value = ""

                # Avisamos a main.py que el login fue correcto
                on_login_success(usuario_encontrado)

            else:
                mensaje.value = (
                    "El usuario no tiene permisos de administrador."
                )

        else:
            intentos += 1

            if intentos >= 3:
                mensaje.value = (
                    "Ha superado el número de intentos permitidos."
                )

                boton.disabled = True
                usuario.disabled = True
                contraseña.disabled = True

            else:
                mensaje.value = (
                    f"Credenciales no válidas. "
                    f"Intento {intentos} de 3."
                )

        page.update()

    boton = ft.Button(
        content="Ingresar",
        icon=ft.Icons.LOGIN,
        on_click=ingresar
    )

    return ft.Container(
            # Imagen de fondo principal
            image=ft.DecorationImage(
                src="https://picsum.photos/1200/1300",
                fit=ft.BoxFit.COVER
            ),
            alignment=ft.Alignment.CENTER,
            expand=True,
            # Contenedor interno estilo "tarjeta" semitransparente para el formulario
            content=ft.Container(
                bgcolor=ft.Colors.with_opacity(0.8, ft.Colors.WHITE),
                border_radius=ft.BorderRadius.all(10),
                padding=30,  # Espacio interno para que no quede pegado a los bordes
                content=ft.Column(
                    controls=[
                        ft.Icon(
                            icon=ft.Icons.PETS,
                            size=60,
                            color=ft.Colors.BLUE
                        ),
                        ft.Text(
                            "Clínica Veterinaria",
                            size=28,
                            weight=ft.FontWeight.BOLD
                        ),
                        ft.Text(
                            "Iniciar sesión",
                            size=20
                        ),
                        usuario,
                        contraseña,
                        boton,
                        mensaje
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=15,
                    tight=True  # Ajusta el tamaño de la columna al contenido de sus hijos
                )
            )
        )
