import json
f=open("Rchilli-SampleJsonInput.txt",encoding="utf-8")
data=f.read()
f.close()
pd=json.loads(data)
#print(pd["data"][0])
print(f'Rchilli-Sample-Resume-output.txt started creating')
#######################################################################################################################
##################################### Starts Writing files ########################################################
f = open(f'Rchilli-Sample-Resume-output.txt','w',encoding="UTF-8")
f.write(f'Name : {pd["data"]["full_name"].capitalize()}\n\n')
##################################### Emails ##################################################
k=0
for i in range(len(pd["data"]["personal_emails"])):
    if k==0:
        f.write(f'Email :\n       {pd["data"]["personal_emails"][i]}\n')
        k=1
    else:
        f.write(f'       {pd["data"]["personal_emails"][i]}\n')
if k==1:
    for i in pd["data"]["emails"]:
        f.write(f'       {i["address"]}\n')
else:
    j=0
    for i in range(len(pd["data"]["emails"])):
        if j== 0:
            f.write(f'Email :\n       {pd["data"]["emails"][i]["address"]}\n')
            j = 1
        else:
            f.write(f'       {pd["data"]["emails"][i]["address"]}\n')

f.write('\n')
#################################### Phone #################################################
k=0
for i in pd["data"]["phone_numbers"]:
    if k==0:
        f.write(f'Phone:\n       {i}\n')
        k=1
    else:
        f.write(f'       {i}\n')
f.write('\n')

################################## ADDRESSS ######################################
cap = 0
f.write('Address: ')
splitting=pd["data"]["location_name"].split(', ')
if len(splitting)>2:
    for i in splitting:
        if cap==0:
            f.write(i.capitalize())
            cap=1
        else:
            f.write(f', {i.capitalize()}')
else:
    splitting=pd["data"]["location_name"].split(' ')
    for i in splitting:
        f.write(f' {i.capitalize()}')
cap=0
if pd["data"]["location_continent"]:
    splitting=pd["data"]["location_continent"].split()
    for i in splitting:
        if cap==0:
            f.write(f', {i.capitalize()}')
            cap=1
        else:
            f.write(f' {i.capitalize()}')


