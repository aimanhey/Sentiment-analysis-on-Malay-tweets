
from collections import OrderedDict

a=['as',"df", "baik"]

b=[]

for gem in a:
    sentiword_txt = [line.replace('\n','').split(":") for line in open("sentiwords_id.txt").read().splitlines()]
    sentiword_dict = OrderedDict()
    for terms in sentiword_txt:
        sentiword_dict[terms[0]] = int(terms[1])
    try:
        kling=sentiword_dict[gem]
        #return kling
    except:
        kling=0
       # return kling
    cap=gem +"\n" +"{}".format(kling)

    b.append([str(j) for j in cap.split()])

print(b)
