import os
import subprocess
import sys
import shutil
import time

def credits():
    print("\n\033[31mCreado por: \033[0m\033[34mFabio Hams Valois Marin\033[0m")
    print("\033[32mLinkedIn: \033[34mwww.linkedin.com/in/fabio-hams-valois-marin-9514ab340\033[0m")
    print("\n\033[31mGracias por usar esta herramienta. Si te atreves...\033[0m")

def show_image():
    if shutil.which("img2txt") is not None:
        if os.path.exists("joker.png"):
            print("\n\033[1;33mCargando la imagen... \033[0m")
            # Simular carga lenta de la imagen
            time.sleep(2)  # Pausa para efecto de carga
            subprocess.run(["img2txt", "joker.png"])  # Mostrar imagen
        else:
            print("\n\033[1;31mNo se encontró la imagen 'joker.png' en el directorio actual.\033[0m")
    else:
        print("\n\033[1;31mNo se puede mostrar la imagen. Asegúrate de tener la herramienta 'img2txt' instalada.\033[0m")

# búsqueda en Google
def search_google(query):
    print(f"\n\033[1;35mBuscando en Google: {query}\033[0m")
    subprocess.run(["googler", "--count", "10", query])
    time.sleep(5)  # Pausa de 5 segundos entre cada búsqueda para evitar bloqueos

#  redes sociales con el nombre de usuario
def search_social_media(username):
    print(f"\n\033[1;36mBuscando en redes sociales para: {username}\033[0m")
    search_google(f"site:twitter.com {username}")
    search_google(f"site:linkedin.com {username}")
    search_google(f"site:instagram.com {username}")
    search_google(f"site:facebook.com {username}")
    search_google(f"site:reddit.com {username}")

#  buscar en la Deep Web (.onion)
def search_deep_web(query):
    print(f"\n\033[1;32mBuscando en la Deep Web: {query}\033[0m")
    subprocess.run(["googler", f"site:.onion {query}"])
    time.sleep(5)  # Pausa de 5 segundos entre cada búsqueda en la Deep Web

# Función para realizar búsquedas más específicas (empleados, documentos, etc.)
def search_company_related(company_name):
    print(f"\n\033[1;33mBuscando información relacionada con la empresa: {company_name}\033[0m")
    search_google(f"empleados {company_name}")
    search_google(f"nómina {company_name}")
    search_google(f"información {company_name}")
    search_google(f"documentos {company_name}")
    search_google(f"site:linkedin.com {company_name}")
    search_deep_web(f"empleados {company_name}")
    search_deep_web(f"nómina {company_name}")
    search_deep_web(f"documentos {company_name}")


def menu():
    os.system('clear')
    show_image()  # Mostrar la imagen lentamente al iniciar
    credits()  # Mostrar los créditos

    # Menú macabro
    while True:
        print("\033[1;31m--------------------------------------------------\033[0m")
        print("\033[1;33m1.\033[0m \033[1;35mIniciar búsqueda\033[0m")
        print("\033[1;33m2.\033[0m \033[1;34mBuscar en redes sociales (Twitter, LinkedIn, Instagram, Facebook, Reddit)\033[0m")
        print("\033[1;33m3.\033[0m \033[1;32mBuscar en la Deep Web\033[0m, En desarrollo ")
        print("\033[1;33m4.\033[0m \033[1;36mBuscar información relacionada con una empresa\033[0m")
        print("\033[1;33m5.\033[0m \033[1;31mSalir\033[0m")
        print("\033[1;31m--------------------------------------------------\033[0m")
        option = input("\033[1;37mElija una opción: \033[0m")

        if option == "1":
            consulta = input("\n\033[1;37mIntroduce la consulta de búsqueda (nombre, teléfono, IP, etc.): \033[0m")
            tipo_de_archivo = input("\033[1;37mIntroduce el tipo de archivo (pdf, docx, xml, etc.): \033[0m")
            search_query = f"filetype:{tipo_de_archivo} {consulta}"
            search_google(search_query)
        
        elif option == "2":
            username = input("\n\033[1;37mIntroduce el nombre de usuario para buscar en redes sociales: \033[0m")
            search_social_media(username)
        
        elif option == "3":
            consulta = input("\n\033[1;37mIntroduce la consulta para la Deep Web (.onion): \033[0m")
            search_deep_web(consulta)
        
        elif option == "4":
            company_name = input("\n\033[1;37mIntroduce el nombre de la empresa para buscar información relacionada: \033[0m")
            search_company_related(company_name)
        
        elif option == "5":
            print("\033[1;31m¡Hasta luego, si te atreves a regresar!\033[0m")
            sys.exit(0)
        
        else:
            print("\033[1;31mOpción inválida. Por favor, elija nuevamente.\033[0m")

if __name__ == "__main__":
    menu()
