import pprint

def read_input(file):
    env = dict()
    with open(file, mode='r') as input_file:
        line = input_file.readline()
        line = line.strip('\n')
        ins = line.split(' ')
        env['globals'] = dict()
        env['globals']['n-rows'] = int(ins[0])
        env['globals']['n-columns'] = int(ins[1])
        env['globals']['n-vehicles'] = int(ins[2])
        env['globals']['n-rides'] = int(ins[3])
        env['globals']['bonus'] = int(ins[4])
        env['globals']['n-steps'] = int(ins[5])
        env['rides'] = list()
        env['vehicles'] = list()
        for n in range(env['globals']['n-rides']):
            line = input_file.readline()
            line = line.strip('\n')
            ins = line.split(' ')
            ride = dict()
            ride['start-row'] = int(ins[0])
            ride['start-column'] = int(ins[1])
            ride['end-row'] = int(ins[2])
            ride['end-column'] = int(ins[3])
            ride['earliest-start'] = int(ins[4])
            ride['latest-finish'] = int(ins[5])
            ride['id'] = n
            ride['completed'] = False
            env['rides'].append(ride)
        for n in range(env['globals']['n-vehicles']):
            vehicle = dict()
            vehicle['rides'] = list()
            vehicle['row'] = 0
            vehicle['column'] = 0
            vehicle['id'] = n
            vehicle['available'] = True
            vehicle['available-at-step'] = 0
            env['vehicles'].append(vehicle)
    return env

