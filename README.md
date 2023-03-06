LottOdds
===============
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/alejandroMAD/mvc-swing-drones/blob/master/README.md)
[![es](https://img.shields.io/badge/lang-es-yellow.svg)](https://github.com/alejandroMAD/mvc-swing-drones/blob/master/README.es.md)

User interface
----------
![Application screenshot](/screenshot.png)

A Python application with a TKinter graphical user interface that utilizes a flexible calculation algorithm to compute
the probabilities of winning the grand prize in lottery games across the world and under different rules and configurations.
The program makes use of the object-oriented paradigm by constructing elements such as graphical interface components and 
an abstract model of a lottery game using classes and objects. It employs a parameterized method with an algorithm capable
of calculating lottery odds with different rules and maximum values of drawn balls, including configurations with two drums,
one for regular drawings and another for extra-ball drawings.

This program is an open-source initiative whose goal is to educate people about the mathematical rules of combinatorics and 
probability that govern games of chance, and to combat the negative effects of the phenomenon that has often been described
with the phrase "Lottery is a taxation upon mathematical ignorance".

![Application logo](/lottodds_banner.png)

Features
-------------------
* The application presents a GUI so users can easily calculate the odds of winning lottery grand prizes.
* The GUI has spinner controls and a disable checkbox to help the user select the desired lottery game configuration.
* The algorithm allows for the calculation of winning odds in different types of lottery games with 1 or 2 drums of balls.
* A formatting function transforms the numeric result into a friendly and easy-to-understand explanation of the probability.
* The program properly catches exceptions related to wrong lottery configurations and value user inputs.
* A secondary message is displayed comparing the results with interesting statistical facts.
* The application stores localization strings to allow for the GUI to be displayed in Spanish and English.


Credits
-------------------

* Balls drum images: [Bingo icons created by Freepik - Flaticon](https://www.flaticon.com/free-icons/bingo)
* Lottery icons: [Lottery icons created by Flat Icons - Flaticon](https://www.flaticon.com/free-icons/lottery)


License
--------
    Copyright (C) 2022  Alejandro M. González
    
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
    
    MIT License: http://opensource.org/licenses/MIT
