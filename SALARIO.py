#programa: Este programa calcula el salario neto de un empleado después de aplicar impuestos y deducciones.
salariobm = float (input("Ingresa tu salario bruto mensual: "))
Porcentaje = float (input("Ingresa el porcentaje de impuestos: "))
deducciones = float (input("Ingresa el monto de deducciones adicionales: "))
impuesto = salariobm * (Porcentaje / 100)
Salario_neto = salariobm - impuesto - deducciones
print("Tu salario neto es: ", Salario_neto)
