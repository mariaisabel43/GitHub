Algoritmo sin_titulo
	cantidadVacunas = 1000
	vacunasGastadas = 0
	Mientras cantidadVacunas>0 Hacer
		Escribir "Digite cuantas vacunas ha usado"
		Leer vacunasGastadas
		cantidadVacunas = cantidadVacunas - vacunasGastadas
		Si cantidadVacunas<200 Entonces
			Escribir "Atención quedan menos de 200 vacunas"
		FinSi
	FinMientras
FinAlgoritmo
