import folium
from shapely.geometry import Point
from streamlit_folium import st_folium
import streamlit as st

class Map:
    def __init__(self, gdf, nodes_data):
        self.gdf = gdf
        self.nodes_data = nodes_data
        self.selected_nodes = []

    def render(self):
        m = self.create_map()
        map_data = st_folium(m, height=500, width=700)
        
        if map_data:
            self.handle_click(map_data)

    def create_map(self):
        m = folium.Map(location=[51.505, -0.09], zoom_start=13)

        # Add Markers
        for _, row in self.gdf.iterrows():
            folium.Marker(
                location=[row["lat"], row["lng"]],
                popup=row["id"],
                tooltip=row["attributes"],
                icon=folium.Icon(color="blue" if row["id"] not in self.selected_nodes else "red")
            ).add_to(m)

        return m

    def handle_click(self, map_data):
        if "last_clicked" in map_data and map_data["last_clicked"]:
            clicked_id = str(map_data["last_clicked"]["popup"])
            self.select_node(clicked_id)

    def select_node(self, node_id):
        if node_id in self.selected_nodes:
            self.selected_nodes.remove(node_id)
        else:
            self.selected_nodes.append(node_id)