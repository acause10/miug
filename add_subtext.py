# %%
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

# %%

img_1 = mpimg.imread('Plots/days_of_the_week.png')
img_2 = mpimg.imread('Plots/arrested_dist.png')
img_3 = mpimg.imread('Plots/knn_accuracy.png')
img_4 = mpimg.imread('Plots/nn_accuracy.png')
img_5 = mpimg.imread('Plots/classifier_acc.png')
img_6 = mpimg.imread('Plots/roc_curve.png')
img_7 = mpimg.imread('Plots/table_2.png')
img_8 = mpimg.imread('Plots/table_3.png')
img_9 = mpimg.imread('Plots/table_4.png')
img_10 = mpimg.imread('Plots/table_5.png')
img_11 = mpimg.imread('Plots/table_6.png')
img_12 = mpimg.imread('Plots/table_7.png')
img_13 = mpimg.imread('Plots/table_8.png')
img_14 = mpimg.imread('Plots/table_9.png')
img_15 = mpimg.imread('Plots/table_10.png')
img_16 = mpimg.imread('Plots/nn_layers.png')
img_17 = mpimg.imread('Plots/nn_units.png')

# %%
SMALL_SIZE = 8
MEDIUM_SIZE = 10
BIGGER_SIZE = 12

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

# %%
plt.imshow(img_1)

# %%
fig = plt.figure()
imgplot = plt.imshow(img_1)
plt.xlabel('Figure 1', fontsize=10)
plt.xticks([])
plt.yticks([])
plt.savefig('Plots/output_days_of_the_week.png', dpi=300)

# %%
fig = plt.figure()
imgplot = plt.imshow(img_2)
plt.xlabel('Figure 2', fontsize=10)
plt.xticks([])
plt.yticks([])
plt.savefig('Plots/output_arrested_dist.png', dpi=300)

# %%
fig = plt.figure()
imgplot = plt.imshow(img_3)
plt.xlabel('Figure 3', fontsize=10)
plt.xticks([])
plt.yticks([])
plt.savefig('Plots/output_knn_accuracy.png', dpi=300)

# %%
fig = plt.figure()
imgplot = plt.imshow(img_4)
plt.xlabel('Figure 4', fontsize=10)
plt.xticks([])
plt.yticks([])
plt.savefig('Plots/output_nn_accuracy.png', dpi=300)

# %%
fig = plt.figure()
imgplot = plt.imshow(img_5)
plt.xlabel('Table 1', fontsize=10)
plt.xticks([])
plt.yticks([])
plt.savefig('Plots/output_classifier_acc.png', dpi=300)

# %%
fig = plt.figure()
imgplot = plt.imshow(img_6)
plt.xlabel('Figure 5', fontsize=10)
plt.xticks([])
plt.yticks([])
plt.savefig('Plots/output_roc_curve.png', dpi=300)

# %%
fig = plt.figure()
imgplot = plt.imshow(img_7)
plt.xlabel('Table 2', fontsize=10)
plt.xticks([])
plt.yticks([])
plt.savefig('Plots/output_table_2.png', dpi=300)

# %%
fig = plt.figure()
imgplot = plt.imshow(img_8)
plt.xlabel('Table 3', fontsize=10)
plt.xticks([])
plt.yticks([])
plt.savefig('Plots/output_table_3.png', dpi=300)

# %%
fig = plt.figure()
imgplot = plt.imshow(img_9)
plt.xlabel('Table 4', fontsize=10)
plt.xticks([])
plt.yticks([])
plt.savefig('Plots/output_table_4.png', dpi=300)

# %%
fig = plt.figure()
imgplot = plt.imshow(img_10)
plt.xlabel('Table 5', fontsize=10)
plt.xticks([])
plt.yticks([])
plt.savefig('Plots/output_table_5.png', dpi=300)

# %%
fig = plt.figure()
imgplot = plt.imshow(img_11)
plt.xlabel('Table 6', fontsize=10)
plt.xticks([])
plt.yticks([])
plt.savefig('Plots/output_table_6.png', dpi=300)

# %%
fig = plt.figure()
imgplot = plt.imshow(img_12)
plt.xlabel('Table 7', fontsize=10)
plt.xticks([])
plt.yticks([])
plt.savefig('Plots/output_table_7.png', dpi=300)

# %%
fig = plt.figure()
imgplot = plt.imshow(img_13)
plt.xlabel('Table 8', fontsize=10)
plt.xticks([])
plt.yticks([])
plt.savefig('Plots/output_table_8.png', dpi=300)
# %%
fig = plt.figure()
imgplot = plt.imshow(img_14)
plt.xlabel('Table 9', fontsize=10)
plt.xticks([])
plt.yticks([])
plt.savefig('Plots/output_table_9.png', dpi=300)
# %%
fig = plt.figure()
imgplot = plt.imshow(img_15)
plt.xlabel('Table 10', fontsize=10)
plt.xticks([])
plt.yticks([])
plt.savefig('Plots/output_table_10.png', dpi=300)
# %%
fig = plt.figure()
imgplot = plt.imshow(img_16)
plt.xlabel('Figure 4.1', fontsize=10)
plt.xticks([])
plt.yticks([])
plt.savefig('Plots/output_nn_layers.png', dpi=300)
# %%
fig = plt.figure()
imgplot = plt.imshow(img_17)
plt.xlabel('Figure 4.2', fontsize=10)
plt.xticks([])
plt.yticks([])
plt.savefig('Plots/output_nn_units.png', dpi=300)
# %%
