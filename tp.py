tipo_material = print("Ingrese el tipo de material que requiere, son los siguientes:")
materiales = ["Madera","Acero","Pvc"]
for material in materiales:
    print(material)
    #funcion para realizar una lista y elegir una de las opciones
eliga_material = input("Ingrese el tipo de material:")
peso = float(input("Ingrese su peso:"))
#funcion para escribir el peso y tipo de material
if peso<50:
    print("Su precio del flete es 350$.")
elif 50<= peso<100:
    print(f"Su precio es de 400$.")
elif 100<= peso<300:
    print(f"El precio es de 500")
else: 
    print("Precio de 650")
    #funcion para determinar su precio dado con su peso


