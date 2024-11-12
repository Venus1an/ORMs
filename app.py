from flaskr import create_app
from flaskr.modelos.modelos import Cliente, Rol, Categoria, Subcategoria, Proveedor, Producto, Venta, Factura, Detalle_Venta_Productos, Tabla_de_Pagos, Empleado, Empresas_Proveedoras
from flaskr.modelos.modelos import db


app = create_app('default')
app_context = app.app_context()
app_context.push()
db.init_app(app)
db.create_all()


with app.app_context():
    empl = Empleado(nombre='Nubia Arias', contrasena= '12345')
    cat = Categoria (nombre= 'Manos', subcategoria_id= '1' )
    subcat = Subcategoria (nombre = 'uñas')
    ven = Venta (fecha = '28-10-1999', total = 552820, empleado_id = 5)
    prod = Producto (nombre = 'Esmalte rojo', precio_venta= 8000, iva = 0.19, precio_bruto= 4000, marca = 'masglo', cantidad = 2000, empleado_id = 5)

    cat.subcategoria_id.append(subcat)
    empl.producto.append(prod)
    empl.venta.append(ven)
    db.session.add(cat)
    db.session.add(ven)
    db.session.commit()
    print(Subcategoria.query.all())
    print(Producto.query.all())
    print(Empleado.query.all().nombre)
    db.session.delete(subcat)
    db.session.delete(cat)
    print(Subcategoria.query.all())
    print ()