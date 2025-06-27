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

# creando elipses
# me basé en lo que necesita VietorisRipsPersistence siguiendo:
# https://github.com/giotto-ai/giotto-tda/blob/master/examples/data/generate_datasets.py


def crear_elipse(centro, eje_horizontal, eje_vertical, num_datos, magnitud_ruido):
    '''
    Parameters
    ----------
    centro : array of shape (1,2)
        Center ellipse at (centro[0],centro[1])
    eje_horizontal : float
        Horizontal radius.
    eje_vertical : float
        Vertical radius.
    num_datos : int
        Number of data points.
    magnitud_ruido : float
        Add random noise to data following uniform distribution over 
        [0,magnitud_ruido].

    Returns
    -------
    datos : ndarray of shape (1,num_datos,3)

    '''
    x0, y0 = centro
    rx, ry = eje_horizontal, eje_vertical
    noise = magnitud_ruido

    datos = np.array([[[x0 + rx*np.cos(t) + noise*np.random.rand(1)[0],
                        y0 + ry*np.sin(t) + noise*np.random.rand(1)[0],
                        0]
                       for t in np.linspace(0, 2*np.pi, num_datos+1)[0:-1]
                       ]
                      ])
    return datos


# elipses sin ruido
centro1 = [0, 0]
r_hor1 = 1
r_ver1 = 2
n_dat1 = 10
cloud1 = crear_elipse(centro1, r_hor1, r_ver1, n_dat1, 0.)

centro2 = [5, 5]
r_hor2 = 2
r_ver2 = 2
n_dat2 = 10
cloud2 = crear_elipse(centro2, r_hor2, r_ver2, n_dat2, 0.)


def get_cloud_from_trip_data(trip_id):
    data_path = f"trip_{trip_id}.csv"

    trip_data_df = pd.read_csv(data_path)

    array_2d = trip_data_df[["X", "Y"]].to_numpy()
    zeros_col = np.zeros((array_2d.shape[0], 1))
    array_3d_input = np.hstack((array_2d, zeros_col))
    array_3d = array_3d_input.reshape((1, array_2d.shape[0], 3))
    return array_3d


# vamos a juntar las elipses en una nube de puntos
trip_id = "H51_08"
cloud = get_cloud_from_trip_data(trip_id)
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

figure_path = f"diagrama_{trip_id}.png"
plt.savefig(figure_path, transparent=True)
