'''
    FUENTE: https://platzi.com/clases/1104-python/7119-implementando-web-scrapi-7/
'''
import requests
from bs4 import BeautifulSoup
import urllib.request

if __name__ == '__main__':
    for i in range(1,11):
        # requests.get: ejecuta una llamada HTTP GET a la URL indicada
        response = requests.get(f'https://www.xkcd.com/{i}')
        print(response.content)
        print(type(response.content))
        # BeautifulSoup: es una biblioteca que facilita el scrapping de información de páginas web. 
        # Se encuentra por encima de un parseador HTML o XML, proporcionando un idioma "pytónico" para 
        # poder iterar, buscar y modificar el árbol parseado.
        # Le enviamos lo parámetros:
        # - markup: Una cadena o un objeto similar a un archivo que representa el contenido para ser parseado.
        # - features: Características del parseador que  será utilizado, que puede ser el nombre 
        # de un parseador específico ("lxml", "lxml-xml", "html.parser" o "html5lib") 
        # o puede ser el tipo de contenido ("html", "html5", "xml"). 
        # Se recomienda que se indique un parseador específico, para que BeautifulSoup retorne
        # los mismos resultados en todas las plataformas y entornos virtuales.
        soup = BeautifulSoup (response.content, 'html.parser')
        
        # soup.find: buscamos el elemento con id = "comic" 
        image_container = soup.find (id = 'comic')
        
        # soup.find: buscamos el nodo <img/> y obtenemos el valor de su atributo "src" 
        image_url = image_container.find('img')['src']
        
        # obtenemos la última parte de la cadena dividida por "/" (que será el nombre del archivo)
        image_name = image_url.split('/')[-1]
        print(f'Descargando la imagen {image_url}')
        
        # urllib.request.urlretrieve: Recupere el contenido de una URL en una ubicación temporal en el disco.
        # Enviamos los parámetros URL y la cadena "files/" concatenada al nombre de archivo (se usará como 
        # ruta de ubicación del archivo temporal).
        urllib.request.urlretrieve(f'https:{image_url}', f'files/{image_name}')
