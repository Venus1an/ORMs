
from marshmallow import fields
from flask_sqlalchemy import SQLAlchemy
import enum

from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

db = SQLAlchemy()

class Empresas_Proveedoras(db.Model):
    

    Id_Empresas_proveedoras = db.Column(db.Integer, primary_key=True) 
    Nombre = db.Column(db.String(255)) 
    Encargado_Despacho = db.Column(db.String(100))
    Telefono_Empresa = db.Column(db.String(15))  
    Direccion_Empresa = db.Column(db.String(50)) 

    Proveedor_Empresas_Proveedoras = db.relationship('Proveedor', back_populates="Empresas_Proveedoras")

class Cliente(db.Model):
    

    Id_Cliente = db.Column(db.Integer, primary_key=True)
    Nombres_Cliente = db.Column(db.String(250))
    Apellidos_Cliente = db.Column(db.String(250))
    Cedula = db.Column(db.String(250))
    Telefono = db.Column(db.String(15))  
    Direccion = db.Column(db.String(50))

    Detalle_Venta_Productos_Cliente = db.relationship('Detalle_Venta_Productos', back_populates="Cliente")

class Rol(db.Model):
    
    

    Id_Rol = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(180))
    Descripcion = db.Column(db.String(120))
   
    Empleado_Rol = db.relationship('Empleado', back_populates="Rol")

class Empleado(db.Model):
    
    

    Id_Empleado = db.Column(db.Integer, primary_key=True)
    Nombres = db.Column(db.String(250))
    Apellidos = db.Column(db.String(250))
    Cedula = db.Column(db.String(250))
    Correo_Electronico = db.Column(db.String(250))
    Telefono = db.Column(db.String(15))  # Cambiado de Integer a String para telefonos
    Fecha_Contrato_Inicio = db.Column(db.DateTime)
    Fecha_Contrato_Finalizado = db.Column(db.DateTime)
    FK_Id_rol = db.Column(db.Integer, db.ForeignKey("rol.Id_Rol"))
    
    Rol = db.relationship('Rol', back_populates="Empleado_Rol")
    Venta_Empleado = db.relationship('Venta', back_populates='Empleado')

class Categoria(db.Model):
    
    

    Id_Categoria = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(250))
    Descripcion = db.Column(db.String(250))
    
    Subcategoria_Categoria = db.relationship('Subcategoria', back_populates="Categoria")

class Subcategoria(db.Model):
    
    

    Id_Subcategoria = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(250))
    Descripcion = db.Column(db.String(250))
    FK_Id_Categoria = db.Column(db.Integer, db.ForeignKey("Categoria.Id_Categoria"))

    Categoria = db.relationship('Categoria', back_populates="Subcategoria_Categoria")
    Producto = db.relationship('Producto', back_populates='Subcategoria')

class Proveedor(db.Model):
    
    

    Id_Proveedor = db.Column(db.Integer, primary_key=True)
    Nombre_Prov = db.Column(db.String(180))
    Apellido_Prov = db.Column(db.String(180))
    Cedula = db.Column(db.String(180))
    Telefono_Prov = db.Column(db.String(15))  
    Direccion_Prov = db.Column(db.String(50))
    FK_Id_Empresas_Proveedoras = db.Column(db.Integer, db.ForeignKey("Empresas_Proveedoras.Id_Empresas_Proveedoras"))
    
    Empresas_Proveedoras = db.relationship('Empresas_Proveedoras', back_populates="Proveedor_Empresas_Proveedoras")

class Producto(db.Model):
    

    Id_Producto = db.Column(db.Integer, primary_key=True, nullable=False)
    Nombre_Prod = db.Column(db.String(250))
    Medida_Prod = db.Column(db.Integer)
    Unidad_Medida_Prod = db.Column(db.String(80))
    Precio_Unidad_Prod = db.Column(db.Float)
    Costo_Prod = db.Column(db.Float)
    Iva_Prod = db.Column(db.Float)
    Porcentaje_Ganancia = db.Column(db.Float)
    Unidades_Totales_Prod = db.Column(db.Integer)
    Estado = db.Column(db.String(80))
    Marca_Prod = db.Column(db.String(80))
    FK_Id_Proveedor = db.Column(db.Integer, db.ForeignKey("Proveedor.Id_Proveedor"))
    FK_Id_Subcategoria = db.Column(db.Integer, db.ForeignKey("Subcategoria.Id_Subcategoria"))
    
    Proveedor = db.relationship('Proveedor', back_populates='Producto')
    Subcategoria = db.relationship('Subcategoria', back_populates='Producto')
    Detalle_Venta_Productos = db.relationship('Detalle_Venta_Productos', back_populates="Producto")

class Venta(db.Model):
    __tablename__ = 'venta'

    Id_Venta = db.Column(db.Integer, primary_key=True)
    Fecha_Venta = db.Column(db.DateTime)
    Total_Venta = db.Column(db.Float)
    FK_Id_Empleado = db.Column(db.Integer, db.ForeignKey("Empleado.Id_Empleado"))
 
    Empleado = db.relationship('Empleado', back_populates='Venta_Empleado')
    Tabla_de_Pagos = db.relationship('Tabla_de_Pagos', back_populates='Venta')   
    Detalle_Venta_Productos = db.relationship('Detalle_Venta_Productos', back_populates="Venta")

class Tabla_de_Pagos(db.Model):
    

    Id_Pagos = db.Column(db.Integer, primary_key=True, nullable=False)
    Metodos_de_Pago = db.Column(db.String(80))
    Total_a_Pagar = db.Column(db.Float)
    Fecha_De_Pago = db.Column(db.DateTime)
    Estado_Pago = db.Column(db.String(80))
    FK_Id_Venta = db.Column(db.Integer, db.ForeignKey("Venta.Id_Venta"))

    Venta = db.relationship('Venta', back_populates='Tabla_de_Pagos')

class Factura(db.Model):
    

    Id_Factura = db.Column(db.Integer, primary_key=True)
    Fecha_Generacion_Factura = db.Column(db.DateTime)
    Impuestos_Factura = db.Column(db.Float)
    FK_Id_Tabla_de_Pagos = db.Column(db.Integer, db.ForeignKey("Tabla_de_Pagos.Id_Pagos"))
    
    Tabla_de_Pagos = db.relationship('Tabla_de_Pagos', back_populates="Factura")

class Detalle_Venta_Productos(db.Model):
    

    Id_Detalle_Venta_Producto = db.Column(db.Integer, primary_key=True, nullable=False)
    Cantidad = db.Column(db.Integer)
    Precio_unidad = db.Column(db.Float)
    FK_Id_Venta = db.Column(db.Integer, db.ForeignKey("Venta.Id_Venta"))
    FK_Id_Producto = db.Column(db.Integer, db.ForeignKey("Producto.Id_Producto"))
    FK_Id_Cliente = db.Column(db.Integer, db.ForeignKey("Cliente.Id_Cliente"))
    
    Cliente = db.relationship('Cliente', back_populates="Detalle_Venta_Productos_Cliente")
    Producto = db.relationship('Producto', back_populates="Detalle_Venta_Productos")
    Venta = db.relationship('Venta', back_populates="Detalle_Venta_Productos")


    

    

