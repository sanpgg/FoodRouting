*Esta herramienta digital surgió de la colaboración entre el equipo del Municipio de San Pedro Garza García y la Brigada Digital MX*
# Dispersador de rutas
## Descripción
Repositorio que contiene los algoritmos necesarios para la optimización de rutas y asignación de recursos en respuesta a COVID-19.

## Problemática
Ante el contexto global y los estragos ocasionados por el virus COVID-19, el Municipio de San Pedro Garza García cuenta con una campaña de apoyo con paquetes alimenticios para los ciudadanos. Dada la demanda de entrega de apoyos (serie de coordenadas y el tipo de despensa dd = (lat,long, td) ), y centros de distribución (coordenadas cd = (lat,long)) es necesario encontrar la asignación óptima de los hogares a cada centro de distribución.

*** Variables:
- *Hogares*: Direcciones postales con coordenadas (lat,long);
- *Centros de Distribución*: Centros en los que se almacenan las despensas y luego de ahí salen las cuadrillas a repartirlas;
- *Cuadrillas*: Grupos de diversas dependencias que saldrán a entregar las despensas, cada uno es responsable de guardar su evidencia de la entrega, hay más de una cuadrilla por centro de distribución;
- *Despensas*: Hay al menos 4 tipos de despensas:
  - Adultos mayores.
  - Enfermos COVID-19
  - Familias con niños.
  - Familias sin niños.
  
*** Sistemas. 
Módulos a resolver: 

- Generar la distribución de insumos necesarios entre los diversos centros de distribución.
- Generar el orden en el que las cuadrillas tendrán que repartir las distintas despensas. 

*** Planeación de rutas. 
Dado un número de cuadrillas, con la demanda asignada al centro de distribución, tenemos que encontrar el orden de visita para cada uno de los hogares que cada cuadrilla visitará. Se busca que el problema sea óptimo y se minimice el tiempo en calle de cada una de las cuadrillas. 

## Ambiente de desarrollo
Si lo que deseas es utilizar el proyecto como desarrollador lo primero que debes hacer el preparar tu ambiente de desarrollo para poder realiar pruebas, detectar posibles errores e incluso proponer mejoras.

Este repositorio contiene archivos de compilación que se pueden usar para iniciar un entorno de desarrollo usando [Docker](https://www.docker.com/).

### Instrucciones de uso

* Sigue las siguientes instruciones para [instalar Docker](https://docs.docker.com/engine/installation/) en tu sitema operativo.

* Estructura de datos (test.json):
  ```json
    {
    "hogares": [
        {
            "labs_casas": 0000000,
            "lat": 25.000000,
            "lon": -100.00000
        }
        ],
	"centros": [
        {
		  "labs_centros": 1,
		  "lat": 25.0000000,
		  "lon": -100.00000000,
          "n": 18
	    }
        ]
    }
  ```
* Clonar este repositorio:

  ```bash
  $ git clone https://github.com/sanpgg/FoodRouting.git
  ```
* Ingresa a la carpeta del proyecto:

  ```bash
  $ cd FoodRouting
  ```
* Build:

  ```bash
  # Run with sudo if necessary
  $ docker build -t food-routing:latest . 
  ```
* Run:

  ```bash
  # Run with sudo if necessary
  $ docker run -it -p  3000:3000 food-routing 
  ```
* Mandar parámetros:

  ```bash
  # Run with sudo if necessary
  $ curl --header "Content-Type: application/json" --request POST --data @test.json http://127.0.0.1:3000/get_best_routes 
  ```
