# Import osmnx for and matplotlib
import osmnx as ox
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
import warnings
warnings.filterwarnings('ignore')

#Define the colormap
cmap = mcolors.LinearSegmentedColormap.from_list("blue_pink", ["#4DFFFD", "#ff6ec7"])

admin_district = ox.geocode_to_gdf('Osogbo, Osun')
admin_poly = admin_district.geometry.values[0]
admin_poly

footprints = ox.features_from_polygon(admin_poly, tags={"building": True})
print("Type of the footprints data:", type(footprints))
print("Number of buildings:", len(footprints))

# Create a plot to visualize the administrative boundary and building footprints
f, ax = plt.subplots(1, 1, figsize=(10, 10))

# Plot the administrative boundary
#admin_district.plot(ax=ax, color='none', edgecolor='k', alpha = 0.3, linewidth = 4)

# Plot the building footprints
footprints.plot(ax=ax, cmap = cmap,  alpha=0.99, linewidth = 1.0)

# Customize the plot
ax.axis('off')
f.patch.set_facecolor('black')