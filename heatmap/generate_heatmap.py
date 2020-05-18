#!/usr/bin/env python

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.colors as colors

import pandas as pd
import numpy as np


df = pd.read_csv("matrix.csv", index_col=0)

fig, ax = plt.subplots(1)
fig.set_size_inches(6, 3)

c = plt.pcolor(df, norm=colors.LogNorm(vmin=0.49, vmax=1))

cb = plt.colorbar(c,  ticks=[i/10 for i in range(5,11)])
cb.set_ticklabels(["%.1f"% (i/10) if i != 5 else "<0.5" for i in range(5,11)])

ax.add_patch(
    patches.Rectangle(
        (4, 8),
        1,
        1,
        edgecolor='r',
        facecolor="none",
        linewidth=2,
        )
    )
            

plt.yticks(np.arange(0.5, len(df.index), 1), df.index)
plt.xticks(np.arange(0.5, len(df.columns), 1), df.columns)

plt.xlabel("$M_o$")
h = plt.ylabel("$M_d$")

h.set_rotation(0)

#remove whitespace
#https://stackoverflow.com/questions/11837979/removing-white-space-around-a-saved-image-in-matplotlib
plt.subplots_adjust(top = 1, bottom = 0, right = 1, left = 0, 
                    hspace = 0, wspace = 0)
plt.margins(0,0)

plt.savefig("barcode_graph_optimisation.pdf", bbox_inches ='tight', pad_inches=0)
