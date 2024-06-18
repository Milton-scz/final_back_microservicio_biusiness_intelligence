from datetime import datetime
def clasificar_activos(alquileres):
    activos_fijos = {}
    for alquiler in alquileres:
        activo = alquiler["activo"]
        categoria_nombre = activo["categoria"]["nombre"]
        if categoria_nombre not in activos_fijos:
            activos_fijos[categoria_nombre] = 0
        activos_fijos[categoria_nombre] += 1
    return activos_fijos


def is_numerical(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def calcular_total_ingresos(alquileres):
    total = 0.0
    for alquiler in alquileres:
        monto = alquiler.get("monto")
        if is_numerical(monto):
            total += float(monto)
    return total

def calcular_ingresos_por_mes(alquileres):
    ingresos_por_mes = {}
    for alquiler in alquileres:
        fecha_inicio = datetime.strptime(alquiler["fechaInicio"], "%Y-%m-%d")
        mes_inicio = fecha_inicio.strftime("%Y-%m")
        monto = alquiler.get("monto")
        if is_numerical(monto):
            if mes_inicio not in ingresos_por_mes:
                ingresos_por_mes[mes_inicio] = 0.0
            ingresos_por_mes[mes_inicio] += float(monto)
    return ingresos_por_mes

def determinar_categoria_mas_frecuente(alquileres):
    categorias = {}
    for alquiler in alquileres:
        categoria_nombre = alquiler["activo"]["categoria"]["nombre"]
        if categoria_nombre not in categorias:
            categorias[categoria_nombre] = 0
        categorias[categoria_nombre] += 1
    return max(categorias, key=categorias.get)

def calcular_duracion_alquileres(alquileres):
    duracion_alquileres = {}
    for alquiler in alquileres:
        fecha_inicio = datetime.strptime(alquiler["fechaInicio"], "%Y-%m-%d")
        fecha_fin = datetime.strptime(alquiler["fechaFin"], "%Y-%m-%d")
        duracion = (fecha_fin - fecha_inicio).days
        activo_id = alquiler["activo"]["_id"]
        if activo_id not in duracion_alquileres:
            duracion_alquileres[activo_id] = []
        duracion_alquileres[activo_id].append(duracion)
    return duracion_alquileres

def calcular_adquisiciones_por_mes(alquileres):
    adquisiciones_por_mes = {}
    for alquiler in alquileres:
        fecha_inicio = datetime.strptime(alquiler["fechaInicio"], "%Y-%m-%d")
        mes_inicio = fecha_inicio.strftime("%Y-%m")
        if mes_inicio not in adquisiciones_por_mes:
            adquisiciones_por_mes[mes_inicio] = 0
        adquisiciones_por_mes[mes_inicio] += 1
    return adquisiciones_por_mes
