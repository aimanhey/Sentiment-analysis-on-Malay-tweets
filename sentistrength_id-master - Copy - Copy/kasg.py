
import json
import sys
import re
import nltk
import emoji
from collections import OrderedDict
import sentistrength_id as fl
import mysql.connector
import webbrowser
import urllib





def okay():
    config = json.loads(open('tweetshwe.json','r').read())
    print(len(config))
    non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
    ham=[]
    kuyms=[]
    for gur in range(len(config)) :
        kuy1=[]
        if config[gur]["lang"]=="in" or config[gur]["lang"]=="zsm" :
            kuys=(config[gur]["full_text"].encode('utf-16', 'surrogatepass').decode("utf-16"))
            date=(config[gur]["created_at"].encode('utf-16', 'surrogatepass').decode("utf-16"))
            kuy=""
            try:
            
                 if "RT " in kuys:
                     print(int(gur))
                     kuy=(config[gur]["retweeted_status"]["full_text"].encode('utf-16', 'surrogatepass').decode("utf-16"))
                     kam=config[gur]["retweeted_status"]["full_text"]
                 else:
                    print(int(gur))
                    kuy=(config[gur]["full_text"].encode('utf-16', 'surrogatepass').decode("utf-16"))
                    kam=config[gur]["full_text"]
            except:
                    print(int(gur))
                    kuy=(config[gur]["full_text"].encode('utf-16', 'surrogatepass').decode("utf-16"))
                    kam=config[gur]["full_text"]
                 
                 # kuy=config[gur][gelem].translate(non_bmp_map).encode('utf-16', 'surrogatepass').decode("utf-16")
        
            kuyms.append(kam)
            samantaro=emoji.demojize(kuy)
            #kuyms.append(samantaro)
            kuym=re.sub('salah satu','',samantaro)
            
            link_removed = re.sub(r"http\S+",'',kuym)
            lower_case_tweets= link_removed.lower()
            lower_case_tweet=re.sub(':',' ',lower_case_tweets)
            print(lower_case_tweet)
            print(date)
            tokens=nltk.tokenize.word_tokenize(lower_case_tweet)
            """tokens=[]
            for word in tokensx:
                try:
                    corrector=malaya.spell.probability()
                    wordd=corrector.correct(str(word),fast= True)
                    tokens.append(wordd)
                except:
                    tokens.append(word)
                    """
            #print(" ".join(tokens))  
            tokenss=[]
            print(tokenss)
            for word in tokens:
                matches=re.match(r'^(.*)(2|nye|,)$', word)
                #print(matches)
                if matches:
                    matchess=re.sub('(2|nye|,)$',"",word)
                    tokenss.append(str(matchess))
                else:
                    tokenss.append(word)
            tokenssd=[]    
            for tot in tokenss:
                et=wani(tot)
                tokenssd.append(et)
            tokenss=" ".join(tokenssd)
            if  "bukan biasa biasa" in tokenss:
                tokenss=re.sub(r'bukan biasa biasa',r'luar biasa', tokenss)
            else:
                tokenss=tokenss
            if  "tak pernah tak" in tokenss:                                                                                     #any(value in tokenss for value in ["tak", "tidak", "bukan"]):
                tokens=re.sub(r'tak pernah tak',r'', tokenss)
            else:
                tokens=tokenss
           
                
            #print(tokens)
            ham.append("".join(tokens))
            positiveWords=0
            negativeWords=0
            #print(tokenss)
            tokenssx=nltk.tokenize.word_tokenize(tokenss)
            #print("lko")
           # print(tokenssx)
           
         #   for word in tokenssx:
           #     if positiveList.count(word)==1:
             #       positiveWords+=1
                    #print(word)
               # if negativeList.count(word)==1: # if the word is a negative one
                 #   negativeWords+=1
                    #print(word)
           # print(positiveWords)
            #print(negativeWords)
            
            print(" ------------------------------------------------- ")
        else:
            print("")
    
        
       
    return ham,kuyms



