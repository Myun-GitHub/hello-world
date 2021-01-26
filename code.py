# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 10:18:32 2021

@author: MaClo
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from cycler import cycler

plt.style.use('ggplot')
data = np.random.randn(50)

mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.linestyle'] = '--'

mpl.rcParams['axes.prop_cycle'] = cycler(color=['r', 'g', 'b', 'y'])
plt.plot(data)  # first color is red
