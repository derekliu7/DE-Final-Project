from geoplotlib.colors import create_set_cmap
from sklearn.cluster import KMeans
from geoplotlib.layers import BaseLayer
from geoplotlib.core import BatchPainter
import numpy as np


class KMeansLayer(BaseLayer):

    def __init__(self, data):
        self.data = data
        self.k = 15

    def invalidate(self, proj):
        self.painter = BatchPainter()
        x, y = proj.lonlat_to_screen(
            self.data['lon'], self.data['lat'])

        k_means = KMeans(n_clusters=self.k)
        k_means.fit(np.vstack([x, y]).T)
        labels = k_means.labels_

        self.cmap = create_set_cmap(set(labels), 'hsv')
        for l in set(labels):
            self.painter.set_color(self.cmap[l])
            self.painter.convexhull(x[labels == l], y[labels == l])
            self.painter.points(x[labels == l], y[labels == l], 2)

    def draw(self, proj, mouse_x, mouse_y, ui_manager):
        self.painter.batch_draw()
