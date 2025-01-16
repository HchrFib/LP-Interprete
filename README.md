El llenguatge de programació Llull
===================================

Implementación del interprete y el pretty-print de lenguaje de progrmación llull. El glorioso.

Requisitos previos:

	- Tener instalado el interprete de python
   - instalación jre, para la visualización de arbol.
   - pasos para visualizar el árbol.

   			javac llull*.java
   			grun llull root -tree < program.llull
   			grun llull root -tree < program.llull


Instrucción para instalar librerias

	pip3 install nombre_libreria

Librerias instaladas:
   
   - Termcolor
   - Antlr4
   - Colorama

uso de librerias: 
   - sys
   - antlr
   - colorama
   - textwraper
   - termcolor

Ejecución
	
	Modos de ejecución:

	1) python3 llull.py program.llull, ejecutará por defecto el método main
	2) python3 llull.py program.llull nombre_funcion arg1 arg2 .... argn



Caracteristica del lenguaje:
	- Uso de funciones
	- Operaciones ariméticas muy simples
	- Crea arrays, 
	- Agrega y elementos de una array, para la obtención de elementos nuestro querido lenguaje puede obtener un índice a través de una expresión aritmética.
	- Realiza funciones recursivas :
	    - Hanoi
	    - MCD
	    - Números primos, etc
	    - Paso de parámetros por referencia en el caso de los arrays y por valor para variables de tipo entero.
	- Implementación de un pretty printer.

