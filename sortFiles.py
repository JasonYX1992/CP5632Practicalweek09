import os, shutil

os.chdir('FilesToSort')

for filename in os.listdir('.'):

    data = os.path.splitext(filename)
    data2 = data[1].replace('.', '')

    if not os.path.isdir(data2):
        os.mkdir(data2)
    shutil.move(filename, data2)