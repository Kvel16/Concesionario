from django.db import models

class Empleado(models.Model):
    id_empleado = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    fecha_inicio = models.DateField(null=True)

class asesorComercial(models.Model):
    id_asesor = models.CharField(max_length=10, primary_key=True)
    salario = models.CharField(max_length=10)
    empleado = models.OneToOneField(Empleado, on_delete=models.CASCADE)

class Cliente(models.Model):
    nombre = models.CharField(max_length=200)
    telefono = models.CharField(max_length=10)
    correo = models.CharField(max_length=250)
    direccion = models.CharField(max_length=200)
    id_cliente = models.CharField(max_length=20, primary_key=True)

class vehiculoCliente(models.Model):
    modelo = models.CharField(max_length=4)
    color = models.CharField(max_length=15)
    placa = models.CharField(max_length=6, primary_key=True)
    VIN = models.CharField(max_length=12)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class Sucursal(models.Model):
    cod_sucursal = models.CharField(max_length=2, primary_key=True)
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=20)

class jefeTaller(models.Model):
    nombre = models.CharField(max_length=40)
    correo = models.CharField(max_length=40)
    telefono = models.CharField(max_length=10)
    id_jefetaller = models.CharField(max_length=10, primary_key=True)
    cod_sucursal = models.CharField(max_length=10)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    empleado = models.OneToOneField(Empleado, on_delete=models.CASCADE)

class ordenReparacion(models.Model):
    numero_orden = models.CharField(max_length=10)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    placa = models.CharField(max_length=6)
    trabajos = models.CharField(max_length=700)
    jefetaller = models.ForeignKey(jefeTaller, on_delete=models.CASCADE)

class Gerente(models.Model):
    id_gerente = models.CharField(max_length=10, primary_key=True)
    nombre = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    correo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)

class Repuestos(models.Model):
    referencia_repuesto = models.CharField(max_length=12, primary_key=True)
    cantidad = models.CharField(max_length=8)
    precioUnitario = models.CharField(max_length=8)
    precioTotal = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)

class vehiculoNuevo(models.Model):
    VIN = models.CharField(max_length=10, primary_key=True)
    color = models.CharField(max_length=15)
    modelo = models.CharField(max_length=4)
    linea = models.CharField(max_length=15)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)

class Cotizacion(models.Model):
    id_cotizacion = models.AutoField(primary_key=True)
    fecha_cotizacion = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    referencia_repuesto = models.ForeignKey(Repuestos, on_delete=models.CASCADE, null=True)
    VIN = models.ForeignKey(vehiculoNuevo, on_delete=models.CASCADE)
    cod_sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    numero_cotizacion = models.IntegerField()
    descripcion = models.CharField(max_length=300)
