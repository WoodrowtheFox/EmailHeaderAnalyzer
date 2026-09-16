def readfile(filename):
    data = {}
    file = open(filename, "r");
    i = 0;
    for line in file:
        currline = line.split();
        currline = [word.replace("(", "") for word in currline]
        currline = [word.replace(")", "") for word in currline]
        currline = [word.replace("[", "") for word in currline]
        currline = [word.replace("]", "") for word in currline]
        data[i] = currline;
        i += 1;
    data[i] = "THE FILE IS OVER NOW"
    file.close();
    return data;

def extractdetails(datafromfile):
    values = {}
    i = 0;
    while(datafromfile.get(i) != "THE FILE IS OVER NOW"):
        if(values.get("Server") in datafromfile.get(i)):
            values["IP"] = datafromfile.get(i)[1]
        if("from" in datafromfile.get(i)):
            values["Server"] = datafromfile.get(i)[2] + "."
        if("by" in datafromfile.get(i) and len(datafromfile.get(i)) == 2):
            values["Destination"] = datafromfile.get(i)[1]
        if("with" in datafromfile.get(i) and len(datafromfile.get(i)) == 4):
            values["Protocol"] = datafromfile.get(i)[1]
        if("with" in datafromfile.get(i) and len(datafromfile.get(i)) == 4):
            values["Protocol"] = datafromfile.get(i)[1]
        i += 1;
    values["TimeStamp"] = datafromfile.get(14)[0]+ " " + datafromfile.get(14)[1] + " " + datafromfile.get(14)[2] + " " + datafromfile.get(14)[3] + " " + datafromfile.get(14)[4]
    return values;

def main():
    val = input("Please enter the file with the email header:\n");
    data = readfile(val);
    values = extractdetails(data);
    for key in values:
        print(key + ": " + values.get(key) + "\n")
main();
