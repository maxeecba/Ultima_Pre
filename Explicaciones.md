Herencia de templates 

Consiste en usar como base determinadas cosas que estaran en todos nuestros templates. (menu principal, pie de pagina, logo,etc). son identicos en todas las paginas
son estaticos.

Esto se realizará pasando todos los elementos comunes al template padre y dejando en el template hijo todos los elementos que queremos modificar

crear el archivo padre.html y dentro de la misma pegamos todo lo que está dentro de inicio.html. 
dentro del archivo padre.html crearemos un segmento que que es el que va cambiar segun la vista que mostremos 
Entre el header y el footer crearemos una etiqueta y el contenido que cambia 
{% block "contenido que cambia"%}
Todo lo que está dentro de acá va cambiar.
{% endblock "contenido que cambia" %}
Fuera lo que no cambia

Usaremos inicio como uno de los hijos del padre 


Usaremos la palabra extend para heredar los componentes que estan en el modulo html que elijamos
{% extends 'nombre de la carpeta que esta dentro de la carpeta template/nombre del modulo .html' %}

Con load static cargamos los statics en este archivo html 
{% load static %}

y dentro de nuestro bloque que se llama contenido que cambia 
{% block "contenido que cambia"%}
<h1> titulo</h1>
<p>contenido </p>
{% endblock "contenido que cambia" %}