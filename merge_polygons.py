#!/usr/bin/env python3
'''
Merge touching polygons w/ geopandas
'''
import geopandas as gpd
import sys

gf1 = gpd.read_file(sys.argv[1])
gf2 = gpd.read_file(sys.argv[2])

# In case geometry is multipolygon (like washington), just take convex_hull
gf1['geometry'] = gf1.geometry.convex_hull
gf2['geometry'] = gf2.geometry.convex_hull

# geoseries is just geometry
gs = gf1.geometry.union(gf2.geometry)
gs.to_file('merged.shp')
