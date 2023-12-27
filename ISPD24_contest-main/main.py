import numpy as np

class Net:
    def __init__(self, name, access_points):
        self.name = name
        self.access_points = access_points

import numpy as np

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
                if current_net_name:  # save the previous net if there is one
                    nets[current_net_name] = access_points
                current_net_name = line
                access_points = []
            elif line.startswith("("):
                continue
            elif line.startswith(")"):
                if current_net_name:  # save the net when it's closed
                    nets[current_net_name] = access_points
                    current_net_name = ""
                    access_points = []
            else:
                # Remove characters that are not needed and split the remaining string
                clean_line = line.translate({ord(i): None for i in '[](),'})
                points = [int(i) for i in clean_line.split()]
                if points:  # if the line was not empty after cleaning
                    access_points.append(points)

    return nets


def main():
    cap_file = 'input/example.cap'
    net_file = 'input/example.net'
    output_file = 'output/example.PR_output'

    # Read the .cap and .net files
    cap_data = read_cap_file(cap_file)
    net_data = read_net_file(net_file)
    
    print(cap_data)
    print(net_data)

    # TODO: Process the data

    # Write the processed data to the .PR_output file
    with open(output_file, 'w') as file:
        file.write('This is an example output file.\n')

if __name__ == '__main__':
    main()
