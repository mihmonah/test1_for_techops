import csv


def csv_to_args(scv_file_name):
"""
Function from this module takes data from .csv file and generate
list of tuples with this data.
"""
    csvfile = open(scv_file_name, newline='')
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    ids = []
    inputs = []
    outputs = []
    next(spamreader)
    for row in spamreader:
        id = row[0]
        input = row[1]
        output = row[2]
        ids.append(id)
        inputs.append(input)
        outputs.append(output)
    n_inp = ''
    for i in inputs:
        n_inp = n_inp + '+' + i[1:-1]
    inputs = n_inp.split('+')
    inputs = inputs[1:]
    n_out = ''
    for o in outputs:
        n_out = n_out + '+' + o[1:-1]
    outputs = n_out.split('+')
    outputs = outputs[1:]
    param = []
    x = 0
    while (x < len(inputs)):
        param.append((inputs[x], outputs[x]))
        x = x + 1
    return ([ids, param])
