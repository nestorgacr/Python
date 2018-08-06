if __name__ == '__main__':
    calificaciones = {}
    calificaciones['uno']=10
    calificaciones['dos']=7
    calificaciones['tres']=9
    calificaciones['cuatro']=9

    notas = 0

    for item in calificaciones.values():
        notas += item

    promedio = notas / len(calificaciones)

    print('El promedio es de {}'.format(promedio))
