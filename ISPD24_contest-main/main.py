import numpy as np
from algorithm import a_star_search, Point3D
class Net:
    def __init__(self, name, access_points):
        self.name = name
        self.access_points = access_points

def read_cap_file(file_path):
    with open(file_path, 'r') as file:
        nLayers, xSize, ySize = map(int, file.readline().split())
        unit_costs = list(map(float, file.readline().split()))
        unit_length_wire_cost, unit_via_cost = unit_costs[:2]
        unit_length_short_costs = unit_costs[2:]
        
        hEdgeLengths = list(map(float, file.readline().split()))
        vEdgeLengths = list(map(float, file.readline().split()))
        
        capacity = np.zeros((nLayers, xSize, ySize))
        layerDirections = []
        layerMinLengths = []
        
        for l in range(nLayers):
            line = file.readline().strip()
            layer_name, direction, min_length = line.split()
            direction = int(direction)
            min_length = float(min_length)
            layerDirections.append(direction)
            layerMinLengths.append(min_length)
            
            for y in range(ySize):
                capacity[l, :, y] = list(map(float, file.readline().split()))
    
    return {
        'nLayers': nLayers,
        'xSize': xSize,
        'ySize': ySize,
        'unit_length_wire_cost': unit_length_wire_cost,
        'unit_via_cost': unit_via_cost,
        'unit_length_short_costs': unit_length_short_costs,
        'hEdgeLengths': hEdgeLengths,
        'vEdgeLengths': vEdgeLengths,
        'capacity': capacity,
        'layerDirections': layerDirections,
        'layerMinLengths': layerMinLengths
    }


def read_net_file(file_path):
    nets = {}
    with open(file_path, 'r') as file:
        current_net_name = ""
        access_points = []

        for line in file:
            line = line.strip()
            if line.startswith("Net"):
                if current_net_name:
                    nets[current_net_name] = access_points
                current_net_name = line
                access_points = []
            elif line.startswith("("):
                pass  
            elif line.startswith(")"):
                pass 
            else:
                access_point_strings = line.split('),')
                temp_points = []
                for point_str in access_point_strings:
                    clean_line = point_str.translate({ord(i): None for i in '[](),'})
                    points = [int(i) for i in clean_line.split()]
                    if points:
                        temp_points.append(points)
                if temp_points:
                    access_points.append(temp_points)

        if current_net_name:
            nets[current_net_name] = access_points

    return nets


def simple_routing_algorithm(net_pins):
    paths = []
        
    for i in range(len(net_pins) - 1):
        
        start = Point3D(net_pins[i][0][0], net_pins[i][0][1], net_pins[i][0][2])
        goal = Point3D(net_pins[i+1][0][0], net_pins[i+1][0][1], net_pins[i+1][0][2])
        path = a_star_search(start, goal)
        print(path)

        # Simplify the path
        simplified_path = []
        transformed_path = []
        j = 0
        while j < len(path):
            start = path[j]
            while j < len(path) - 1 and path[j][2] == path[j+1][2]:
                j += 1
            end = path[j]
            simplified_path.append((start[0], start[1], end[0], end[1], start[2]))
            transformed_path.append((start[0], start[1], end[0]+1, end[1]+1, start[2]))
            j += 1
            

        paths.append(transformed_path)
    
    return paths


def main():
    cap_file = 'input/example.cap'
    net_file = 'input/example.net'
    output_file = 'output/example.PR_output'

    # Read the .cap and .net files
    cap_data = read_cap_file(cap_file)
    net_data = read_net_file(net_file)
    
    print(cap_data)
    print(net_data)
    
    # Process the data for all nets
    net_paths = {}
    for net_name, net_pins in net_data.items():
        print("net pins", net_pins)
        net_paths[net_name] = simple_routing_algorithm(net_pins)
        
    # Write the processed data to the .PR_output file
    with open(output_file, 'w') as file:
        for net_name, paths in net_paths.items():
            file.write(f'{net_name}\n{{\n')
            for path in paths:
                # file.write(str(path))
                for point in path:
                    file.write(f'{point[0]} {point[1]} {point[2]} {point[3]} metal{point[4]}\n')
            file.write('}')

if __name__ == '__main__':
    main()
