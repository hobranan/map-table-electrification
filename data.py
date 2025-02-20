import pandas as pd
import geopandas as gpd
from shapely.geometry import Point

def load_data():
    # Sample node data with lat/lng and attributes
    nodes_data = [
        {"id": "1", "lat": 51.505, "lng": -0.09, "attributes": {"name": "Tree", "age": "5 years", "status": "Healthy"}},
        {"id": "2", "lat": 51.515, "lng": -0.1, "attributes": {"name": "House", "floors": "3", "status": "Renovated"}},
        {"id": "3", "lat": 51.520, "lng": -0.095, "attributes": {"name": "Car", "age": "2 years", "status": "New"}},
    ]

    # Convert to GeoDataFrame
    df = pd.DataFrame(nodes_data)
    df["geometry"] = df.apply(lambda row: Point(row["lng"], row["lat"]), axis=1)
    gdf = gpd.GeoDataFrame(df, geometry="geometry")
    
    return nodes_data, gdf