def read(get,kuy,query):
    print("Bilangan " +str(len(get)))
    print("Bilangan " +str(len(kuy)))
    print(str(kuy))
    gets=get
    kuys=kuy
    """        
    for  saps in kuys:
        print(str(saps))
        print("sfdgvhbjnkmlxdfcvgbhjnkmsdfvgnj")
        """
    #print(kuys)\
    dia=[]
    print("Bilangan " +str(len(gets)))
    for sap in gets:
        print(" ")
        print(" ")
        printdf=(fl.senti.main(str(sap)))
        dia.append(printdf)
        print((printdf))

    dias=[]
    print("Bilangan " +str(len(kuys)))
    for sap in kuys:
        #gat=emoji.emojize(sap.encode('utf-16', 'surrogatepass').decode("utf-16"))
        non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
        gat=sap.translate(non_bmp_map).encode('utf-8', 'surrogatepass').decode("utf-8")
        print(str(sap))
        semah=tuple([gat])
        dias.append(semah)
        print(" _________________")

    guman=tuple(dia)
    gumant=tuple(dias)

    result = list(x + y for x, y in zip(guman, gumant))
    print(result)
    mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="sentiment")
    mycursor=mydb.cursor()
    sql ="INSERT INTO sentimen (score,kelas,tweet) VALUES (%s,%s,%s)"
    mycursor.executemany(sql,result)
    mydb.commit()
    print(mycursor.rowcount, "masuk dah.")
    data = urllib.parse.urlencode({'nama': query })
    data = data.encode('utf-8')
    request = urllib.request.Request("http://localhost//PhpProject2356//yeah1.php")
    request.add_header("Content-Type","application/x-www-form-urlencoded;charset=utf-8")
    f = urllib.request.urlopen(request, data)
    print(f.read().decode('utf-8'))
    webbrowser.open_new("http://localhost//kemas//asdf.php")

   
       
       
     

def getLexicons(positiveList, negativeList):
	## Open positive lexicon 
	positiveLex = open('C:\\Users\\Acer E Series\\Documents\\GitHub\\ID-OpinionWords\\positive.txt', encoding="utf-8")
	for words in positiveLex:
		words=words.rstrip("\n") # to eliminate the line break
		positiveList.append(words) # add the word to the list

	## Negative lexicon 
	negativeLex = open('C:\\Users\\Acer E Series\\Documents\\GitHub\\ID-OpinionWords\\negative.txt',  encoding="utf-8")
	for words in negativeLex:
		words=words.rstrip("\n") # to eliminate the line break
		negativeList.append(words) # add the word to the list

	## Negative lexicon 
	

            ## close the files
	positiveLex.close()
	negativeLex.close()
	
	

	return positiveList, negativeList
    
def negate_sequence(text):
    negation = False
    result = []
    delims = "?.,!:;"
    words = text.split()
    prev = None
    pprev = None
    for word in words:
        stripped = word.strip(delims)
        negated = "tak_" + stripped if negation else stripped
        result.append(negated)
        if prev:
            bigram = prev + " " + negated
            result.append(bigram)
            if pprev:
                trigram = pprev + " " + bigram
                result.append(trigram)
            pprev = prev
        prev = negated

        if any(neg in word for neg in ["tak", "tidak", "bukan"]):
            negation = not negation

        if any(c in word for c in delims):
            negation = False

    return result

def is_plural(text):
    negation = False
    result = []
    delims = "?.,!:;"
    words = text.split()
    prev = None
    pprev = None
    for word in words:
        stripped = word.strip(delims)
        negated = " kupasan_" + stripped if negation else stripped
        result.append(negated)
        if prev:
            bigram = prev + " " + negated
            result.append(bigram)
            if pprev:
                trigram = pprev + " " + bigram
                result.append(trigram)
            pprev = prev
        prev = negated

        if any(neg in word for neg in ["semakin"]):
            negation = not negation

        if any(c in word for c in delims):
            negation = False

    return result


def wani(term):
    sentiword_txt = [line.replace('\n','').split(":") for line in open("tidak.txt").read().splitlines()]
    sentiword_dict = OrderedDict()
    for terms in sentiword_txt:
        sentiword_dict[terms[0]] = str(terms[1])
    try:
        return sentiword_dict[term]
    except:
        return term
    

"""
positiveList=[]
negativeList=[]
getLexicons(positiveList, negativeList)
ham,kuym=okay(positiveList, negativeList)
read(ham,kuym)

"""




#range(len(config))
   #config = (config.decode("raw_unicode_escape").encode('utf-16', 'surrogatepass').decode('utf-16'))
#print(config)
#print(config[0]["full_text"])
   #if(config[gur]["retweeted_status"]["full_text"]):
     #   kuy=config[gur]["retweeted_status"]["full_text"].translate(non_bmp_map)
    #else:


  # kuy=config[gur][gelem].translate(non_bmp_map).encode('utf-16', 'surrogatepass').decode("utf-16")
#.translate(non_bmp_map)

 #user_removed = re.sub(r'@[A-Za-z0-9]+','',kuy)

#C:\\Users\\Acer E Series\\AppData\\Local\\Programs\\Python\\Python37-32\\tweetsh.json

   #print(kuy + " \n")
    #r1=re.match("RT",kuy)
    #print(r1)

    #if(kuy.find("RT")==-1):
     #   print("hello")
    #else:
      #  print("hi")

#
    
#with open('C:\\Users\\Acer E Series\\AppData\\Local\\Programs\\Python\\Python37-32\\tweetsh.json', 'r') as j:
#    json_data = json.loads(j)
 #   print((json_data.['full_text']))
     

