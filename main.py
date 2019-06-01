import os                                                                                #required imports
from app import app
from flask import request,flash, redirect, render_template,send_from_directory
from werkzeug.utils import secure_filename
from sim_textrank import simTextRank
from cos_sim_textrank import cosineTextRank
from jaccard_sim_textrank import jaccardTextRank
from pos_textrank import posTextRank
from nltk.tokenize import sent_tokenize


ALLOWED_EXTENSIONS = set(['txt'])                                #allowed files

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/girija-mage.github.io/')                                                  #home page
def home():
    return render_template('index.html')


@app.route('/summarygenerator')
def summarygenerator():
	return render_template('summarygenerator.html')


@app.route('/summarygenerator', methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':                  #check if the post request has the file part
        if 'file' not in request.files:
            flash('No file')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)   
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))                      #save file at given location
            #flash('File uploaded successfully')
            #return redirect(request.url)
            
        with open(os.path.join(app.config['UPLOAD_FOLDER'], filename), "r",encoding="utf-8") as inFile:
            data = inFile.read()
                
        sentences = []
        sentences = sent_tokenize(data)
            
        size = len(sentences)                                                            #summary size
        no_of_sentences = 0
        if(size<30):
            flash('Small input...Select another file')
            return redirect(request.url)
        else:
            no_of_sentences = int(0.3*size)
            
        if request.form['submit_button'] == 'Summarize':
            pass
            cosineTextRank(os.path.join(app.config['UPLOAD_FOLDER'],filename),no_of_sentences)
            return send_from_directory(app.config['DOWNLOAD_FOLDER'], 'cos_textrank.txt')
                  
    return render_template('summarygenerator.html')

@app.route('/algorithmanalysis')
def algorithmanalysis():
	return render_template('algorithmanalysis.html')


@app.route('/algorithmanalysis', methods=['GET','POST'])
def upload_file1():
    if request.method == 'POST':                  #check if the post request has the file part
        if 'file' not in request.files:
            #flash('No file')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            #flash('No file selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)   
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))                      #save file at given location
            #flash('File uploaded successfully')
       
        with open(os.path.join(app.config['UPLOAD_FOLDER'], filename), "r",encoding="utf-8") as inFile:
            data = inFile.read()
                
        sentences = []
        sentences = sent_tokenize(data)
            
        size = len(sentences)
        if(size<30):
            flash('Small input...Select another file')
            return redirect(request.url)
        
        if request.form['submit_button'] == 'TextRank based on Sentence Overlap':
            pass
            simTextRank(os.path.join(app.config['UPLOAD_FOLDER'],filename),10)
            return send_from_directory(app.config['DOWNLOAD_FOLDER'], 'sim_textrank.txt')
        
        elif request.form['submit_button'] == 'TextRank based on Sentence Position':
            pass
            posTextRank(os.path.join(app.config['UPLOAD_FOLDER'],filename),10,5)
            return send_from_directory(app.config['DOWNLOAD_FOLDER'], 'pos_textrank.txt')
        
        elif request.form['submit_button'] == 'TextRank with Cosine Similarity':
            pass
            cosineTextRank(os.path.join(app.config['UPLOAD_FOLDER'],filename),10)
            return send_from_directory(app.config['DOWNLOAD_FOLDER'], 'cos_textrank.txt')
        
        else:
            pass
            jaccardTextRank(os.path.join(app.config['UPLOAD_FOLDER'],filename),10)
            return send_from_directory(app.config['DOWNLOAD_FOLDER'], 'jaccard_textrank.txt')
                  
    return render_template('algorithmanalysis.html')



if __name__ == "__main__":
    app.run(debug=True)

