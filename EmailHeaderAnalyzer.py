def readfile(input):
    with open("Email.txt", "w") as f:
        f.write(input)
    data = {};
    file = open("Email.txt", "r");
    i = 0;
    for line in file:
        data[i] = line;
        i += 1;
    file.close();
    return data;

def main():
    print("Please enter the filepath\n");
    data = readfile("Delivered-To: haiyang@d.umn.edu Received: by 2002:a05:6402:1907:0:0:0:0 with SMTP id e7csp4086589edzMon, 1 Feb 2021 08:44:25 -0800 (PST)" +
                    "X-Received: by 2002:a05:6638:1344:: with SMTP id u4mr15832375jad.86.1612197865113;" +
                    "Mon, 01 Feb 2021 08:44:25 -0800 (PST)" +
                    "Return-Path: <cox00133@d.umn.edu>" +
                    "Received: from mta-p8.oit.umn.edu" +
                    "(mta-p8.oit.umn.edu. [134.84.196.208])" +
                    "by mx.google.com" +
                    "with ESMTPS id o9si10466400ioo.93.2021.02.01.08.44.24" +
                    "for <haiyang@d.umn.edu>;" +
                    "Mon, 01 Feb 2021 08:44:25 -0800 (PST)" +
                    "Received-SPF: pass" +
                    "(google.com: domain of cox00133@d.umn.edu" +
                    "designates 209.85.166.70 as permitted sender)" +
                    "client-ip=209.85.166.70;" +
                    "Authentication-Results: mx.google.com;" +
                    "dkim=pass;" +
                    "spf=pass);" +
                    "for i in data: " +
                    "print(data[i]);");
main();
