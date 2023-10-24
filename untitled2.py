# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 15:07:15 2023

@author: cj23aah
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 1000)

sinh = np.sinh(x)
cosh = np.cosh(x)
plt.figure()
plt.plot(x,np.sinh(x),label="sinh(x)")
plt.plot(x,np.cosh(x),label="cosh(x)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.xlim(-5.0,5.0)
plt.show()
