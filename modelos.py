from marshmallow import fields
from flask_sqlalchemy import SQLAlchemy
import enum

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()



class Rol(db.Model): #db.model es una clase base de SQLAlchemy al utilizarla con Flask
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(180))
   
    Usuario = db.relationship('Usuario', back_populates= "Rol")
    

class Usuario(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))
    contraseña = db.Column(db.String(250))
    cedula = db.Column(db.String(250))
    correo = db.Column(db.String(250))
    telefono = db.Column(db.Integer)
    fechaContratoInicio = db.Column(db.String(8))
    rol = db.Column(db.Integer, db.ForeignKey("Rol.id"))
    
    Rol = db.relationship('Rol', back_populates= "Usuario")
    


class Categoria(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))
    descripcion = db.Column(db.String(250))
    
    Subcategoria = db.relationship('Subcategoria', back_populates= "Categoria")

    

class Subcategoria(db.Model):
   
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))
    descripcion = db.Column(db.String(250))
    categoria =  db.Column(db.Integer, db.ForeignKey("Categoria.id"))

    Categoria = db.relationship('Categoria', back_populates= "Subcategoria")
    Producto= db.relationship('Producto', back_populates='Subcategoria')



class Proveedor(db.Model):
    
    
    id = db.Column(db.Integer, primary_key=True)
    nombreProv = db.Column(db.String(180))
    apellidoProv = db.Column(db.String(180))
    cedula = db.Column(db.String(180))
    telefonoProv = db.Column(db.String(180))
    direccionProv = db.Column(db.String(180))
    
    Producto = db.relationship('Producto', back_populates= "Proveedor")
    fechaRegistroProd= db.relationship('fechaRegistroProd', back_populates = "Proveedor")

class Producto(db.Model):
    

    id = db.Column(db.Integer, primary_key=True)
    nombreProd = db.Column(db.String(250))
    medidaProd = db.Column(db.Integer)
    unidadMedidaProd = db.Column(db.String(250))
    precioBrutoProd = db.Column(db.Float)
    precioNetoProd = db.Column(db.Float)
    ivaProd = db.Column(db.Float)
    porcentajeGanancia = db.Column(db.Float)
    unidadesTotalesProd = db.Column(db.Integer)
    estadoProd = db.Column(db.String(250))
    marcaProd = db.Column(db.String(250))
    proveedor = db.Column(db.Integer, db.ForeignKey("Proveedor.id"))
    subcategoria = db.Column(db.Integer, db.ForeignKey("Subcategoria.id"))
    
    Proveedor = db.relationship('Proveedor', back_populates='Producto')
    Subcategoria = db.relationship('Subcategoria', back_populates='Producto')
    DetalleVenta= db.relationship('detalleVenta', back_populates = "Producto")
    fechaRegistroProd= db.relationship('fechaRegistroProd', back_populates = "Producto")



class Venta(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    fechaVenta = db.Column(db.DateTime)
    totalVenta = db.Column(db.Float)
    MetodoPago = db.Column(db.String(250))
    usuario= db.Column(db.Integer, db.ForeignKey("Usuario.id"))
 
    Usuario= db.relationship('Usuario', back_populates= 'Venta')
    DetalleVenta= db.relationship('detalleVenta', back_populates = "Venta")


class Factura(db.Model):

    id = db.Column(db. Integer, primary_key= True)
    fechaGeneracionFactura = db.Column (db.DateTime)
    impuestosFactura = db.Column (db.Numeric(19,0))
    
    DetalleVenta= db.relationship('detalleVenta', back_populates = "Factura")



class detalleVenta(db.Model):
    
    id = db. Column(db.Integer, primary_key=True)
    cantidad = db.Column(db.Integer)
    precioUnidad = db.Column(db.Float)
    cedula = db.Column(db.String(180))
    direccion = db.Column(db.String(180))
    telefono = db.Column(db.String(180))
    venta = db.Column(db.Integer, db.ForeignKey("Venta.id"))
    producto = db.Column(db.Integer, db.ForeignKey("Producto.id"))
    factura = db.Column(db.Integer, db.ForeignKey("Factura.id"))
    
    Factura= db.relationship('Factura', back_populates = "detalleVenta")
    Producto= db.relationship('Producto', back_populates = "detalleVenta")
    Venta= db.relationship('Venta', back_populates = "detalleVenta")

    
class fechaRegistroProd(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    fechaRegistro = db.Column(db.DateTime)
    cantidad = db.Column(db.Integer)
    proveedor = db.Column(db.Integer, db.ForeignKey("Proveedor.id"))
    producto = db.Column(db.Integer, db.ForeignKey("Producto.id"))

    Producto= db.relationship('Producto', back_populates = "fechaRegistroProd")
    Proveedor= db.relationship('Proveedor', back_populates = "fechaRegistroProd")
    

