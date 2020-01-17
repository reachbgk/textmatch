from flask import Flask, request, render_template
import string


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/match_text', methods=['GET', 'POST'])
def match_text_post():
    if request.method == 'POST':
#get form inputs	
        input_text1 = request.form['input_text1']
        input_text2 = request.form['input_text2']
        match_type = request.form['match_type']

#Exact match
        if match_type == "exact_match":
            if input_text1 == input_text2:
                match_score = "1"
#Ignore Case				
            else:
                match_score = "0" 
        elif match_type == "exact_match_no_case":
            if input_text1.lower() == input_text2.lower():
                match_score = "1"
            else:
                match_score = "0"
#Ignore punctuation				
        elif match_type == "match_words_only":
            input_text1 = input_text1.translate(str.maketrans('', '', string.punctuation))
            input_text2 = input_text2.translate(str.maketrans('', '', string.punctuation))
            if input_text1.lower() == input_text2.lower():
                match_score = "1"
            else:
                match_score = "0"	
        
		
    return render_template('index.html', 
	                        match_score = match_score)

if __name__ == '__main__':
    app.run(debug=True,port=9015)