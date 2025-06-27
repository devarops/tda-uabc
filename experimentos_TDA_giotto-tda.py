#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  5 19:43:32 2025

@author: user
"""

# numpy, pyplot
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# la librería principal es "gtda"
# https://giotto-ai.github.io/gtda-docs/0.5.1/library.html
from gtda.homology import VietorisRipsPersistence
from gtda.plotting import plot_diagram, plot_point_cloud

id = "H51_08"

data_path = f"trip_{id}.csv"
figure_path = f"diagrama_{id}.png"

trip_data_df = pd.read_csv(data_path)

array_2d = trip_data_df[["X", "Y"]].to_numpy()
zeros_col = np.zeros((array_2d.shape[0], 1))
array_3d_input = np.hstack((array_2d, zeros_col))
array_3d = array_3d_input.reshape((1, array_2d.shape[0], 3))

# vamos a juntar las elipses en una nube de puntos
cloud = array_3d
print(cloud.shape)

# calculamos diagrama de persistencia
VR = VietorisRipsPersistence(homology_dimensions=[0, 1])
diagram = VR.fit_transform(cloud)
print(diagram.shape)

# gráficas
plt.subplot(2, 1, 1)
plt.title('datos')
plt.scatter(x=cloud[0][:, 0], y=cloud[0][:, 1], color='k', label='datos')
plt.legend()


plt.subplot(2, 1, 2)
plt.title('diagrama de persistencia')
diagram2 = diagram[0][diagram[0][:, 2] == 0]
plt.scatter(x=diagram2[:, 0], y=diagram2[:, 1], label='$H_0$')
diagram3 = diagram[0][diagram[0][:, 2] == 1]
plt.scatter(x=diagram3[:, 0], y=diagram3[:, 1], label='$H_1$')
plt.legend()

maximo = np.max(diagram[0])
plt.xlim([0-maximo/32, maximo+maximo/32])
plt.ylim([0-maximo/32, maximo+maximo/32])
plt.plot([0, maximo], [0, maximo], linestyle="--")

plt.tight_layout()

plt.savefig(figure_path, transparent=True)
