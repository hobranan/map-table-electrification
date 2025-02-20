# import streamlit as st
# import pandas as pd
# import geopandas as gpd
# from shapely.geometry import Point, box
# from streamlit_folium import st_folium
# import folium

# # Sample node data
# nodes_data = [
#     {"id": "1", "lat": 51.505, "lng": -0.09, "attributes": {"name": "Tree", "age": "5 years", "status": "Healthy"}},
#     {"id": "2", "lat": 51.515, "lng": -0.1, "attributes": {"name": "House", "floors": "3", "status": "Renovated"}},
#     {"id": "3", "lat": 51.520, "lng": -0.095, "attributes": {"name": "Car", "age": "2 years", "status": "New"}},
# ]

# # Convert to GeoDataFrame
# df = pd.DataFrame(nodes_data)
# df["geometry"] = df.apply(lambda row: Point(row["lng"], row["lat"]), axis=1)
# gdf = gpd.GeoDataFrame(df, geometry="geometry")

# # Initialize session state
# if "selected_nodes" not in st.session_state:
#     st.session_state.selected_nodes = []
# if "focused_node" not in st.session_state:
#     st.session_state.focused_node = None

# # Function to handle node selection
# def select_node(node_id):
#     node_id = str(node_id)  # Ensure ID is a string
#     if st.session_state.focused_node == node_id:
#         st.session_state.focused_node = None  # Deselect if clicked again
#     else:
#         st.session_state.focused_node = node_id  # Set as focused node

#     if node_id in st.session_state.selected_nodes:
#         st.session_state.selected_nodes.remove(node_id)
#     else:
#         st.session_state.selected_nodes.append(node_id)

# # Function to handle drag box selection
# def select_within_box(bounds):
#     if not bounds or "southWest" not in bounds or "northEast" not in bounds:
#         return

#     min_lat, min_lng = bounds["southWest"]["lat"], bounds["southWest"]["lng"]
#     max_lat, max_lng = bounds["northEast"]["lat"], bounds["northEast"]["lng"]

#     selection_box = box(min_lng, min_lat, max_lng, max_lat)
#     selected = gdf[gdf.geometry.within(selection_box)]
    
#     st.session_state.selected_nodes = list(selected["id"].astype(str))

# # Create map
# m = folium.Map(location=[51.515, -0.1], zoom_start=13)

# # Add markers
# for _, row in gdf.iterrows():
#     icon_color = "blue"
#     if row["id"] in st.session_state.selected_nodes:
#         icon_color = "red"
#     if row["id"] == st.session_state.focused_node:
#         icon_color = "green"

#     folium.Marker(
#         location=[row["lat"], row["lng"]],
#         popup=row["id"],
#         tooltip=str(row["attributes"]),
#         icon=folium.Icon(color=icon_color),
#     ).add_to(m)

# # Display map
# map_data = st_folium(m, height=500, width=700)

# # Handle marker clicks safely
# if map_data and "last_clicked" in map_data and map_data["last_clicked"]:
#     if "popup" in map_data["last_clicked"]:  # ✅ Check if 'popup' exists
#         clicked_id = str(map_data["last_clicked"]["popup"])
#         select_node(clicked_id)

# # Handle drag box selection
# if map_data and "bounds" in map_data:
#     select_within_box(map_data["bounds"])

# # Function to create scrollable tables
# def create_scrollable_table(title, data):
#     st.sidebar.subheader(title)
#     if data:
#         df_table = pd.DataFrame(data)
#         st.sidebar.dataframe(df_table, height=200)
#     else:
#         st.sidebar.info(f"No data available for {title}")

# # **Focused Node Table**
# focused_node_data = []
# if st.session_state.focused_node:
#     node = next((n for n in nodes_data if n["id"] == st.session_state.focused_node), None)
#     if node:
#         focused_node_data = [{"Attribute": k, "Value": v} for k, v in node["attributes"].items()]

# # **Selected Nodes Table**
# selected_nodes_data = [n for n in nodes_data if n["id"] in st.session_state.selected_nodes]
# selected_nodes_table = []
# for node in selected_nodes_data:
#     for attr, value in node["attributes"].items():
#         selected_nodes_table.append({"Attribute": attr, "Value": value})

# # **Section Table (Placeholder)**
# section_data = [
#     {"Attribute": "Zone", "Value": "Residential"},
#     {"Attribute": "Risk Level", "Value": "Low"},
# ]

# # Display Tables in Sidebar
# create_scrollable_table("Focused Node", focused_node_data)
# create_scrollable_table("Selected Nodes", selected_nodes_table)
# create_scrollable_table("Section", section_data)

# import streamlit as st
# import pandas as pd
# import geopandas as gpd
# from shapely.geometry import Point, box
# from streamlit_folium import st_folium
# import folium

