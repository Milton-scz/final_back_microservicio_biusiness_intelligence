get_All_alquileres = '''
query { 
getAlquilers {
    alquilerId
    fechaInicio
    fechaFin
    monto
    descripcion
    activo {
         _id
        nombre
        descripcion
        fechaAdquisicion
        precio
        estado
              categoria {
                _id
                nombre
                descripcion
              }
    }
    cliente{
      clienteId
      nombre
      cedula
      celular
      fechaNacimiento
      direccion
    }
    }
}
'''
