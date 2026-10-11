from datos import clientes, mascotas, veterinarios, citas
from entidades import Cliente, Mascota, Veterinario, Cita


# =========================
# CLIENTES
# =========================

def crear_cliente(nombre_cliente, telefono_cliente, correo_cliente):

    id_cliente = len(clientes) + 1

    cliente = Cliente(
        id=id_cliente,
        nombre=nombre_cliente,
        telefono=telefono_cliente,
        correo=correo_cliente
    )

    clientes.append(cliente)


def listar_clientes():
    return clientes


def buscar_cliente(id_cliente):
    for cliente in clientes:
        if cliente.id == id_cliente:
            return cliente
    return None


def actualizar_cliente(id_cliente, nombre, telefono, correo):
    cliente = buscar_cliente(id_cliente)

    if cliente:
        cliente.nombre = nombre
        cliente.telefono = telefono
        cliente.correo = correo
        return True

    return False


def eliminar_cliente(id_cliente):
    cliente = buscar_cliente(id_cliente)

    if cliente:
        clientes.remove(cliente)
        return True

    return False


# =========================
# MASCOTAS
# =========================

def crear_mascota(
    nombre,
    especie,
    raza,
    edad,
    cliente_id
):

    id_mascota = len(mascotas) + 1

    mascota = Mascota(
        id=id_mascota,
        nombre=nombre,
        especie=especie,
        raza=raza,
        edad=edad,
        cliente_id=cliente_id
    )

    mascotas.append(mascota)



def listar_mascotas():
    return mascotas


def buscar_mascota(id_mascota):
    for mascota in mascotas:
        if mascota.id == id_mascota:
            return mascota
    return None


def actualizar_mascota(id_mascota, nombre, especie, raza, edad, cliente_id):
    mascota = buscar_mascota(id_mascota)

    if mascota:
        mascota.nombre = nombre
        mascota.especie = especie
        mascota.raza = raza
        mascota.edad = edad
       # mascota.cliente_id = cliente_id
        return True

    return False


def eliminar_mascota(id_mascota):
    mascota = buscar_mascota(id_mascota)

    if mascota:
        mascotas.remove(mascota)
        return True

    return False


# =========================
# VETERINARIOS
# =========================

def crear_veterinario(veterinario):
    veterinarios.append(veterinario)


def listar_veterinarios():
    return veterinarios


def buscar_veterinario(id_veterinario):
    for veterinario in veterinarios:
        if veterinario.id == id_veterinario:
            return veterinario
    return None


def actualizar_veterinario(id_veterinario, nombre, especialidad, telefono):
    veterinario = buscar_veterinario(id_veterinario)

    if veterinario:
        veterinario.nombre = nombre
        veterinario.especialidad = especialidad
        veterinario.telefono = telefono
        return True

    return False


def eliminar_veterinario(id_veterinario):
    veterinario = buscar_veterinario(id_veterinario)

    if veterinario:
        veterinarios.remove(veterinario)
        return True

    return False


# =========================
# CITAS
# =========================

def crear_cita(cita):
    citas.append(cita)


def listar_citas():
    return citas


def buscar_cita(id_cita):
    for cita in citas:
        if cita.id == id_cita:
            return cita
    return None


def actualizar_cita(id_cita, mascota_id, veterinario_id, fecha, motivo):
    cita = buscar_cita(id_cita)

    if cita:
        cita.mascota_id = mascota_id
        cita.veterinario_id = veterinario_id
        cita.fecha = fecha
        cita.motivo = motivo
        return True

    return False


def eliminar_cita(id_cita):
    cita = buscar_cita(id_cita)

    if cita:
        citas.remove(cita)
        return True

    return False

from datos import usuarios
def listar_usuarios():
    return usuarios

#Para buscar un usuario podemos crear:
def buscar_usuario(usuario, contraseña):

    for u in usuarios:
        if u.usuario == usuario and u.contraseña == contraseña:
            return u

    return None


