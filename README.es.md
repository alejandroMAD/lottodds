LottOdds
===============
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/alejandroMAD/LottOdds/blob/master/README.md)
[![es](https://img.shields.io/badge/lang-es-yellow.svg)](https://github.com/alejandroMAD/LottOdds/blob/master/README.es.md)

![Application logo](/lottodds_banner.png)


User interface
----------
![Application screenshot](/screenshot.png)

Una aplicación escrita en Python con interfaz gráfica de usuario que permite, por medio de un algoritmo de cálculo flexible,
obtener las probabilidades de ganar el premio máximo en sorteos de lotería bajo diferentes reglas y configuraciones.

El programa emplea el paradigma de orientación a objetos construyendo elementos tales como los componentes de la interfaz
o el modelo abstracto de un sorteo de lotería mediante clases y objetos, y hace valer un método parametrizado con un algoritmo
capaz de calcular las probabilidades de sorteos de lotería con diferentes reglas y valores máximos de las bolas disponibles,
incluyendo configuraciones de uno y dos bombos, uno de extracciones regulares y otro de extracciones de bolas extra.

Este programa surge de una iniciativa para divulgar información sobre las reglas matemáticas de combinatoria y probabilidad
que gobiernan los juegos de azar y combatir los efectos negativos del fenómeno que se ha descrito muchas veces con la frase:

<br/>

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"La lotería es un impuesto sobre la ignorancia matemática".

<br/>

Características
-------------------
* La aplicación presenta una GUI para que los usuarios puedan calcular cómodamente la probabilidad de ganar en juegos de lotería.
* La interfaz gráfica tiene controles numéricos y un checkbox para deshabilitar el bombo secundario, para ayudar al usuario a seleccionar la configuración del juego de lotería deseada.
* El algoritmo permite el cálculo de la probabilidad de ganar en diferentes tipos de juegos de lotería con 1 o 2 bombos de bolas.
* Una función para dar formato transforma el resultado numérico en una cadena con una explicación fácil de entender de la probabilidad.
* El programa maneja adecuadamente las excepciones por configuraciones de lotería inválidas y valores de entrada del usuario incorrectos.
* Junto al resultado, se muestra un mensaje secundario que compara los resultados con datos estadísticos interesantes.
* La aplicación almacena localización de textos para permitir que la interfaz gráfica se muestre en español o en inglés.

<br/>

Combinatoria
-------------------

![Combinations formula](/cformula.png)

La Fórmula de Combinaciones permite calcular la probabilidad de seleccionar un conjunto de r elementos en un conjunto de n elementos,
sin importar el orden en que se seleccionen. Esta fórmula se utiliza comúnmente en el cálculo de las probabilidades de ganar en juegos
de lotería y otros juegos de azar en los que se deben seleccionar un número determinado de elementos de un conjunto más grande.
En la fórmula, n es el número total de elementos en el conjunto y r es el número de elementos que se desean seleccionar.

El signo de exclamación (!) representa la operación de factorial, que significa multiplicar un número por todos los enteros positivos
desde 1 hasta dicho número. Por ejemplo, el factorial de cinco ó 5! = 5 x 4 x 3 x 2 x 1 = 120.

<br/>

Pruebas
-------------------
Resultados de las pruebas propuestas para LottOdds con diferentes configuraciones de sorteos de lotería de todo el mundo como inputs:

<br/>

<table>
  <tr>
    <td align="center"><b>Juego de lotería</b></td>
    <td align="center"><b>Configuración de números y extracciones</b></td>
    <td align="center"><b>Probabilidad</b></td>
  </tr>
  <tr>
    <td>EE. UU. Mega Millions</td>
    <td>Bolas normales: 5; Número máximo en las bolas normales: 70;
        <br>Bolas extra: 1; &emsp;&nbsp;&nbsp; Número máximo en las bolas extra: 25</td>
    <td>1 entre 302.575.350</td>
  </tr>
  <tr>
    <td>EE. UU. Powerball</td>
    <td>Bolas normales: 5; Número máximo en las bolas normales: 69;
        <br>Bolas extra: 1; &emsp;&nbsp;&nbsp; Número máximo en las bolas extra: 26</td>
    <td>1 entre 292.201.338</td>
  </tr>
  <tr>
    <td>Europa EuroMillones</td>
    <td>Bolas normales: 5; Número máximo en las bolas normales: 50;
        <br>Bolas extra: 2; &emsp;&nbsp;&nbsp; Número máximo en las bolas extra: 12</td>
    <td>1 entre 139.838.160</td>
  </tr>
  <tr>
    <td>España La Primitiva</td>
    <td>Bolas normales: 6; Número máximo en las bolas normales: 49;
        <br>Bolas extra: 1; &emsp;&nbsp;&nbsp; Número máximo en las bolas extra: 10</td>
    <td>1 entre 139.838.160</td>
  </tr>
  <tr>
    <td>España El Gordo</td>
    <td>Bolas normales: 5; Número máximo en las bolas normales: 54;
        <br>Bolas extra: 1; &emsp;&nbsp;&nbsp; Número máximo en las bolas extra: 10</td>
    <td>1 entre 31.625.100</td>
  </tr>
  <tr>
    <td>España Bonoloto</td>
    <td>Bolas normales: 6; Número máximo en las bolas normales: 49;
        <br>Bolas extra: 0; &emsp;&nbsp;&nbsp; Número máximo en las bolas extra: 0</td>
    <td>1 entre 13.983.816</td>
  </tr>
  <tr>
    <td>España Lotería de Navidad</td>
    <td>Bolas normales: 1; Número máximo en las bolas normales: 100,000;
        <br>Bolas extra: 0; &emsp;&nbsp;&nbsp; Número máximo en las bolas extra: 0</td>
    <td>1 entre 100.000</td>
  </tr>
  <tr>
    <td>Australia Powerball</td>
    <td>Bolas normales: 7; Número máximo en las bolas normales: 35;
        <br>Bolas extra: 1; &emsp;&nbsp;&nbsp; Número máximo en las bolas extra: 20</td>
    <td>1 entre 134.490.400</td>
  </tr>
  <tr>
    <td>Italia SuperEnalotto</td>
    <td>Bolas normales: 6; Número máximo en las bolas normales: 90;
        <br>Bolas extra: 0; &emsp;&nbsp;&nbsp; Número máximo en las bolas extra: 0</td>
    <td>1 entre 622.614.630</td>
  </tr>
  <tr>
    <td>Japón Takarakuji Loto 7</td>
    <td>Bolas normales: 7; Número máximo en las bolas normales: 37;
        <br>Bolas extra: 0; &emsp;&nbsp;&nbsp; Número máximo en las bolas extra: 0</td>
    <td>1 entre 10.295.472</td>
  </tr>
</table>

<br/>

> "Debiera haberme retirado entonces, pero en mí surgió una extraña sensación, una especie de reto a la suerte, un afán de mojarle la oreja, de sacarle la lengua. Apunté con la puesta más grande permitida, cuatro mil florines, y perdí. Luego, enardecido, saqué todo lo que me quedaba, lo apunté al mismo número y volví a perder. Me aparté de la mesa como atontado. Ni siquiera entendía lo que me había pasado"
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ― Fyodor M. Dostoevsky, El jugador

<br/>

Reconocimiento
-------------------

* Imágenes de bombos de lotería: [Iconos de bingo creados por Freepik - Flaticon](https://www.flaticon.com/free-icons/bingo)
* Iconos de lotería: [Iconos de lotería creados por Flat Icons - Flaticon](https://www.flaticon.com/free-icons/lottery)

<br/>

Licencia
--------
    Copyright (C) 2022  Alejandro M. González
    
    Licencia MIT: http://opensource.org/licenses/MIT
