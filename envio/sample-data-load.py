from envio.models import Centro, Estudio, Plan

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

estudios = [
	Estudio(134, 'Graduado en Finanzas y Contabilidad', 5),
	Estudio(157, 'Graduado en Estudios en Arquitectura', 5),
	Estudio(148, 'Graduado en Ingeniería Informática', 5),
]

for e in estudios:
    e.save()


planes = [
	Plan(pid=449, curso='2018', estudio=Estudio.objects.get(eid=134), centro=Centro.objects.get(cid=109)),
	Plan(pid=470, curso='2018', estudio=Estudio.objects.get(eid=157), centro=Centro.objects.get(cid=110)),
	Plan(pid=439, curso='2018', estudio=Estudio.objects.get(eid=148), centro=Centro.objects.get(cid=110)),
	Plan(pid=443, curso='2018', estudio=Estudio.objects.get(eid=148), centro=Centro.objects.get(cid=326)),
]

for p in planes:
    p.save()