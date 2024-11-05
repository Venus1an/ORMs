from flask import Flask
from flask_migrate import Migrate
from flask_migrate import SQLAlchemy  # => ORM

app = Flask(__name__)  # instancia de flask

# configuración de la base de datos
USER_DB = 'root'
PASS_DB = ''
URL_DB = 'localhost'
NAME_DB = 'bella_y_actual'
FULL_URL_DB = f'mysql+pymysql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQL_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# migracion de datos
migrate = Migrate()
migrate.init_app(app, db)

class Rol(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(180))
    Usuario = db.Column(db.Integer, db.ForeignKey("Usuario"))

class Empleado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(250))
    cedula = db.Column(db.String(250))
    correo = db.Column(db.String(250))
    contraseña = db.Column(db.String(250))
    telefono = db.Column(db.String(250))

    def __init__(self, id, nombre, apellido, correo):
        self.id = id
        self.nombre = nombre

class Empleado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(250))
    cedula = db.Column(db.String(250))
    correo = db.Column(db.String(250))
    contraseña = db.Column(db.String(250))
    telefono = db.Column(db.String(250))

    def __init__(self, id, nombre, apellido, correo):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo

    def json(self):  # enviar datos en formato API
        return {'id': self.id, 'nombre': self.nombre, 'apellido': self.apellido, 'correo': self.correo}

    def __str__(self):  # el objeto se debe representar como cadena de texto
        return str(self.__class__) + ":" + str(self.__dict__)

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))
    precio_venta = db.Column(db.Float)
    iva = db.Column(db.Float)
    precio_bruto = db.Column(db.Float)
    marca = db.Column(db.String(250))
    cantidad = db.Column(db.Integer)
    empleado_id = db.Column(db.Integer, db.ForeignKey("Empleado.id"))

    Empleado = db.relationship('Empleado')

    def __init__(self, id, nombre, precio_venta, iva, precio_bruto, marca, cantidad, empleado_id):
        self.id = id
        self.nombre = nombre
        self.precio_venta = precio_venta
        self.iva = iva
        self.precio_bruto = precio_bruto
        self.marca = marca
        self.cantidad = cantidad
        self.empleado_id = empleado_id

class Producto(db.Model):
    Empleado = db.relationship('Empleado')

    def __init__(self, id, nombre, precio_venta, iva, precio_bruto, marca, cantidad, empleado_id):
        self.id = id
        self.nombre = nombre
        self.precio_venta = precio_venta
        self.iva = iva
        self.precio_bruto = precio_bruto
        self.marca = marca
        self.cantidad = cantidad
        self.empleado_id = empleado_id

    def json(self):  # enviar datos en formato API
        return {'id': self.id, 'nombre': self.nombre, 'precio_venta': self.precio_venta, 'iva': self.iva, 'precio_bruto': self.precio_bruto, 'cantidad': self.cantidad}

class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))
    Subcategoria = db.Column(db.Integer, db.ForeignKey("Subcategoria.id"))

    def __init__(self, id, nombre, subcategoria):
        self.id = id
        self.nombre = nombre
        self.Subcategoria = subcategoria

class Subcategoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))

class Venta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.String(250))
    total = db.Column(db.Float)
    Empleado = db.Column(db.Integer, db.ForeignKey("Empleado.id"))

class Proveedor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(180))
    telefono = db.Column(db.String(180))
    Empresa_Proveedora = db.Column(db.Integer, db.ForeignKey("Empresa_Proveedora.id"))

class Empresa_Proveedora(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))
    direccion = db.Column(db.String(180))

class Cliente(db.Model):
    
    id = db. Column(db. Integer, primary_key=True)
    Nombre = db.Column(db.String(250))
    Cedula=db.Column(db.String(180))
    telefono = db.Column(db.String(180))

class Factura(db.Model):

    id = db.Column(db. Integer, primary_key= True)
    fecha = db.Column (db.Date)
    Empleado = db.Column (db. Integer, db.ForeignKey("Empleado. id"))
    Producto = db. Producto (db. Integer, db.ForeignKey("Producto.id"))


class Usuario (db.Mode1):
    id = db.Column(db. Integer, primary_key = True)
    nombre = db.Column(db. String (180))


class Tabla_de_pagos (db. Model) :

    id = db.Column (db. Integer, primary_key = True)
    Metodos_de_Pago = db. Column(db.String(250))
    Total_a_Pagar = db.Column(db.String(250) )
    Fecha_de_Pago = db.Column(db.String(250) )
    Estado_de_Pago = db.Column(db.String(250))
    Id_Venta = db.Column(db. Integer, db.ForeignKey ("Venta.id"))