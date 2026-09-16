def readfile(filename):
    data = {}
    file = open(filename, "r");
    i = 0;
    for line in file:
        currline = line.split();
        data[i] = currline;
        i += 1;
    file.close();
    return data;

def extractdetails(datafromfile):
    values = {}
    i = 0;
    while(datafromfile.get(i)):
        print(datafromfile.get(i))
        i += 1;

def main():
    val = input("Please enter the file with the email header");
    data = readfile(val);
    extractdetails(data);
main();
