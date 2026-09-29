from dataclasses import dataclass


@dataclass
class Cliente:
    id: int
    nombre: str
    telefono: str
    correo: str


@dataclass
class Mascota:
    id: int
    nombre: str
    especie: str
    raza: str
    edad: int
    cliente_id: int


@dataclass
class Veterinario:
    id: int
    nombre: str
    especialidad: str
    telefono: str


@dataclass
class Cita:
    id: int
    mascota_id: int
    veterinario_id: int
    fecha: str
    motivo: str

@dataclass
class Usuario:
    id: int
    nombre: str
    usuario: str
    contraseña: str
    rol: str
