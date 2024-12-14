import osmnx as ox
import matplotlib.pyplot as plt
from shapely.geometry import box
import tkinter as tk
from tkinter import messagebox

def plot_map(north, south, east, west, edge_color, background_color, file_extension):
    # Create a polygon from the bounding box
    bbox = box(west, south, east, north)

    # Download the street network for the bounding box using the polygon
    graph = ox.graph_from_polygon(bbox, network_type='drive')

    # Convert the graph to GeoDataFrames for plotting
    nodes, edges = ox.graph_to_gdfs(graph)

    # Create a figure with the desired size (30x40 cm) at 300 DPI
    plt.figure(figsize=(11.8, 15.7), dpi=300)  # 30x40 cm in inches

    # Set the figure background color
    plt.gcf().set_facecolor(background_color)

    # Plot the edges (roads) of the network
    edges.plot(ax=plt.gca(), linewidth=0.5, color=edge_color)

    # Set the background color
    plt.gca().set_facecolor(background_color)

    # Remove axes
    plt.axis('off')

    # Add title and annotations with enhanced typography
    plt.title(f"Map of Area\nCoordinates: ({north}, {east}) to ({south}, {west})", fontsize=20, loc='center',color=edge_color)

    # Save the figure
    plt.savefig(f'road_map_poster.{file_extension}', bbox_inches='tight', dpi=300, format=file_extension)
    plt.show()

def on_submit():
    try:
        north = float(entry_north.get())
        south = float(entry_south.get())
        east = float(entry_east.get())
        west = float(entry_west.get())
        edge_color = edge_color_var.get()
        background_color = background_color_var.get()
        file_extension = file_extension_var.get()

        plot_map(north, south, east, west, edge_color, background_color, file_extension)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical coordinates.")

# Create the main window
root = tk.Tk()
root.title("Map Plotter")

# Create input fields for coordinates
tk.Label(root, text="North Latitude:").grid(row=0, column=0)
entry_north = tk.Entry(root)
entry_north.grid(row=0, column=1)

tk.Label(root, text="South Latitude:").grid(row=1, column=0)
entry_south = tk.Entry(root)
entry_south.grid(row=1, column=1)

tk.Label(root, text="East Longitude:").grid(row=2, column=0)
entry_east = tk.Entry(root)
entry_east.grid(row=2, column=1)

tk.Label(root, text="West Longitude:").grid(row=3, column=0)
entry_west = tk.Entry(root)
entry_west.grid(row=3, column=1)

# Create dropdown for edge color
tk.Label(root, text="Edge Color:").grid(row=4, column=0)
edge_color_var = tk.StringVar(value='black')  # Default value
edge_color_dropdown = tk.OptionMenu(root, edge_color_var, 'black', 'white')
edge_color_dropdown.grid(row=4, column=1)

# Create dropdown for background color
tk.Label(root, text="Background Color:").grid(row=5, column=0)
background_color_var = tk.StringVar(value='white')  # Default value
background_color_dropdown = tk.OptionMenu(root, background_color_var, 'black', 'white')
background_color_dropdown.grid(row=5, column=1)

# Create dropdown for file extension
tk.Label(root, text="File Extension:").grid(row=6, column=0)
file_extension_var = tk.StringVar(value='png')  # Default value
file_extension_dropdown = tk.OptionMenu(root, file_extension_var, 'png', 'jpg', 'svg')
file_extension_dropdown.grid(row=6, column=1)

# Create a submit button
submit_button = tk.Button(root, text="Plot Map", command=on_submit)
submit_button.grid(row=7, columnspan=2)

# Run the application
root.mainloop()
