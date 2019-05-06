# This is the raw code - it's not designed to be run in VS that is, it will not show the same interactive results as in Jupyter Lab.
# The goal of the code is to be interactive inside of Jupyter Lab and showing the consumers intertemporal choice


# Import Packages
%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, fixed


# a. Simple consumer choice
def U(c1, c2, alpha):
    return (c1**alpha)*(c2**(1-alpha))
    """ Defining the utility function as a simple cobb-douglas function
        c1,c2 are the two goods avalaible in the market
    """

def budgetc(c1, p1, p2, I):
    return (I/p2)-(p1/p2)*c1
    """ Defining the budget constraint
        p1,p2 = prices and I = endowment

        The function is written such that c2 = ... so that we can plot it later on
    """

def indif(c1, ubar, alpha):
    return (ubar/(c1**alpha))**(1/(1-alpha))
    """ Defining the indifference curve

        Same as for the budget constraint. the indifference curved is solved for c2
        so that it can be plotable
    """

def find_opt(p1,p2,I,alpha):
    c1 = alpha * I/p1
    c2 = (1-alpha)*I/p2
    u = U(c1,c2,alpha)
    return c1, c2, u
    """ Finding the optimum

        We have solved the consumers utility function by Lagrange.
    """

# b. paramers for plot
alpha = 0.5
p1, p2 = 1, 1
I = 100
""" Setting parameter for our plots to be used later in the code
"""

pmin, pmax = 1, 4
Imin, Imax = 10, 200
cmax = (3/4)*Imax/pmin
""" Setting parameter for our plots to be used later in the code
"""

def consume_plot(p1=p1, p2=p2, I=I, alpha=alpha):
    
    c1 = np.linspace(0.1,cmax,num=100)
    c1e, c2e, uebar = find_opt(p1, p2 ,I, alpha)
    idfc = indif(c1, uebar, alpha)
    budg = budgetc(c1, p1, p2, I)
    
    fig, ax = plt.subplots(figsize=(8,8))
    ax.plot(c1, budg, lw=2.5)
    ax.plot(c1, idfc, lw=2.5)
    ax.vlines(c1e,0,c2e, linestyles="dashed")
    ax.hlines(c2e,0,c1e, linestyles="dashed")
    ax.plot(c1e,c2e,'ob')
    ax.set_xlim(0, cmax)
    ax.set_ylim(0, cmax)
    ax.set_xlabel(r'$c_1$', fontsize=16)
    ax.set_ylabel('$c_2$', fontsize=16)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.grid()
    plt.show()
""" hvad sker der her??
"""


# c. Intertemporal choice model
def u(c, rho):
    """ The function is used to define the utility function
    """
    return (1/rho)* c**(1-rho)

def U2(c1, c2, rho, delta):
    """ The function is used to define the utility function
    """
    return u(c1, rho) + delta*u(c2, rho)

def budget2(c1, r, y1, y2):
    """ The function is used to define the budget constraint
    """
    Ey = y1 + y2/(1+r)
    return Ey*(1+r) - c1*(1+r)

def indif2(c1, ubar, rho, delta):
    """ The function is used to define the indifference function
    """
    return  ( ((1-rho)/delta)*(ubar - u(c1, rho)) )**(1/(1-rho))

def find_opt2(r, rho, delta, y1, y2):
    """ The function is used to define the optimum
    """
    Ey = y1 + y2/(1+r)
    A = (delta*(1+r))**(1/rho)
    c1 = Ey/(1+A/(1+r))
    c2 = c1*A
    u = U2(c1, c2, rho, delta)
    return c1, c2, u

# d. parameters for plot
rho = 0.5
delta = 1
r = 0
y1, y2 = 80, 20

rmin, rmax = 0, 1
cmax = 150
""" Section d is simply to state the parameter values for the comming plots
"""


def consume_plot2(r, delta, rho, y1, y2):
    
    c1 = np.linspace(0.1,cmax,num=100)
    c1e, c2e, uebar = find_opt2(r, rho, delta, y1, y2)
    idfc = indif2(c1, uebar, rho, delta)
    budg = budget2(c1,  r, y1, y2)
    
    fig, ax = plt.subplots(figsize=(8,8))
    ax.plot(c1, budg, lw=2.5)
    ax.plot(c1, idfc, lw=2.5)
    ax.vlines(c1e,0,c2e, linestyles="dashed")
    ax.hlines(c2e,0,c1e, linestyles="dashed")
    ax.plot(c1e,c2e,'ob')
    ax.vlines(y1,0,y2, linestyles="dashed")
    ax.hlines(y2,0,y1, linestyles="dashed")
    ax.plot(y1,y2,'ob')
    ax.text(y1-6,y2-6,r'$y^*$',fontsize=16)
    ax.set_xlim(0, cmax)
    ax.set_ylim(0, cmax)
    ax.set_xlabel(r'$c_1$', fontsize=16)
    ax.set_ylabel('$c_2$', fontsize=16)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.grid()
    plt.show()

interact(consume_plot2, r=(rmin,rmax,0.1), rho=fixed(rho), delta=(0.5,1,0.1), y1=(10,100,1), y2=(10,100,1));
""" An interactive graph for consumption
"""


consume_plot()

interact(consume_plot,p1=(pmin,pmax,0.1),p2=(pmin,pmax,0.1), I=(Imin,Imax,10),alpha=(0.05,0.95,0.05));

# Saving case
consume_plot2(r, delta, rho, y1, y2)

interact(consume_plot2, r=(rmin,rmax,0.1), rho=fixed(rho), delta=(0.5,1,0.1), y1=(10,100,1), y2=(10,100,1));

c1e, c2e, uebar = find_opt2(r, rho, delta, y1, y2)

c1e, c2e

y1,y2

y1-c1e


# A barrowing case
y1,y2 = 20,80
consume_plot2(r, delta, rho, y1, y2)