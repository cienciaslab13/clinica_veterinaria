import flet as ft
from funciones import listar_clientes, listar_mascotas


def mostrar_dashboard(page: ft.Page):

    titulo = ft.Text(
        value="Clínica Veterinaria",
        size=30,
        weight=ft.FontWeight.BOLD
    )

    descripcion = ft.Text(
        value="Sistema de gestión de la clínica veterinaria",
        size=16
    )

    total_clientes = len(listar_clientes())
    total_mascotas = len(listar_mascotas())

   
    estadisticas = ft.Row(
        controls=[
            ft.Text("Clientes: " + str(total_clientes)), 
            ft.Text("Mascotas: " + str(total_mascotas))],
        alignment=ft.MainAxisAlignment.SPACE_EVENLY
    )
    return ft.Column(
        controls=[
            titulo,
            descripcion,
            estadisticas
           ]
    )