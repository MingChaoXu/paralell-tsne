
from sklearn import manifold
import matplotlib.pyplot as plt
import numpy as np
import mpl_toolkits.axisartist.axislines as axislines
import matplotlib as mpl
from cycler import cycler
from matplotlib.font_manager import FontProperties

# tsne_input = np.load('tsne/feature_ae-allattack.npy')
# target = np.load('tsne/target_ae-allattack.npy')
tsne_input = np.load('tsne/feature_resnet-allattack.npy')
target = np.load('tsne/target_resnet-allattack.npy')
print('tsne_input:', tsne_input.shape)
print('target:', target.shape)
# tsne = manifold.TSNE(n_components=2, init='pca', learning_rate=1000, random_state=0, perplexity=50, early_exaggeration=6.0)
# print("Computing t-SNE embedding")
# tsne_output = np.array(tsne.fit_transform(tsne_input))

# print('tsne_output:', tsne_output.shape)
# np.save('tsne/tsne_output_resnet.npy', tsne_output)
# np.save('tsne/tsne_output_type1.npy', tsne_output)
# colors = ['red', 'm', 'cyan', 'blue', 'lime']

tsne_output = np.load('tsne/tsne_output_resnet.npy')
# tsne_output = np.load('tsne/tsne_output_ae.npy')
print('tsne_output:', tsne_output.shape)
colors = ['#F08080', '#00FFFF', '#7B68EE', '#7FFF00']
# colors = ['lightcoral', 'cornflowervlue', 'lightgreen', 'moccasin']

cases = ['live', 'attack1', 'attack2', 'attack3']
# mpl.rcParams['axes.prop_cycle'] = cycler(cases, colors)

plt.switch_backend('agg')
figure, ax = plt.subplots(figsize=(6, 6))
# ax.xaxis.set_major_locator(MultipleLocator(10))
# ax.yaxis.set_major_locator(MultipleLocator(10))
# fig = plt.figure(figsize=(10, 6))

# font_prop = FontProperties()
# font_prop.set_family('Times')

font1 = {'family' : 'Times',
'weight' : 'normal',
'size'   : 23,
}

print('start plot:')
x_max = np.max(tsne_output[:,0], axis=0)
x_min = np.min(tsne_output[:,0], axis=0)
length_x = x_max-x_min
y_max = np.max(tsne_output[:,1], axis=0)
y_min = np.min(tsne_output[:,1], axis=0)
length_y = y_max - y_min
print('x_max:', x_max)
for i in range(len(colors)):
    px = []
    py = []
    #px2 = []
    #py2 = []

    #index = np.where(pred_all[:,] == i)

    for j in range(3000):
        x = tsne_output[j, 0]
        y = tsne_output[j, 1]
        # if x > x_max/2 :
        #     continue
        if target[j] == i :
            #plt.plot(tsne_output[j, 0], tsne_output[j, 1])
            px.append(x)
            py.append(y)
    print('px:', len(px))
    #if i == 0:
    A = plt.scatter(px, py, s=20, c=colors[i], label = cases[i], marker='o')
    #plt.scatter(px2, py2, s=20, c=colors[i], marker='v')
# plt.tick_params(labelsize=23)
plt.legend(handles=[A], prop=font1)
# plt.legend(np.arange(0,5).astype(str))
ax.set_yticks([])
ax.set_xticks([])
# ax.set_yticks([y_min, int(y_min+length_y/6), int(y_min+length_y/6*2), int(y_min+length_y/6*3), int(y_min+length_y/6*4), int(y_min+length_y/6*5), int(y_min+length_y/6*6)])
# ax.set_xticks([x_min, int(x_min+length_x/6), int(x_min+length_x/6*2), int(x_min+length_x/6*3), int(x_min+length_x/6*4), int(x_min+length_x/6*5), int(x_min+length_x/6*6)])
# plt.xticks(range(-40, 40))
# plt.yticks(range(-40, 40))
# plt.savefig('C:/Users/Day/Desktop/PPT_report/Galaxy pic/Visualization/2/cnn1_train.png', dpi=300, bbox_inches='tight')
# plt.savefig('tsne/tsne_output_ae_siwori.png', dpi=300,bbox_inches='tight')
plt.savefig('tsne/tsne_output_resnet_siwori.png', dpi=300,bbox_inches='tight')


