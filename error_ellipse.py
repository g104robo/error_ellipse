# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import math
from matplotlib import ticker

fig = plt.figure()
ax = plt.axes()

#問題1の誤差分散行列
# sigmap = np.array([[2.5,1.5],[1.5,2.5]])
# sigmap_offset=(20.0,5.0)
# sigmaf = np.array([[13.0/7.0,3.0/7.0],[3.0/7.0,5.0/7.0]])
# sigmaf_offset=(26.0,15.0)
# sigmas = np.array([[0.0,0.0],[0.0,1.0]])
# sigmas_offset=(23.0,24.0)


#問題2の誤差分散行列
sigmap = np.array([[2.5,1.5],[1.5,2.5]])
sigmap_offset=(20.0,5.0)
sigmaf = np.array([[5.0/2.0,3.0/2.0],[3.0/2.0,5.0/2.0]])
sigmaf_offset=(20.0,5.0)

#固有値、固有ベクトルの計算
sigmap_eigenval, sigmap_eigenvec = np.linalg.eig(sigmap)
sigmap_rad = np.arctan2(sigmap_eigenvec[0][0], sigmap_eigenvec[1][0])
sigmaf_eigenval, sigmaf_eigenvec = np.linalg.eig(sigmaf)
sigmaf_rad = np.arctan2(sigmaf_eigenvec[0][0], sigmaf_eigenvec[1][0])
# sigmas_eigenval, sigmas_eigenvec = np.linalg.eig(sigmas)
# sigmas_rad = np.arctan2(sigmas_eigenvec[0][0], sigmas_eigenvec[1][0])

#楕円の生成
sigmap_ell = patches.Ellipse(xy=sigmap_offset, width=sigmap_eigenval[0], height=sigmap_eigenval[1], angle=math.degrees(sigmap_rad), fc='b', ec='y', fill=False, label='sigma_p' )
sigmaf_ell = patches.Ellipse(xy=sigmaf_offset, width=sigmaf_eigenval[0], height=sigmaf_eigenval[1], angle=math.degrees(sigmaf_rad), fc='b', ec='b', fill=False, label='sigma_f')
#sigmas_ell = patches.Ellipse(xy=sigmas_offset, width=1000.0, height=2.0, angle=0.0, fc='b', ec='g', fill=False, label='sigma_s')

ax.add_patch(sigmap_ell)
ax.add_patch(sigmaf_ell)
#ax.add_patch(sigmas_ell)

plt.axis('scaled')
ax.set_aspect('equal')
ax.grid(which='major', color='k', linestyle='--', linewidth=1)

# ax.set_xlim(18, 27)
# ax.set_ylim(0, 26)
ax.yaxis.set_major_locator(ticker.MultipleLocator(1.0))           # 1.0ごと
plt.xlabel('x[cm]')
plt.ylabel('y[cm]')
plt.legend(loc='lower right')
plt.show()


