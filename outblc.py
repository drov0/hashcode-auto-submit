def write_output(file, env):
    with open(file, 'w') as output_file:
        for vehicle in env['vehicles']:
            line = str(len(vehicle['rides'])) + " "
            if len(vehicle['rides']) > 0:
                rides = list()
                for ride in vehicle['rides']:
                    rides.append(str(ride))
                line += " ".join(rides)
            line += '\n'
            output_file.write(line)
