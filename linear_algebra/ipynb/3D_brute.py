
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
#import seaborn as sns
#sns.set_style("whitegrid")
fig = plt.figure()
np.random.seed(3)

ax = fig.add_subplot(111, projection='3d')
ax._axis3don = False
ax.plot(np.zeros(3),np.array(range(-1,2)),np.zeros(3),"k-")
ax.plot(np.array(range(-1,2)),np.zeros(3),np.zeros(3),"k-")
ax.plot(np.zeros(3),np.zeros(3),np.array(range(-1,2)),"k-")

ax.set_xlim([-0.5,0.5])
ax.set_ylim([-0.5,0.5])
ax.set_zlim([-0.5,0.5])
ax.set_xticks([-1,-0.5,0,0.5,1])
ax.set_xticklabels([],fontsize=20)
ax.set_yticks([-1,-0.5,0,0.5,1])
ax.set_yticklabels([],fontsize=20)
ax.set_zticks([-1,-0.5,0,0.5,1])
ax.set_zticklabels([],fontsize=20)
ax.text(1.05,0,0,"$D_1$",fontsize=17)
ax.text(0,1.05,0,"$D_2$",fontsize=17)
ax.text(0,0,1.05,"$D_3$",fontsize=17)
ax.text(-0.1,-0.01,0.01,"$\mathcal{O}$",fontsize=20)

centroid3 = 0
centroid1 = 0
centroid2 = 0
# Plot cluster 1
nb_points = 70
color_cluster_1 = "darkred"
#ax.plot(np.random.randn(nb_points)*0.1-0.5,np.random.randn(nb_points)*0.05-0.5,np.random.randn(nb_points)*0.05-0.5,"ko",markersize=2.5,alpha=0.2)
if centroid1:
	ax.plot([-0.5],[-0.5],[-0.5],"X",color=color_cluster_1,markersize=10)
	ax.plot([-0.5,-0.5],[-0.5,-0.5],[-0.5,0],"--",color=color_cluster_1)
	ax.plot([-0.5,0],[-0.5,-0.5],[0,0],"--",color=color_cluster_1)
	ax.plot([-0.5,-0.5],[-0.5,0],[0,0],"--",color=color_cluster_1)
	#ax.plot([-0.5,0],[-0.5,-0.5],[-0.5,-0.5],"--",color=color_cluster_1)
	#ax.plot([-0.5,-0.5],[-0.5,0],[-0.5,-0.5],"--",color=color_cluster_1)
	#ax.plot([0,0],[-0.5,-0.5],[-0.5,0],"--",color=color_cluster_1)
	#ax.plot([-0.5,-0.5],[0,0],[-0.5,0],"--",color=color_cluster_1)
	if 1:
		ax.plot([0,-0.5],[0,0],[0,0],"-",color=color_cluster_1,linewidth=3.5)
		ax.plot([0,0],[0,-0.5],[0,0],"-",color=color_cluster_1,linewidth=3.5)
		ax.plot([0,0],[0,0],[0,-0.5],"-",color=color_cluster_1,linewidth=3.5)
	ax.text(-0.65,-0.65,-0.65,"$\mathcal{C}_1$",fontsize=20,color=color_cluster_1)

color_cluster_2 = "darkblue"
#ax.plot(np.random.randn(nb_points)*0.001-0.0,np.random.randn(nb_points)*0.21+0.5,np.random.randn(nb_points)*0.21-0,"ko",markersize=2.5,alpha=0.2)
if centroid2:
	ax.plot([0],[0.5],[0],"X",color=color_cluster_2,markersize=7)
	ax.text(-0.05,0.5,0.1,"$\mathcal{C}_2$",fontsize=13,color=color_cluster_2)
	#ax.plot([0,0],[0,0.5],[0,0],"-",color=color_cluster_2,markersize=17,linewidth=3.5)
	#ax.text(-0.05,0.2,0.1,"$x$",fontsize=17,color=color_cluster_2)


color_cluster_3 = "darkgreen"
#ax.plot(np.random.randn(nb_points)*0.02+0.8,np.random.randn(nb_points)*0.02-0.4,np.random.randn(nb_points)*0.41-0,"ko",markersize=2.5,alpha=0.2)
if centroid3:
	ax.plot([0.8],[-0.4],[0],"X",color=color_cluster_3,markersize=7)
	ax.text(0.7,-0.5,-0.1,"$\mathcal{C}_3$",fontsize=13,color=color_cluster_3)
	ax.plot([0,0.8],[-0.4,-0.4],[0,0],"--",color=color_cluster_3)
	ax.plot([0.8,0.8],[0,-0.4],[0,0],"--",color=color_cluster_3)

plt.tight_layout()
plt.savefig("3D_brute.pdf",bbox_inches='tight')
#plt.show()