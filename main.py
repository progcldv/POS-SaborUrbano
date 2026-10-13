'''
Proyecto PBD A8.1 Práctica Proyecto Básico Python
El Food Truck "Sabor Urbano" necesita automatizar el control de sus ventas diarias. 
Tu misión es desarrollar un programa en Python que registre cada venta del día, aplique reglas de cobro y entregue un balance detallado al finalizar la jornada.
'''

monto_total_diario = 0.0
caja_abierta = True

while caja_abierta:
    print("MENÚ")
    print("1. Registrar Venta")
    print("2. Ver total acumulado del día.")
    print("3. Cerrar caja y salir.")

    opcion = input("Ingrese opción: ")
    if opcion == "1":
        print("REGISTRO DE VENTAS")
        subtotal_cliente = 0.0
        registro_venta = True

        while registro_venta:
            entrada = input("Ingrese precio: ")

            if entrada == "0" or entrada == "fin":
                registro_venta = False
            else:
                precio = float(entrada)
                subtotal_cliente = subtotal_cliente + precio
            #fin-if
        #fin-while
        print("--- Boleta ---")
        print("Subtotal: ", subtotal_cliente)
        monto_iva = subtotal_cliente * 0.19
        total_iva_cliente = subtotal_cliente + monto_iva
        print("Monto IVA: ", monto_iva)
        print("Total Cliente (+IVA): ", total_iva_cliente)

        print("--- Metodo de pago ---")
        metodo_pago = input("1.Efectivo\n2.Tarjeta\nOpción: ")
        descuento = 0.0 
        if metodo_pago == "1":
            descuento = total_iva_cliente*0.05
            print("Descuento por efectivo (5%): ", descuento)
        total_final_cliente = total_iva_cliente - descuento
        print("---")
        print("Total Final: ", total_final_cliente)
        print("---")
        if total_final_cliente > 15000:
            print("Clasificada como Venta Alta")
        else:
            print("Clasificada como Venta Habitual")
        # fin-if
        print("---")
        monto_total_diario = monto_total_diario + total_final_cliente
        print("Monto Total Diario: ", monto_total_diario)
    elif opcion == "2":
        print("TOTAL ACUMULADO DEL DIA")
    elif opcion == "3":
        print("CERRAR CAJA Y SALIR")
        caja_abierta = False
    else:
        print("Opcion No valida, por favor ingrese 1, 2 o 3.")
    # fin-if
#fin-while