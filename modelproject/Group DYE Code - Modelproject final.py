# a. Import Packages
%matplotlib inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from ipywidgets import interact, fixed

# b. Defining functions
def u(c, alpha):
    """ Defines the CRRA utility function (Constant-Relative Risk Aversion)
    """
    return (1/alpha)* c**(1-alpha)

def U(c1, c2, alpha, delta):
    """ Defines the households life-time utility function
    """
    return u(c1, alpha) + delta*u(c2, alpha)

def bud_cons(c1, r, e1, e2):
    """ Defines the budget constraint

        e = e1 + e2/(1+r) is total endowment
    """
    e = e1 + e2/(1+r)
    return e*(1+r) - c1*(1+r)

def indif_curve(c1, ubar, alpha, delta):
    """ Defines the indifference curve
    """
    return  ( ((1-alpha)/delta)*(ubar - u(c1, alpha)) )**(1/(1-alpha))

def solve_opt(r, alpha, delta, e1, e2):
    """ This function solves the model by defining the first order condition.
        Returning consumption in both periods as well as the life-time utility
    """
    e = e1 + e2/(1+r)
    A = (delta*(1+r))**(1/alpha)
    c1 = e/(1+A/(1+r))
    c2 = c1*A
    u = U(c1, c2, alpha, delta)
    return c1, c2, u

# c. Parameter definitions
alpha = 0.5
delta = 1
r = 0
e1, e2 = 80, 20

rmin, rmax = 0, 1
cmax = 150

# d. Defining plotting function
def cons_plot(r, delta, alpha, e1, e2):
    """ This function will create a graph of the intertemporal utility and the budget constraint
    """
    c1 = np.linspace(0.1,cmax,num=100)
    c1e, c2e, uebar = solve_opt(r, alpha, delta, e1, e2)
    idfc = indif_curve(c1, uebar, alpha, delta)
    budg = bud_cons(c1,  r, e1, e2)
    
    fig, ax = plt.subplots(figsize=(8,8))
    ax.plot(c1, budg, lw=2.5)
    ax.plot(c1, idfc, lw=2.5)
    ax.vlines(c1e,0,c2e, linestyles="dashed")
    ax.hlines(c2e,0,c1e, linestyles="dashed")
    ax.plot(c1e,c2e,'ob')
    ax.vlines(e1,0,e2, linestyles="dashed")
    ax.hlines(e2,0,e1, linestyles="dashed")
    ax.plot(e1,e2,'ob')
    ax.text(e1-7,e2-6,r'$e^*$',fontsize=16)
    ax.set_xlim(0, cmax)
    ax.set_ylim(0, cmax)
    ax.set_xlabel(r'$c_1$', fontsize=16)
    ax.set_ylabel('$c_2$', fontsize=16)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.fill_between(c1, bud_cons(c1, r, e1, e2), alpha = 0.2)
    ax.grid()
    plt.show()

# e. Define function that returns allocation as a pandas frame and graph
def allocation():
    c1e, c2e, uebar = solve_opt(r, alpha, delta, e1, e2)
    
    lst = {"Consumption": [c1e,c2e],
           "Endowment": [e1,e2],
           "Saving": [e1-c1e,0]}
    """ Creating a list with Consumption, Endowment and Saving as variables
        with their respective values
    """
        
    df = pd.DataFrame(lst,columns= ["Consumption", "Endowment", "Saving"])
    df.index = ["Period 1", "Period2"]
    """ The code above creates our Pandas Dataframe which takes lst as input and applies the variables
        as column names
    """

    return df

# f.1 Allocation in the saving case
allocation()
cons_plot(r, delta, alpha, e1, e2)

# f.2 Allocation in the borrowing case
e1,e2 = 20,80
allocation()
cons_plot(r, delta, alpha, e1, e2)


# g. interactive graph - can ONLY be used in the notebook
interact(cons_plot, r=(rmin,rmax,0.1), alpha=fixed(alpha), delta=(0.5,1,0.1), e1=(10,100,1), e2=(10,100,1));