import urllib.request
import json

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
        currline = [word.replace(",", "") for word in currline]
        data[i] = currline;
        i += 1;
    data[i] = "THE FILE IS OVER NOW"
    file.close();
    return data;

def extractdetails(datafromfile):
    values = {}
    i = 0;
    while(datafromfile.get(i) != "THE FILE IS OVER NOW"):
        list = datafromfile.get(i);
        if(values.get("Server")):
            values["IP"] = list[list.index(values.get("Server")) + 1]
        if("from" in list):
            values["Server"] = list[list.index("from") + 1] + "."
        if("by" in list):
            values["Destination"] = list[list.index("by") + 1]
        if("with" in list):
            values["Protocol"] = list[list.index("with") + 1]
        if(("Mon" in list) or ("Tue" in list) or ("Wed" in list) or ("Thu" in list) or ("Fri" in list) or ("Sat" in list) or ("Sun" in list)):
            days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
            for day in days:
                if(day in list):
                    values["Timestamp"] = list[list.index(day)]+ " " + list[list.index(day) + 1] + " " + list[list.index(day) + 2] + " " + list[list.index(day) + 3] + " " + list[list.index(day) + 4]
        i += 1;
    return values;

def check_ip(ip):
    url = f"http://ip-api.com/json/{ip}"
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read())

    info = check_ip("8.8.8.8")
    print(info["city"], info["country"], info["isp"])

def main():
    val = input("Please enter the file with the email header:\n");
    data = readfile(val);
    values = extractdetails(data);
    for key in values:
        print(key + ": " + values.get(key) + "\n")
    check_ip(values.get("IP"));
main();
