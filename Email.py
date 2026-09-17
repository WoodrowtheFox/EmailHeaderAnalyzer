import urllib.request
import json
dates  = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];

def readfile(filename):
    email_data = {};
    textfile = open(filename, "r");
    i = 0;
    in_block = 0;
    block_key = 0;
    for line in textfile:
        currline = line.split();
        currline = [word.replace("(", "") for word in currline];
        currline = [word.replace(")", "") for word in currline];
        currline = [word.replace("[", "") for word in currline];
        currline = [word.replace("]", "") for word in currline];
        currline = [word.replace(",", "") for word in currline];
        if(in_block == 1):
                    email_data[block_key] = currline;
                    block_key += 1;
                    for day in dates:
                        if(day in currline):
                            in_block = 0;   
        if("Received:" in currline and "from" in currline):
            email_data[block_key] = currline;
            in_block = 1;
            block_key += 1;   
        i += 1;
    email_data[block_key] = "THE FILE IS NOW OVER"
    textfile.close();
    return email_data;

def extractdetails(emaildata):
    email_values = {}
    current_email_values = {}
    b = 0;
    h = 0;
    i = 0;
    while(emaildata.get(i) != "THE FILE IS NOW OVER"):
        currlist = emaildata.get(i);
        if(b == 0):
            current_email_values["Server"] = currlist[currlist.index("from") + 1];
            b += 1;
        elif(b == 1):
            current_email_values["IP"] = currlist[1];
            b += 1;
        elif(b == 2):
            current_email_values["Destination"] = currlist[currlist.index("by") + 1];
            b += 1;
        elif(b == 3 and "with" in currlist):
            current_email_values["Protocol"] = currlist[currlist.index("with") + 1];
            b += 1;
        for day in dates:
            if(day in currlist):
                current_email_values["Timestamp"] = currlist[currlist.index(day)]+ " " + currlist[currlist.index(day) + 1] + " " + currlist[currlist.index(day) + 2] + " " + currlist[currlist.index(day) + 3] + " " + currlist[currlist.index(day) + 4] + " " + currlist[currlist.index(day) + 5];
                email_values[h] = current_email_values;
                b = 0;
                h += 1;
                current_email_values = {};
        i += 1;
    return email_values;    

def check_ip(ip):
    url = f"http://ip-api.com/json/{ip}"
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read());

def main():
    emailheader = input("Please enter the file with the email header:\n");
    emaildata = readfile(emailheader);
    email_values = extractdetails(emaildata)

    for key in email_values:
            print("Hop: \n")
            for value in email_values.get(key):
                print(value + ": " + email_values.get(key).get(value) + "\n");
            info = check_ip(email_values.get(key).get("IP"));
            print("Location: " + info["city"] + ", " + info["regionName"] + ", " + info["country"]);

main();
