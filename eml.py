
#Note: Only supply the EML file and all other files will be created automatically
import email
import pandas as pd
import os
from email import policy
from email.parser import BytesParser
# Fname="It"  # give the file name here<<-------------------->>
# file_list = Fname+".eml"
currentDirectoy = os.getcwd()
os.chdir(currentDirectoy+"/emls")
email_list = os.listdir()
print(email_list)
for email in email_list:
    with open(email, 'rb') as fp:
        msg = BytesParser(policy=policy.default).parse(fp)
    text = msg.get_body(preferencelist=('plain')).get_content()

    txt = os.path.splitext(email)[0]+".txt"
    os.chdir(currentDirectoy + "/txtFiles")
    file = open(txt, "w")
    file.write(text)
    file.close()
    os.chdir(currentDirectoy + "/emls")
    csv = os.path.splitext(email)[0]+".csv"

    def sep_colon():
        os.chdir(currentDirectoy + "/txtFiles")
        data = pd.read_csv(txt, sep=":", error_bad_lines=False, header=None, engine='python')
        os.chdir(currentDirectoy+"/csvFiles")
        data.to_csv(csv)
        os.chdir(currentDirectoy + "/emls")

    def sep_space():
        os.chdir(currentDirectoy + "/txtFiles")
        data = pd.read_csv(txt, sep=" ",error_bad_lines=False, header=None,engine='python')
        os.chdir(currentDirectoy + "/csvFiles")
        data.to_csv(csv)
        os.chdir(currentDirectoy + "/emls")

    def sep_JAB_Special_chars():
        os.chdir(currentDirectoy + "/txtFiles")
        with open(txt, 'r') as infile,  \
             open('out.txt', 'w') as outfile:
            data = infile.read()
            data = data.replace("@", " ")
            data = data.replace("€ ", " ")
            data = data.replace("     ", " ")
            data = data.replace("   ", " ")
            # print(data)
            outfile.write(data)
        data = pd.read_csv('out.txt', sep=" ", error_bad_lines=False, header=None, engine='python')
        #print (data)
        os.chdir(currentDirectoy + "/csvFiles")
        data.to_csv(csv)
        os.chdir(currentDirectoy + "/emls")

    sep_colon()
    sep_space()
    sep_JAB_Special_chars()