f.write('\n\n')
################################## Education ######################################
k = 0
for i in range(len(pd["data"]["education"])):
    if k == 0:
        cap=0
        splitting=pd["data"]["education"][i]["school"]["name"].split()
        for splitted in splitting:
            if cap==0:
                f.write(f'Education:\n        {splitted.capitalize()}')
                cap=1
            else:
                f.write(f' {splitted.capitalize()}')
        if pd["data"]["education"][i]["school"]["location"]:
            if pd["data"]["education"][i]["school"]["location"]["name"]:
                splitting_main = pd["data"]["education"][i]["school"]["location"]["name"].split(", ")
                if len(splitting_main) > 1:
                    for splitting in splitting_main:
                        if len(splitting.split()) > 1:
                            count1 = 0
                            for splitted in splitting.split():
                                if count1 == 0:
                                    f.write(f', {splitted.capitalize()}')
                                    count1 = 1
                                else:
                                    f.write(f' {splitted.capitalize()}')
                        else:
                            f.write(f', {splitting.capitalize()}')
                else:
                    splitting_main = pd["data"]["experience"][i]["school"]["location"]["name"].split(" ")
                    count1 = 0
                    for splitted in splitting.split():
                        if count1 == 0:
                            f.write(f', {splitted.capitalize()}')
                            count1 = 1
                        else:
                            f.write(f' {splitted.capitalize()}')

            f.write('\n')
            #f.write(f', {pd["data"]["education"][i]["school"]["location"]["name"].capitalize()}\n')
        else:
            f.write(f'\n')
        if pd["data"]["education"][i]["degrees"]:
            if pd["data"]["education"][i]["degrees"][1]:
                f.write(f'        {pd["data"]["education"][i]["degrees"][1].capitalize()}')
            if pd["data"]["education"][i]["degrees"][0]:
                f.write(f',{pd["data"]["education"][i]["degrees"][0].capitalize()}\n')
        if pd["data"]["education"][i]["start_date"]:
            f.write(f'        {pd["data"]["education"][i]["start_date"]}')
            if pd["data"]["education"][i]["end_date"]:
                f.write(f'-{pd["data"]["education"][i]["end_date"]}\n')
            else:
                f.write('\n')
        elif pd["data"]["education"][i]["end_date"]:
            f.write(f'        {pd["data"]["education"][i]["end_date"]}\n')
        k=1
    else:
        cap=0
        if pd["data"]["education"][i]["school"]["name"]:
            splitting = pd["data"]["education"][i]["school"]["name"].split()
            for splitted in splitting:
                if cap == 0:
                    f.write(f'        {splitted.capitalize()}')
                    cap = 1
                else:
                    f.write(f' {splitted.capitalize()}')
        if pd["data"]["education"][i]["school"]["location"]:
            if pd["data"]["education"][i]["school"]["location"]["name"]:
                splitting_main = pd["data"]["education"][i]["school"]["location"]["name"].split(", ")
                if len(splitting_main) > 1:
                    for splitting in splitting_main:
                        if len(splitting.split()) > 1:
                            count1 = 0
                            for splitted in splitting.split():
                                if count1 == 0:
                                    f.write(f', {splitted.capitalize()}')
                                    count1 = 1
                                else:
                                    f.write(f' {splitted.capitalize()}')
                        else:
                            f.write(f', {splitting.capitalize()}')
                else:
                    splitting_main = pd["data"]["experience"][i]["school"]["location"]["name"].split(" ")
                    count1 = 0
                    for splitted in splitting.split():
                        if count1 == 0:
                            f.write(f', {splitted.capitalize()}')
                            count1 = 1
                        else:
                            f.write(f' {splitted.capitalize()}')

            f.write('\n')
        else:
            f.write(f'\n')
        if pd["data"]["education"][i]["degrees"]:
            count=0
            for deg in reversed(pd["data"]["education"][i]["degrees"]):
                if count==0:
                    for deg1 in deg.split():
                        if count==0:
                            f.write(f'        {deg1.capitalize()}')
                            count=1
                        else:
                            f.write(f' {deg1.capitalize()}')
                else:
                    f.write(f', {deg.capitalize()}\n')

        if pd["data"]["education"][i]["start_date"]:
            f.write(f'        {pd["data"]["education"][i]["start_date"]}')
            if pd["data"]["education"][i]["end_date"]:
                f.write(f'-{pd["data"]["education"][i]["end_date"]}\n')
            else:
                f.write('\n')
        elif pd["data"]["education"][i]["end_date"]:
            f.write(f'        {pd["data"]["education"][i]["end_date"]}\n')
    f.write('\n')


