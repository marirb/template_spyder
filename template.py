# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(username)s
"""

import numpy as np
from matplotlib import pyplot as pl
from glob import glob
from scipy.optimize import curve_fit
from scipy.interpolate import UnivariateSpline
from scipy.signal import savgol_filter
from matplotlib import rc,cm,ticker
from useful_stuff.useful import *
pl.rcParams["savefig.directory"] = os.chdir(os.path.dirname(__file__))
pl.close('all')


rc('text', usetex=True)
rc('font', family='serif',serif='Computer Modern Roman')
rc('text.latex', unicode=True)
rc('text.latex', preamble='\usepackage{siunitx}')
rc('lines',linewidth = 1.5, markersize=10)
rc('axes.formatter', limits=((-3,7)))
pl.rcParams.update(matplotlib_parameters2(size=3,textsize=1.6))
#cmap=cm.Set1
#color=[cmap(i) for i in np.linspace(0, 1, 9)]
pl.rcParams['axes.color_cycle'] = tableau20




def figure_():
    fig,ax=pl.figure(),pl.axes() #[0.15,0.15,0.95-0.15,0.95-0.15]
#    fig.gca().set_color_cycle([cmap(i) for i in np.linspace(0, 1, 100)]) 
#    ax2=pl.axes([])
#    ax2.set_visible(False)

    ax.plot()

    ax.set_xlabel(r'')
    ax.set_ylabel(r'')
    ax.set_title(r'')
#    ax.text(260,380,r'$\mu_{{eff}}={:.3f}\mu_{{\rm B}}$'.format(2.8295*np.sqrt(popt1[0])) + '\n' + r'$T_W={:.2f}\,$K'.format(popt1[1]) + '\n' + r'$\chi_0={:.2f}\cdot 10^{{-9}}$'.format(1e5*popt1[2]),horizontalalignment='center', verticalalignment='center',linespacing=1.5)
#    ax.text(50,50,r'', horizontalalignment='center', verticalalignment='center')

#    ax.set_xlim(0,300)
#    ax.set_ylim(0,20)
#    ax2.set_xlim(0,300)
#    ax2.set_ylim(0,20)
#    ax.set_xscale('log')
#    ax.set_yscale('log')
    ax.legend()
#    ax.set_xticks(tuple(np.linspace(5,100,20)))
#    ax.get_yaxis().set_major_formatter(ticker.ScalarFormatter())
#    pl.close()
    pl.tight_layout(pad=0.2)
    move_figure(2000,90)





























