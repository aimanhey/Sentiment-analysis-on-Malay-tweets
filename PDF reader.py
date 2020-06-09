import os
from PyPDF2 import PdfFileWriter, PdfFileReader
from fpdf import FPDF
from prettytable import PrettyTable
import shutil
import sys
#from reportLab.pdfgen import canvas

#createfolder
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)
createFolder('.Desktop/Like_a_fool')

#create subfolderrr
for i in range(1,9):
    os.makedirs(os.path.join('Like_a_fool', 'subfolder' + str(i)))

# Creates a pdf and MOVE to subfolder
#for i in range(1,10):
doc= FPDF()
doc.add_page()
doc.output("TW.pdf")
output = PdfFileWriter()

shutil.move("C:\\Users\\USER\\Desktop\\TW.pdf", "C:\\Users\USER\\Desktop\\Like_a_fool\\subfolder1\\TW.pdf")
#c=canvas.Canvas(str("TWICE.pdf"))
#c.save()

#gets=input("Your path directory:")

#Read pdf page line by line
#file = open('TW.pdf', 'rb')
gets = "C:\\Users\\USER\\Desktop"
print(" Read the path...")
i=0

#createTable
x = PrettyTable()



#directory = os.fsencode(str(gets))
for file in os.listdir(gets):

    count1=0
    count2=0
    count3=0
    count4=0
    count5=0
    count6=0
    if file.endswith(".pdf"):
        print("This is pdf")
        jut=os.path.join(gets, file)
       # print(str(file))
        input1 = PdfFileReader(open(str(jut),'rb'))
        page  = input1.numPages
        #page  = input1.getNumPages()
       # print(input1.getPage(0).mediaBox)
          

    #sum=0   
        for page in range(page):
            ket=input1.getPage(page).mediaBox
            print(ket)
            ret = ket.upperRight

            print ("RET: " + str(ret[0]))
            typ = ''
            

            if ret[0] >= 2383 and ret[0] <= 2384: 
                typ = 'A0'
                count1+=1
            elif ret[0] >= 1683 and ret[0] <= 1684:     
                typ = 'A1'   
                count2+=1 
            elif ret[0] >= 1190 and ret[0] <= 1191:     
                typ = 'A2'    
                count3+=1
            elif ret[0] >= 1190 and ret[0] <= 1191:     
                typ = 'A3'  
                count4+=1
            elif ret[0] >= 595 and ret[0] <= 596:     
                typ = 'A4'
                count5+=1
            elif ret[0] >= 419 and ret[0] <= 421:     
                typ = 'A5'   
                count6+=1
             
           # sum= sum + i
            #print (typ)
            #x.field_names = ["PDF file name","Paper format","Page"]
            x.field_names = ["PDF file name","A0","A1","A2","A3","A4","A5"]
            
            #x.add_row(typ.page('x'))
        x.add_row([str(file),count1,count2,count3,count4,count5,count6])
        sys.stdout=open('output.txt','wt')
        print(x)
       # from tabulate import tabulate
        #f = open("myfile.txt", "w")
        #f.write(tabulate(x))
        #f.write(x)
        
        

        
    #else:
        #print('not pdf')




