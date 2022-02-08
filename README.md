# PI-Simulator

## Part1 
The first part of the project is to write a python module approximate_pi.py which will be the core of our simulation. 
In other words, this module will only do the work related to the calculation of an approximation of $\pi$ without worrying about visualization issues in the form of an image.

$ python3 simulator.py n

Where n is the number of points used in the simulation. Example; python3 simulator.py 1000000


## Part2

We will now use simulator.py as a module to generate our animated image representing a simulation. The task is to write a python program approximate_pi.py which :

receives 3 arguments in the following order from the command line :
$\star$ the size of the image in pixels, which is square so a single integer which must be greater than or equal to 100 ;
$\star$  the number of points n to be used in the simulation, which must be greater than 100;
$\star$ the number of digits after the decimal point to be used in the display of the approximate value of $\pi$, which must be between 1 and 5.

Example : python3 approximate_pi.py 800 1000000 5