################################## Experience #####################################
k = 0
for i in range(len(pd["data"]["experience"])):
    if k == 0:
        if pd["data"]["experience"][i]["company"]["name"]:
            cap=0
            for splitting in pd["data"]["experience"][i]["company"]["name"].split():
                if cap==0:
                    f.write(f'Experience:\n        {splitting.capitalize()}')
                    cap=1
                else:
                    f.write(f' {splitting.capitalize()}')
        #f.write(f'        {pd["data"]["experience"][i]["company"]["name"].capitalize()}')
        if pd["data"]["experience"][i]["company"]["location"]:
            if pd["data"]["experience"][i]["company"]["location"]["name"]:
                splitting_main = pd["data"]["experience"][i]["company"]["location"]["name"].split(", ")
                if len(splitting_main) > 1:
                    for splitting in splitting_main:
                        if len(splitting.split()) > 1:
                            count1 = 0
                            for splitted in splitting.split():
                                if count1 == 0:
                                    f.write(f', {splitted.capitalize()}')
                                    count1 = 1
                                else:
                                    f.write(f' {splitted.capitalize()}')
                        else:
                            f.write(f', {splitting.capitalize()}')

                else:
                    splitting_main = pd["data"]["experience"][i]["company"]["location"]["name"].split(" ")
                    count1 = 0
                    for splitted in splitting.split():
                        if count1 == 0:
                            f.write(f', {splitted.capitalize()}')
                            count1 = 1
                        else:
                            f.write(f' {splitted.capitalize()}')

        if pd["data"]["experience"][i]["start_date"]:
            f.write(f'        {pd["data"]["experience"][i]["start_date"]}')
            if pd["data"]["experience"][i]["end_date"]:
                f.write(f'-{pd["data"]["experience"][i]["end_date"]}\n')
            else:
                f.write('\n')
        elif pd["data"]["experience"][i]["end_date"]:
            f.write(f'        {pd["data"]["experience"][i]["end_date"]}\n')
        k=1
    else:
        if pd["data"]["experience"][i]["company"]["name"]:
            cap = 0
            for splitting in pd["data"]["experience"][i]["company"]["name"].split():
                if cap == 0:
                    f.write(f'        {splitting.capitalize()}')
                    cap = 1
                else:
                    f.write(f' {splitting.capitalize()}')
        #f.write(f'        {pd["data"]["experience"][i]["company"]["name"].capitalize()}')
        if pd["data"]["experience"][i]["company"]["location"]:
            if pd["data"]["experience"][i]["company"]["location"]["name"]:
                splitting_main = pd["data"]["experience"][i]["company"]["location"]["name"].split(", ")
                print(len(splitting_main))
                if len(splitting_main) > 1:
                    for splitting in splitting_main:
                        if len(splitting.split()) > 1:
                            count1 = 0
                            for splitted in splitting.split():
                                if count1 == 0:
                                    f.write(f', {splitted.capitalize()}')
                                    count1 = 1
                                else:
                                    f.write(f' {splitted.capitalize()}')
                        else:
                            f.write(f', {splitting.capitalize()}')
                else:
                    splitting_main = pd["data"]["experience"][i]["company"]["location"]["name"].split(" ")
                    count1 = 0
                    for splitted in splitting.split():
                        if count1 == 0:
                            f.write(f', {splitted.capitalize()}')
                            count1 = 1
                        else:
                            f.write(f' {splitted.capitalize()}')

        if pd["data"]["experience"][i]["start_date"]:
            f.write(f'        {pd["data"]["experience"][i]["start_date"].capitalize()}')
            if pd["data"]["experience"][i]["end_date"]:
                f.write(f'-{pd["data"]["experience"][i]["end_date"].capitalize()}\n')
            else:
                f.write('\n')
        elif pd["data"]["experience"][i]["end_date"]:
            f.write(f'        {pd["data"]["experience"][i]["end_date"].capitalize()}\n')

    if pd["data"]["experience"][i]["title"]:
        if pd["data"]["experience"][i]["title"]["name"]:
            cap=0
            for splitting in pd["data"]["experience"][i]["title"]["name"].split():
                if cap==0:
                    f.write(f'        {splitting.capitalize()}')
                    cap=1
                else:
                    f.write(f' {splitting.capitalize()}')
        f.write('\n')
    if k==1:
        f.write('\n')

#################################Skills#######################################
k=0
for i in range(len(pd["data"]["skills"])):
    if k==0:
        f.write(f'Skills:\n        {pd["data"]["skills"][i].capitalize()}')
        k=1
    else:
        f.write(f'\n        {pd["data"]["skills"][i].capitalize()}')
if k==1:
    f.write('\n')

f.write('\n')
################################# Interests ####################################
k=0
for i in range(len(pd["data"]["interests"])):
    if k==0:
        f.write(f'Interests:\n         {pd["data"]["interests"][i].capitalize()}')
        k=1
    else:
        f.write(f'\n         {pd["data"]["interests"][i].capitalize()}')
if k==1:
    f.write('\n')
f.write('\n')
#################################### Personal Information ########################
k=0
if k==0:
    f.write(f'Personal Information:\n         Gender : {pd["data"]["gender"].capitalize()}\n')
    k=1
for i in pd["data"]["profiles"]:
    if k==0:
        f.write(f'Personal Information:\n         {i["network"].capitalize()} : {i["url"]}\n')
        k=1
    else:
        f.write(f'         {i["network"].capitalize()} : {i["url"]}\n')



f.close()
print("created")