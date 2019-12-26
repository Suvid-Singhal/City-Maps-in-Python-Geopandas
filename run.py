import geopandas
import matplotlib.pyplot as plt
%matplotlib qt

baghdad_roads=geopandas.read_file("Baghdad\\roads.shp")
baghdad_natural=geopandas.read_file('Baghdad\\natural.shp')
baghdad_waterways=geopandas.read_file('Baghdad\\waterways.shp')

SanFransisco_roads=geopandas.read_file("SanFrancisco\\roads.shp")
SanFransisco_natural=geopandas.read_file('SanFrancisco\\natural.shp')
SanFransisco_waterways=geopandas.read_file('SanFrancisco\\waterways.shp')

Melbourne_roads=geopandas.read_file("Melbourne\\roads.shp")
Melbourne_natural=geopandas.read_file('Melbourne\\natural.shp')
Melbourne_waterways=geopandas.read_file('Melbourne\\waterways.shp')

Seoul_roads=geopandas.read_file("Seoul\\roads.shp")
Seoul_natural=geopandas.read_file('Seoul\\natural.shp')
Seoul_waterways=geopandas.read_file('Seoul\\waterways.shp')

Victoria_roads=geopandas.read_file("Victoria\\roads.shp")
Victoria_natural=geopandas.read_file('Victoria\\natural.shp')
Victoria_waterways=geopandas.read_file('Victoria\\waterways.shp')


fig, axs = plt.subplots(2, 3, figsize=(100,100))
for x in axs.ravel():
    x.axis("off")

ax1 = axs[0,0]

baghdad_roads.plot(ax=ax1, color='y')
baghdad_natural.plot(ax=ax1, color='g')
baghdad_waterways.plot(ax=ax1, color='b')
ax1.set_title("Baghdad")

ax2 = axs[0,1]

SanFransisco_roads.plot(ax=ax2, color='y')
SanFransisco_natural.plot(ax=ax2, color='g')
SanFransisco_waterways.plot(ax=ax2, color='b')
ax2.set_title("San Francisco")

ax3 = axs[0,2]

Melbourne_roads.plot(ax=ax3, color='y')
Melbourne_natural.plot(ax=ax3, color='g')
Melbourne_waterways.plot(ax=ax3, color='b')
ax3.set_title("Melbourne")

ax4 = axs[1,0]

Seoul_roads.plot(ax=ax4, color='y')
Seoul_natural.plot(ax=ax4, color='g')
Seoul_waterways.plot(ax=ax4, color='b')
ax4.set_title("Seoul")

ax5 = axs[1,2]

Victoria_roads.plot(ax=ax5, color='y')
Victoria_natural.plot(ax=ax5, color='g')
Victoria_waterways.plot(ax=ax5, color='b')
ax5.set_title("Victoria")

axs[1,1].set_visible(False)

plt.show()
