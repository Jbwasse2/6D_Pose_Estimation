#Usage #python --log_directory ./logs
#Will create a plot with matplotlib for the average distance across time
import argparse
import glob
from os import path
import re
from matplotlib import pyplot as plt
import pudb
#Takes as input path to a log file and returns that last line of the file
def get_last_line(log_path):
    assert(path.isfile(log_path))
    with open(log_path) as f:
        for line in f:
            pass
        last_line = line
    return last_line

#Sorts input in human readable form (sorts by number and alphabet ordering)
#IE epoch_1_log.txt, epoch_2_log.txt, ..., tpoch_n_log.txt
#https://stackoverflow.com/questions/4836710/is-there-a-built-in-function-for-string-natural-sort
def natural_sort(l): 
    convert = lambda text: int(text) if text.isdigit() else text.lower() 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)

parser = argparse.ArgumentParser()
parser.add_argument('--log_directory', type=str, help='path to log directory')
parser.add_argument('--plot_name', type=str, default='output.png', help='output plot name')
opt = parser.parse_args()

log_directory = opt.log_directory
assert(log_directory is not None)
assert(path.isdir(log_directory))

#Create generator to iterate over all txt files with test in its name and that ends with txt
filepaths = natural_sort(glob.iglob(log_directory + '/*test*.txt'))
number_of_files = 0
distances = []
for filepath in filepaths :
    number_of_files += 1
    last_line = get_last_line(filepath)
    #Use regular expression to match to a number at the end of a file with a decimal
    r = re.compile(r'\d+.\d+$')
    distances.append(float(r.findall(last_line)[0]))
print("Number of files in path = ", number_of_files)

#Create plot for image
#0 to 0.02
fig, ax = plt.subplots()
ax.set_ylim([0,0.02])
plt.plot(range(number_of_files), distances)
plt.xlabel('Epoch')
plt.ylabel('Distance')
plt.title('Mean L2 Distance Between Reference \n and Source Point Clouds')
fig.savefig(opt.plot_name, bbox_inches='tight')
