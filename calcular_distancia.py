def calcular_distancia():

    # Solicitar ciudad de origen y destino
    ciudad_origen = input("Ciudad de Origen: ")
    ciudad_destino = input("Ciudad de Destino: ")

    # Solicitar distancia aproximada en km
    distancia_km = float(input("Ingresa la distancia aproximada en kms: "))
    
    # Solicitar velocidad promedio en km/h
    velocidad = float(input("Ingresa la velocidad promedio en km/h: "))
    
    # Operaciones para calcular la duración del viaje
    duracion_horas = distancia_km / velocidad
    horas = distancia_km//velocidad
    segundos = duracion_horas*3600
    sobrante1=segundos%3600
    minutos=sobrante1//60
    sobrante2=sobrante1%60

    # Calcular el combustible requerido en litros (supongamos 10 Km por litro)
    combustible_litros = round(distancia_km / 12, 1)

    # Mostrar la duración del viaje
    print()
    print(f"La duración aproximada de este viaje será {int(horas)} horas {int(minutos)} minutos y {int(sobrante2)} segundos")
    print()
    # Mostrar el combustible requerido
    print(f"El combustible requerido para este viaje (promediando 12 Km/l) será: {combustible_litros} lts")
    print()
    # Mostrar la narrativa del viaje
    print(f"Viaje desde {ciudad_origen} hasta {ciudad_destino}, con una duración aproximada de {int(horas)} horas {int(minutos)} minutos y {int(sobrante2)} segundos y un consumo de combustible aproximado de {combustible_litros} lts")


if __name__ == "__main__":
    calcular_distancia()
