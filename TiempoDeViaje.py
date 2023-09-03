def calcular_tiempo_total(tiempos):
    tiempo_total = sum(tiempos)
    return tiempo_total

tiempos = []
i = 0

while True:
    tiempo = int(input("Duracion tramo: "))
    if tiempo == 0:
        break
    tiempos.append(tiempo)
    i += 1

tiempo_total = calcular_tiempo_total(tiempos)

horas = tiempo_total // 60
minutos = tiempo_total % 60

print(f"Tiempo total de viaje: {horas}:{minutos:02} horas")
