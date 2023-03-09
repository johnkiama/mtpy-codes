import os, sys

def editedi(indir):
 #   os.chdir(indir)
    files = os.listdir(indir)
    for file in files:
        if file.endswith(".edi"):
            yield file

def display_files(path):
    my_files = editedi(path)
    for n in my_files:
        print(n)
        with open(os.path.join(path, n)) as f:
            reader = f.readlines()
            for lines in reader:
                lines = lines.strip()
                if lines.startswith("DATAID"):
                    data_val, station_name = lines.split("=")
                    print(data_val, station_name)
              
display_files("/home/seismics/mtpy-develop/data/edifiles")


