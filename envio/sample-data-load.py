from envio.models import Centro

centros = [  
    Centro(100, 'Facultad de Ciencias','Z'),
    Centro(101, 'Facultad de Economía y Empresa', 'Z'),
    Centro(102, 'Facultad de Derecho', 'Z'),
    Centro(109, 'Facultad de Economía y Empresa', 'Z'),
    Centro(110, 'Escuela de Ingeniería y Arquitectura', 'Z'),
    Centro(228, 'Facultad de Empresa y Gestión Pública', 'Z'),
    Centro(175, 'Escuela Universitaria Politécnica de la Almunia','A'),
    Centro(302, 'Facultad de Ciencias Sociales y Humanas', 'Z'),
    Centro(326, 'Escuela Universitaria Politécnica de Teruel', 'T'),
]

for c in centros:
    c.save()