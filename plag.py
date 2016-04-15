#sudo pip install -U nltk
#python
#import nltk
#nltk.download()
#stopwords


#from difflib import SequenceMatcher
from nltk.corpus import stopwords
from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)
a=[]
b=[]
cachedStopWords = stopwords.words("english")



with open('file1.txt') as file_1:#, open('file2.txt') as file_2:
    file1_data = file_1.read()
   # file2_data = file_2.read()
    print file1_data
   # print file2_data

    file1_data = ' '.join([word for word in file1_data.split() if word not in cachedStopWords])
   # file2_data = ' '.join([word for word in file2_data.split() if word not in cachedStopWords])

    print "Removed Stop words:-----\n"
    print file1_data
  #  print file2_data
    
    #similarity_ratio = SequenceMatcher(None,file1_data,file2_data).ratio()
    #print similarity_ratio #plagiarism detected
def calplag(file1_data,text1):
	c=0
	val=0.0
	a=file1_data.split(" ")
	b=text1.split(" ")
	print len(a)
	print len(b)
	
	for i in range(0,len(b)):
		print b[i]
		for j in range(0,len(a)):
			print a[j]
			if b[i]==a[j]:
				c+=1;
				print c
				break;
				
	val=c*100
	val=val/len(b);
	print val
	return val
	
#calplag(file1_data,file2_data)
	   

@app.route('/')
def f():
    return render_template("p.html")

@app.route('/',methods=['POST'])
def g():
    text1 = request.form['text1']
    print text1
    text1 = ' '.join([word for word in text1.split() if word not in cachedStopWords])
    print("after stop words removed:",text1)
    val1=calplag(file1_data,text1)
    print val1
    #similarity_ratio = SequenceMatcher(None,file1_data,text1).ratio()
    
    return "Plagiarism: "+str(val1)
    
if __name__ == '__main__':
    app.run('192.168.2.4',debug=True)
