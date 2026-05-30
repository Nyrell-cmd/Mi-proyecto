saldo = 5.0
papas = 0
chocolates = 0
refrescos = 0

while saldo >= 1.50:
    print("\n===== MAQUINA DE SNACKS =====")
    print(f"Saldo disponible: Bs. {saldo:.2f}")
    print("1. Papas (Bs. 1.50)")
    print("2. Chocolate (Bs. 2.00)")
    print("3. Refresco (Bs. 2.50)")
    print("4. Finalizar compra")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        if saldo >= 1.50:
            saldo -= 1.50
            papas += 1
            print("Compra realizada.")
        else:
            print("Saldo insuficiente.")

    elif opcion == "2":
        if saldo >= 2.00:
            saldo -= 2.00
            chocolates += 1
            print("Compra realizada.")
        else:
            print("Saldo insuficiente.")

    elif opcion == "3":
        if saldo >= 2.50:
            saldo -= 2.50
            refrescos += 1
            print("Compra realizada.")
        else:
            print("Saldo insuficiente.")

    elif opcion == "4":
        break

    else:
        print("Opcion invalida.")

print("\n===== RESUMEN =====")
print(f"Papas compradas: {papas}")
print(f"Chocolates comprados: {chocolates}")
print(f"Refrescos comprados: {refrescos}")
print(f"Saldo restante: Bs. {saldo:.2f}")
