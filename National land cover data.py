#!/usr/bin/env python
# coding: utf-8

# <h3><center><font color='magenta'> Team Magenta </font></center></h3>

# <h4> Source of Data </h4>
# 
# <p4> https://data.tnris.org/ </p4>

# <h4> Import Libraries </h4>

# In[31]:


from osgeo import gdal, osr
import numpy as np
import os
import rasterio as rs
from rasterio.plot import show


# <h4> Set Working Directory </h4>

# In[32]:


os.chdir("C:/Users/Reena Shrestha/Desktop/Python/nlcd19_48_lc")
ds = gdal.Open('nlcd_2019_land_cover_l48_20210604_TX.img')


# <h4> Plot the image </h4>

# In[33]:


data = rs.open('nlcd_2019_land_cover_l48_20210604_TX.img')
rs.plot.show(data.read())


# <h4> Extracting data from band </h4>

# In[34]:


ds.RasterCount
band =  ds.GetRasterBand(1)
D = band.ReadAsArray()
D 


# <h4> Function to calculate the number of pixels of any class </h4>

# In[36]:


def Count(x):
    Count = np.count_nonzero(D == x)
    return(Count)


# <h4> Function to calculate the area any class </h4>

# In[37]:


def Area(Count):
    Area = round((Count*30*30)/2.56e+6,2)   # area in square miles
    return(Area)


# <h4> Calculate the total area </h4>

# In[52]:


Total_count = np.count_nonzero(D != -128)
Total_area = Area(Total_count)
Total_area


# <h4> Function to calculate the percentage area </h4>

# In[49]:


def Per(Area):
    Percent = (Area/Total_area)*100
    return(round(Percent,2))


# <h4> Calculate the area of openwater </h4>

# In[46]:


Count_openwater = Count(11)
Area_openwater = Area(Count_openwater)
Area_openwater


# <h4> Calculate the percentage area of openwater </h4>

# In[50]:


Per_openwater = Per(Area_openwater)
Per_openwater


# In[ ]:




