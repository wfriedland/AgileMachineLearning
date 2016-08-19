import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def wrapper_for_kmeans_wef(data, features):
    specialk = KMeans(n_clusters=3, init='random',precompute_distances=True, random_state=23, verbose=False )
    y_pred = specialk.fit_predict(data)

    # plot the points and visually detrmine if the centroids are positioned correctly
    fig = plt.figure(44, figsize=(12, 12))

    sp = plt.subplot(221)
    plt.autoscale(enable=True, axis='both',tight=False)
    plt.grid(True)

    plt.title("Pedal length vs width against KMean Prediction")
    sp.scatter(data[:,2],data[:,3],c=y_pred, color='yellow')
    sp.set_xlabel(features[2])
    sp.set_ylabel(features[3])

    sp2 = plt.subplot(222)
    sp2.scatter(data[:,0],data[:,1],c=y_pred, color='yellow')
    plt.title("Sepal length vs width agains KMean Prediction")
    sp2.set_xlabel(features[0])
    sp2.set_ylabel(features[1])

    sp3 = plt.subplot(223)
    sp3.scatter(data[:,2],data[:,3])
    plt.title("Pedal length vs width")
    sp3.set_xlabel(features[2])
    sp3.set_ylabel(features[3])

    sp4 = plt.subplot(224)
    sp4.scatter(data[:,0],data[:,1])
    plt.title("Sepal length vs width")
    sp4.set_xlabel(features[0])
    sp4.set_ylabel(features[1])
    plt.savefig("./KMeans_plot.jpg", dpi=None, facecolor='w', edgecolor='w',
                orientation='portrait', papertype=None, format=None,
                transparent=False, bbox_inches=None, pad_inches=0.1,
                frameon=None)
    return 100

