import streamlit as st
import pandas as pd

class SidebarTable: # for Focused Node and Selected Nodes
    def __init__(self, nodes_data, gdf):
        self.nodes_data = nodes_data
        self.gdf = gdf
        self.selected_nodes = []


class SidebarTable_Section:  # for totaling Section Node
    def __init__(self, nodes_data, gdf):
        self.nodes_data = nodes_data
        self.gdf = gdf
        self.selected_nodes = []


class Sidebar:
    def __init__(self, nodes_data, gdf):
        self.nodes_data = nodes_data
        self.gdf = gdf
        self.selected_nodes = []

    def render(self):
        
        # Sidebar content
        st.sidebar.title("Focused Node")
        self.display_focused_node_table("1")  # Example focused node data
        
        st.sidebar.title("Selected Nodes")
        # Enable selection toggle
        self.selection_enabled = st.sidebar.checkbox("Enable Node Selection", False, key="selection_toggle")
        self.display_selected_nodes_table()

        st.sidebar.title("Section")
        self.display_section_table()

    def display_focused_node_table(self, node_id):
        focused_node_data = [n for n in self.nodes_data if n["id"] == node_id]
        if focused_node_data:
            table = self.generate_table(focused_node_data)
            st.sidebar.dataframe(table)

    def display_selected_nodes_table(self):
        selected_nodes_data = [n for n in self.nodes_data if n["id"] in self.selected_nodes]
        if selected_nodes_data:
            selected_nodes_table = self.generate_table(selected_nodes_data)
            st.sidebar.dataframe(selected_nodes_table)

    def display_section_table(self):
        section_data = [n for n in self.nodes_data if n["id"] in ["1", "2"]]  # Example section data
        if section_data:
            section_table = self.generate_table(section_data)
            st.sidebar.dataframe(section_table)

    def generate_table(self, nodes_data):
        """Generates a simple table for the given nodes"""
        all_attributes = {}
        for node in nodes_data:
            for key, value in node["attributes"].items():
                if key not in all_attributes:
                    all_attributes[key] = {value}
                else:
                    all_attributes[key].add(value)

        table_data = []
        for attr, values in all_attributes.items():
            value_display = ", ".join(values) if len(values) > 1 else next(iter(values))
            table_data.append({"Enabled": True, "Attribute": attr, "Value": f"*{value_display}*" if len(values) > 1 else value_display})

        return pd.DataFrame(table_data)