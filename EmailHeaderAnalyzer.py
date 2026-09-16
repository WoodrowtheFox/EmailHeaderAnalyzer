import urllib.request
import json

def readfile(filename):
    email_data = {};
    textfile = open(filename, "r");
    i = 0;
    for line in textfile:
        currline = line.split();
        currline = [word.replace("(", "") for word in currline];
        currline = [word.replace(")", "") for word in currline];
        currline = [word.replace("[", "") for word in currline];
        currline = [word.replace("]", "") for word in currline];
        currline = [word.replace(",", "") for word in currline];
        email_data[i] = currline;
        i += 1;
    email_data[i] = "THE FILE IS OVER NOW";
    textfile.close();
    return email_data;

def extractdetails(datafromfile):
    email_values = {}
    i = 0;
    while(datafromfile.get(i) != "THE FILE IS OVER NOW"):
        currlist = datafromfile.get(i);
        if(email_values.get("Server") in currlist):
            email_values["IP"] = currlist[currlist.index(email_values.get("Server")) + 1];
        if("from" in currlist):
            email_values["Server"] = currlist[currlist.index("from") + 1] + ".";
        if("by" in currlist):
            email_values["Destination"] = currlist[currlist.index("by") + 1];
        if("with" in currlist):
            email_values["Protocol"] = currlist[currlist.index("with") + 1];
        if(("Mon" in currlist) or ("Tue" in currlist) or ("Wed" in currlist) or ("Thu" in currlist) or ("Fri" in currlist) or ("Sat" in currlist) or ("Sun" in currlist)):
            days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];
            for day in days:
                if(day in currlist):
                    email_values["Timestamp"] = currlist[currlist.index(day)]+ " " + currlist[currlist.index(day) + 1] + " " + currlist[currlist.index(day) + 2] + " " + currlist[currlist.index(day) + 3] + " " + currlist[currlist.index(day) + 4];
        i += 1;
    return email_values;

def check_ip(ip):
    url = f"http://ip-api.com/json/{ip}"
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read());

def main():
    emailheader = input("Please enter the file with the email header:\n");
    emaildata = readfile(emailheader);
    email_values = extractdetails(emaildata);

    for key in email_values:
        print(key + ": " + email_values.get(key) + "\n");
    
    info = check_ip(email_values.get("IP"));
    print("Location: " + info["city"], ", " + info["regionName"] + ", " + info["country"]);

main();
