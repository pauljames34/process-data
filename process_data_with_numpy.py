import numpy as np

file_path = 'Source/people.csv'

dtype = [('First Name', 'U50'), ('Family Name', 'U50'), ('Date of Birth', 'U50')]

data = np.genfromtxt(file_path, dtype=dtype, delimiter=',', skip_header=1)

print(data)