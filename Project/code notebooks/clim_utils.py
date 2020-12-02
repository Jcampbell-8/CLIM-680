import cartopy.crs as ccrs
import cartopy.mpl.ticker as cticker

def label_latlons(ax,lons,lats):

    """Set the Longitude and Latitude Labels for Plots"""
    
# Longitude labels
    ax.set_xticks(lons, crs=ccrs.PlateCarree())
    lon_formatter = cticker.LongitudeFormatter()
    ax.xaxis.set_major_formatter(lon_formatter)

# Latitude labels
    ax.set_yticks(lats, crs=ccrs.PlateCarree())
    lat_formatter = cticker.LatitudeFormatter()
    ax.yaxis.set_major_formatter(lat_formatter)
    