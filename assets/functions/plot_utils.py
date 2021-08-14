import numpy as np
import matplotlib.pyplot as plt


class plot_utils:
    def __init__(self, img_data, title, num_pixels=10000, colors=None, centroids=None):
        self.img_data = img_data
        self.title = title
        self.num_pixels = num_pixels
        self.colors = colors
        self.centroids = centroids

    def colorSpace(self):
        if self.colors is None:
            self.colors = self.img_data

        rand = np.random.RandomState(42)
        index = rand.permutation(self.img_data.shape[0])[:self.num_pixels]
        colors = self.colors[index]
        R, G, B = self.img_data[index].T

        fig, ax = plt.subplots(1, 2, figsize=(15, 9), tight_layout=True)
        ax[0].scatter(R, G, color=colors, marker='.')
        ax[0].set(xlabel='Red', ylabel='Green', xlim=(0, 1), ylim=(0, 1))
        ax[1].scatter(R, B, color=colors, marker='.')
        ax[1].set(xlabel='Red', ylabel='Blue', xlim=(0, 1), ylim=(0, 1))
        fig.suptitle(self.title, size=28)

        if self.centroids is not None:
            ax[0].scatter(self.centroids[:, 0], self.centroids[:, 1], color='white', 
            marker='o', s=400, edgecolor='black')
            for i, c in enumerate(self.centroids):
                ax[0].scatter(c[0], c[1], marker='$%d$' % i, s=100, edgecolor='k')
            ax[1].scatter(self.centroids[:, 0], self.centroids[:, 2], color='white', 
            marker='o', s=400, edgecolor='black')
            for i, c in enumerate(self.centroids):
                ax[1].scatter(c[0], c[2], marker='$%d$' % i, s=100, edgecolor='k')

    

    def colorSpace3d(self):
        if self.colors is None:
            self.colors = self.img_data

        rand = np.random.RandomState(42)
        index = rand.permutation(self.img_data.shape[0])[:self.num_pixels]
        colors = self.colors[index]
        R, G, B = self.img_data[index].T

        fig = plt.figure(figsize=(15, 9), tight_layout=True)
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter3D(R, G, B, color=colors, marker='.')
        ax.set_xlabel('Red')
        ax.set_ylabel('Green')
        ax.set_zlabel('Blue')
        fig.suptitle(self.title, size=28)