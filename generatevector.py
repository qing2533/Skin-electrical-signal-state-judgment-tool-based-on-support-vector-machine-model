import getattr
import csv
import os

def generate_vector():
    baseline = []
    amusement = []
    stress = []

    path_dir = os.listdir(os.path.join('data', '1baseline'))
    for file in path_dir:
        full_name = os.path.join('data', '1baseline', file)
        with open(full_name, 'r') as f:
            reader = csv.reader(f)
            vector = [float(row[0]) for row in reader]
            vector = getattr.get_vector(vector)
            vector.append(1)
        baseline.append(vector)

    path_dir = os.listdir(os.path.join('data', '2amusement'))
    for file in path_dir:
        full_name = os.path.join('data', '2amusement', file)
        with open(full_name, 'r') as f:
            reader = csv.reader(f)
            vector = [float(row[0]) for row in reader]
            vector = getattr.get_vector(vector)
            vector.append(2)
        amusement.append(vector)

    path_dir = os.listdir(os.path.join('data', '3stress'))
    for file in path_dir:
       full_name = os.path.join('data', '3stress', file)
       with open(full_name, 'r') as f:
            reader = csv.reader(f)
            vector = [float(row[0]) for row in reader]
            vector = getattr.get_vector(vector)
            vector.append(3)
            stress.append(vector)

    with open('model\\amusement.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(amusement)

    with open('model\\baseline.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(baseline)

    with open('model\\stress.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(stress)


