
class PersonaUcc: 
    def __init__(self, nombre, cedula, direccion, fechaNacimiento):
        self.Nombre = nombre
        self.Cedula = cedula
        self.Direccion = direccion
        self.FechaNacimiento = fechaNacimiento

    def calcularEdad():
        pass

class Estudiantes(PersonaUcc):

    Beca = bool;
    def __init__(self, nombre, cedula, direccion, fecha_nacimiento, carrera, semestre, promedio_notas, beca):
        super().__init__(nombre, cedula, direccion, fecha_nacimiento)
        self.Carrera = carrera
        self.Semestre = semestre
        self.Promedio_notas = promedio_notas
        self.Beca = beca

    def matricularMaterias():
        pass

    def generarMatricula():
        pass
    def __str__(self):
        return f"Estudiante: nombre: {self.Nombre} cedula: {self.Cedula} direccion: {self.Direccion} fecha de nacimiento: {self.FechaNacimiento} carrera: {self.Carrera} semestre: {self.Semestre} promedio: {self.Promedio_notas} beca: {self.Beca}"

class Profesores(PersonaUcc):
    def __init__(self, nombre, cedula, direccion, fecha_nacimiento, profesion, salario, eps):
        super().__init__(nombre, cedula, direccion, fecha_nacimiento)
        self.Profesion = profesion
        self.Salario = salario
        self.Eps = eps

    def asignarMaterias():
        pass

    def generarCertificadoLaboral():
        pass
    
    def __str__(self):
        return f"Profesor: nombre: {self.Nombre} cedula: {self.Cedula} direccion: {self.Direccion} fecha de nacimiento: {self.FechaNacimiento} profesion: {self.Profesion} salario: {self.Salario} eps: {self.Eps}"
    

class Administrativo(PersonaUcc):
    def __init__(self, nombre, cedula, direccion, fecha_nacimiento, profesion, cargo, dependencia, salario):
        super().__init__(nombre, cedula, direccion, fecha_nacimiento)
        self.Profesion = profesion
        self.Cargo = cargo
        self.Dependencia = dependencia
        self.Salario = salario

    def renovarContrato():
        pass

    def calculoNomina():
        pass

    def liquidacionVacaciones():
        pass

    def __str__(self):
        return f"Admistrativo: nombre: {self.Nombre} cedula: {self.Cedula} direccion: {self.Direccion} fecha de nacimiento: {self.FechaNacimiento} profesion: {self.Profesion} cargo: {self.Cargo} dependencia: {self.Dependencia} salario: {self.Salario}"
    

print()
estudiante = Estudiantes("sebas","1231231232","calle 2", "01/12/23","ingenieria",5,3,False)
print(estudiante)
print()
profesor = Profesores("juan","10292928","calle 5","20/20/20","maestro",3000000,"sanitas")
print(profesor)
print()
administrativo = Administrativo("William","1085301221","calle 321","11/11/11","Ingeniero de software","jefe","ninguna",10000000)
print(administrativo)