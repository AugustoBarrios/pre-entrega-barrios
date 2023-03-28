import json
ruta = "C:/Users/augus/OneDrive/Escritorio/Primera pre-entrega + Barrios/"

def registro():
    usuario =  input("Ingresa tu usuario")
    contraseña = input("Ingresa una contraseña")
    
    content = {"Usuario": usuario, "Contrasena": contraseña}

    with open(ruta + 'baseDeDAtos.json', 'r', encoding='utf-8') as file:
        datos_a_leer = json.load(file)
        print(datos_a_leer)
        datos_a_leer.append(content)
        print(datos_a_leer)
    
    with open(ruta+ 'baseDeDAtos.json', 'w') as file:
        json.dump(datos_a_leer, file, indent=2)

registro()