# # Sample node data with lat/lng and attributes
# nodes_data = [
#     {"id": "1", "lat": 51.505, "lng": -0.09, "attributes": {"name": "Tree", "age": "5 years", "status": "Healthy"}},
#     {"id": "2", "lat": 51.515, "lng": -0.1, "attributes": {"name": "House", "floors": "3", "status": "Renovated"}},
#     {"id": "3", "lat": 51.520, "lng": -0.095, "attributes": {"name": "Car", "age": "2 years", "status": "New"}},
# ]

# # Convert to GeoDataFrame
# df = pd.DataFrame(nodes_data)
# df["geometry"] = df.apply(lambda row: Point(row["lng"], row["lat"]), axis=1)
# gdf = gpd.GeoDataFrame(df, geometry="geometry")

# # Sidebar selection state
# if "selected_nodes" not in st.session_state:
#     st.session_state.selected_nodes = []
# if "selection_enabled" not in st.session_state:
#     st.session_state.selection_enabled = False

# # Toggle to enable/disable selection feature
# st.sidebar.checkbox("Enable Node Selection", value=st.session_state.selection_enabled, key="selection_toggle")

# # Function to add node to the selected list
# def add_to_selected(node_id):
#     if node_id not in st.session_state.selected_nodes:
#         st.session_state.selected_nodes.append(node_id)

# # Function to check for Ctrl+Click selection
# def select_node(node_id):
#     if node_id in st.session_state.selected_nodes:
#         st.session_state.selected_nodes.remove(node_id)
#     else:
#         st.session_state.selected_nodes.append(node_id)

# # Function to check for Drag Box selection
# def select_within_box(bounds):
#     if not bounds or "southWest" not in bounds or "northEast" not in bounds:
#         st.warning("No bounding box selection detected.")
#         return
    
#     # Extract corners of the selection box
#     min_lat, min_lng = bounds["southWest"]["lat"], bounds["southWest"]["lng"]
#     max_lat, max_lng = bounds["northEast"]["lat"], bounds["northEast"]["lng"]

#     selection_box = box(min_lng, min_lat, max_lng, max_lat)
    
#     selected = gdf[gdf.geometry.within(selection_box)]
#     st.session_state.selected_nodes = list(selected["id"])

# # Create Map
# m = folium.Map(location=[51.505, -0.09], zoom_start=13)

# # Add Markers
# for _, row in gdf.iterrows():
#     folium.Marker(
#         location=[row["lat"], row["lng"]],
#         popup=row["id"],
#         tooltip=row["attributes"],
#         icon=folium.Icon(color="blue" if row["id"] not in st.session_state.selected_nodes else "red")
#     ).add_to(m)

# # Display Map with Selection
# map_data = st_folium(m, height=500, width=700)

# # Handle click selection
# if map_data and "last_clicked" in map_data and map_data["last_clicked"]:
#     clicked_id = str(map_data["last_clicked"]["popup"])
#     if st.session_state.selection_enabled:
#         add_to_selected(clicked_id)
#     else:
#         select_node(clicked_id)

# # Handle drag box selection
# if map_data and "bounds" in map_data:
#     select_within_box(map_data["bounds"])

# # Function to generate table from selected nodes
# def generate_table(selected_nodes_data):
#     all_attributes = {}
#     for node in selected_nodes_data:
#         for key, value in node["attributes"].items():
#             if key not in all_attributes:
#                 all_attributes[key] = {value}
#             else:
#                 all_attributes[key].add(value)

#     table_data = []
#     for attr, values in all_attributes.items():
#         value_display = ", ".join(values) if len(values) > 1 else next(iter(values))
#         table_data.append({"Enabled": True, "Attribute": attr, "Value": f"*{value_display}*" if len(values) > 1 else value_display})

#     return pd.DataFrame(table_data)

# # Display tables in sidebar

# st.sidebar.title("Focused Node")
# focused_node_data = [n for n in nodes_data if n["id"] == "1"]  # Focus on a specific node for demonstration
# if focused_node_data:
#     focused_node_table = generate_table(focused_node_data)
#     st.sidebar.dataframe(focused_node_table)

# st.sidebar.title("Selected Nodes")
# selected_nodes_data = [n for n in nodes_data if n["id"] in st.session_state.selected_nodes]
# if selected_nodes_data:
#     selected_nodes_table = generate_table(selected_nodes_data)
#     st.sidebar.dataframe(selected_nodes_table)
#     st.sidebar.write("UUIDs of Selected Nodes:", [n["id"] for n in selected_nodes_data])

# st.sidebar.title("Section")
# section_data = [n for n in nodes_data if n["id"] in ["1", "2"]]  # Display example section data
# if section_data:
#     section_table = generate_table(section_data)
#     st.sidebar.dataframe(section_table)


import streamlit as st
from sidebar import Sidebar
from map import Map
from data import load_data

# Load Data
nodes_data, gdf = load_data()

# Load visual components
map_component = Map(gdf, nodes_data)
sidebar = Sidebar(nodes_data, gdf)
map_component.render()
sidebar.render()