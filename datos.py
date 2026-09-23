from entidades import Cliente, Mascota, Veterinario, Cita


clientes = [
    Cliente(1, "Roberto Solís", "8888-1111", "roberto@gmail.com"),
    Cliente(2, "María López", "8888-2222", "maria@gmail.com"),
]


mascotas = [
    Mascota(1, "Max", "Perro", "Labrador", 4, 1),
    Mascota(2, "Michi", "Gato", "Siamés", 2, 2),
]


veterinarios = [
    Veterinario(1, "Dra. Ana Martínez", "Medicina general", "8888-3333"),
    Veterinario(2, "Dr. Carlos Pérez", "Cirugía veterinaria", "8888-4444"),
]


citas = [
    Cita(1, 1, 1, "2026-09-25", "Consulta general"),
    Cita(2, 2, 2, "2026-09-26", "Vacunación"),
]