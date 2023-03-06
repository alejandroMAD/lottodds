LottOdds
===============
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/alejandroMAD/LottOdds/blob/master/README.md)
[![es](https://img.shields.io/badge/lang-es-yellow.svg)](https://github.com/alejandroMAD/LottOdds/blob/master/README.es.md)

![Application logo](/lottodds_banner.png)


User interface
----------
![Application screenshot](/screenshot.png)

A Python application with a TKinter graphical user interface that utilizes a flexible calculation algorithm to compute
the probabilities of winning the grand prize in lottery games across the world and under different rules and configurations.

The program makes use of the object-oriented paradigm by constructing elements such as graphical interface components and 
the abstract model of a lottery game using classes and objects. It employs a parameterized method with an algorithm capable
of calculating lottery odds with different rules and maximum values of the balls in the pool, including single-drum
configurations and games with two drums, one for regular drawings and another for extra-ball drawings.

This program is an open-source initiative whose goal is to educate people about the mathematical rules of combinatorics and 
probability that govern games of chance, and to combat the negative effects of the phenomenon that has often been described
with the phrase:

<br/>

> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"Lottery is a taxation upon mathematical ignorance".

<br/>

Features
-------------------
* The application presents a GUI so users can conveniently calculate the odds of winning different lottery grand prizes.
* The GUI provides spinner controls and a disable checkbox to help the user select the desired lottery game configuration.
* The algorithm allows for the calculation of winning odds in different types of lottery games with 1 or 2 drums of balls.
* A formatting function transforms the numeric result into a friendly and easy-to-understand explanation of the probability.
* The program properly catches exceptions related to wrong lottery configurations and value user inputs.
* A secondary message is displayed comparing the results with interesting statistical facts.
* The application stores localization strings to allow for the GUI to be displayed in Spanish and English.

<br/>

Combinatorics
-------------------

![Combinations formula](/cformula.png)

The "Combination formula" or "Combinations formula" is used to calculate the number of ways to choose r items from a set
of n items, where the order of the items does not matter. In the context of lotteries, n represents the total number of balls
in the lottery pool, and r represents the number of balls drawn to determine the winning combination. The formula calculates
the number of possible combinations of r balls that can be drawn from the total set of n balls, and thus can be used to
calculate the odds of winning the lottery.

The exclamation mark (!) represents the factorial operation, which means multiplying a number by all the positive integers
less than it. For example, five factorial o 5! = 5 x 4 x 3 x 2 x 1 = 120.

<br/>

Tests
-------------------
Results of testing LottOdds application with different configurations inputs from world lottery games:

<br/>

<table>
  <tr>
    <td align="center"><b>Lottery game</b></td>
    <td align="center"><b>Drawing configuration</b></td>
    <td align="center"><b>Grand prize odds</b></td>
  </tr>
  <tr>
    <td>U.S. Mega Millions</td>
    <td>Regular draws: 5; Regular numbers: 70; Bonus draws: 1; Bonus numbers: 25</td>
    <td>1 in 302,575,350</td>
  </tr>
  <tr>
    <td>U.S. Powerball</td>
    <td>Regular draws: 5; Regular numbers: 69; Bonus draws: 1; Bonus numbers: 26</td>
    <td>1 in 292,201,338</td>
  </tr>
  <tr>
    <td>Europe EuroMillions</td>
    <td>Regular draws: 5; Regular numbers: 50; Bonus draws: 2; Bonus numbers: 12</td>
    <td>1 in 139,838,160</td>
  </tr>
  <tr>
    <td>Spain La Primitiva</td>
    <td>Regular draws: 6; Regular numbers: 49; Bonus draws: 1; Bonus numbers: 10</td>
    <td>1 in 139,838,160</td>
  </tr>
  <tr>
    <td>Spain El Gordo</td>
    <td>Regular draws: 5; Regular numbers: 54; Bonus draws: 1; Bonus numbers: 10</td>
    <td>1 in 31,625,100</td>
  </tr>
  <tr>
    <td>Spain Bonoloto</td>
    <td>Regular draws: 6; Regular numbers: 49; Bonus draws: 0; Bonus numbers: 0</td>
    <td>1 in 13,983,816</td>
  </tr>
  <tr>
    <td>Spain Christmas Lottery</td>
    <td>Regular draws: 1; Regular numbers: 100,000; Bonus draws: 0; Bonus numbers: 0</td>
    <td>1 in 100,000</td>
  </tr>
  <tr>
    <td>Australia Powerball</td>
    <td>Regular draws: 7; Regular numbers: 35; Bonus draws: 1; Bonus numbers: 20</td>
    <td>1 in 134,490,400</td>
  </tr>
  <tr>
    <td>Italia SuperEnalotto</td>
    <td>Regular draws: 6; Regular numbers: 90; Bonus draws: 0; Bonus numbers: 0</td>
    <td>1 in 622,614,630</td>
  </tr>
  <tr>
    <td>Japan Takarakuji Loto 7</td>
    <td>Regular draws: 7; Regular numbers: 37; Bonus draws: 0; Bonus numbers: 0</td>
    <td>1 in 10,295,472</td>
  </tr>
</table>

<br/>

> "At that point I ought to have gone away, but a strange sensation rose up in me, a sort of defiance of fate, a desire to challenge it, to put out my tongue at it. I laid down the largest stake allowed – four thousand gulden – and lost it. Then, getting hot, I pulled out all I had left, staked it on the same number, and lost again, after which I walked away from the table as though I were stunned. I could not even grasp what had happened to me"
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ― Fyodor M. Dostoevsky, The Gambler 

<br/>

Credits
-------------------

* Balls drum images: [Bingo icons created by Freepik - Flaticon](https://www.flaticon.com/free-icons/bingo)
* Lottery icons: [Lottery icons created by Flat Icons - Flaticon](https://www.flaticon.com/free-icons/lottery)

<br/>

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
