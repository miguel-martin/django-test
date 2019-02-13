from envio.models import Centro, Estudio, Plan, Persona, Matricula, Entrega, Departamento

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



departamentos = [
Departamento(1, 'Análisis Económico'),
Departamento(2, 'Anatomía e Histología Humanas'),
Departamento(3, 'Anatomía Patológica, Medicina Legal y Forense y Toxicología'),
Departamento(4, 'Anatomía, Embriología y Genética Animal'),
Departamento(5, 'Bioquímica y Biología Molecular y Celular'),
Departamento(6, 'Ciencia y Tecnología de Materiales y Fluidos'),
Departamento(7, 'Ciencias Agrarias y del Medio Natural'),
Departamento(8, 'Ciencias de la Antigüedad'),
Departamento(9, 'Ciencias de la Documentación e Historia de la Ciencia'),
Departamento(10, 'Ciencias de la Educación'),
Departamento(11, 'Ciencias de la Tierra'),
Departamento(12, 'Cirugía, Ginecología y Obstetricia'),
Departamento(13, 'Contabilidad y Finanzas'),
Departamento(14, 'Derecho de la Empresa'),
Departamento(15, 'Derecho Penal, Filosofía del Derecho e Historia del Derecho'),
Departamento(16, 'Derecho Privado'),
Departamento(17, 'Derecho Público'),
Departamento(18, 'Didáctica de las Ciencias Experimentales'),
Departamento(19, 'Didáctica de las Lenguas y de las Ciencias Humanas y Sociales'),
Departamento(20, 'Dirección de Marketing e Investigación de Mercados'),
Departamento(21, 'Dirección y Organización de Empresas'),
Departamento(22, 'Estructura e Historia Económica y Economía Pública'),
Departamento(23, 'Expresión Musical, Plástica y Corporal'),
Departamento(24, 'Farmacología y Fisiología'),
Departamento(25, 'Filología Española'),
Departamento(26, 'Filología Francesa'),
Departamento(27, 'Filología Inglesa y Alemana'),
Departamento(28, 'Filosofía'),
Departamento(29, 'Fisiatría y Enfermería'),
Departamento(30, 'Fisica Aplicada'),
Departamento(31, 'Física de la Materia Condensada'),
Departamento(32, 'Física Teórica'),
Departamento(33, 'Geografía y Ordenación del Territorio'),
Departamento(34, 'Historia del Arte'),
Departamento(35, 'Historia Medieval, Ciencias y Técnicas Historiográficas y Estudios Árabes e Islámicos'),
Departamento(36, 'Historia Moderna y Contemporánea'),
Departamento(37, 'Informática e Ingeniería de Sistemas'),
Departamento(38, 'Ingeniería de Diseño y Fabricación'),
Departamento(39, 'Ingeniería Eléctrica'),
Departamento(40, 'Ingeniería Electrónica y Comunicaciones'),
Departamento(41, 'Ingeniería Mecánica'),
Departamento(42, 'Ingeniería Química y Tecnologías del Medio Ambiente'),
Departamento(43, 'Lingüística General e Hispánica'),
Departamento(44, 'Matemática Aplicada'),
Departamento(45, 'Matemáticas'),
Departamento(46, 'Medicina, Psiquiatría y Dermatología'),
Departamento(47, 'Métodos Estadísticos'),
Departamento(48, 'Microbiología, Medicina Preventiva y Salud Pública'),
Departamento(49, 'Patología Animal'),
Departamento(50, 'Pediatría, Radiología y Medicina Física'),
Departamento(51, 'Producción Animal y Ciencia de los Alimentos'),
Departamento(52, 'Psicología y Sociología'),
Departamento(53, 'Química Analítica'),
Departamento(54, 'Química Física'),
Departamento(55, 'Química Inorgánica'),
Departamento(56, 'Química Orgánica'),
Departamento(57, 'Unidad Predepartamental de Arquitectura'),
]

for d in departamentos:
    d.save()