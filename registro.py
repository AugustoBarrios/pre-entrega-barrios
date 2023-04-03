import json
ruta = "C:/Users/augus/OneDrive/Escritorio/Primera pre-entrega + Barrios/"

""" def registro():
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

registro() """ 

def login():
    usuario =  input("Ingresa tu usuario")
    
    
    with open(ruta + 'baseDeDAtos.json', 'r', encoding='utf-8') as file:
        datos_a_leer = json.load(file)
        for lista in datos_a_leer:
            if usuario == lista["Usuario"]:
                print( f"Ahora brindanos tu contraseña querido/a {usuario}")
                contraseña = input("Ingresa una contraseña")
                if contraseña == lista["contrasena"]:
                    print(f"Bienvenido {usuario}")
                else: print("O te equivocaste de contraseña o eres un hacker, cual sera la opcion correcta?")
            else:()


login()