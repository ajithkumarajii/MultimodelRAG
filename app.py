from flask import Flask, request, redirect, url_for, render_template, session
from werkzeug.utils import secure_filename
import os
from utils.pdf_processor import parse_pdf
from utils.model_utils import process_text, process_images, process_query
from utils.display_utils import generate_response

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'pdf'}

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files.get('file')
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            session['pdf_path'] = filepath
            text_content, image_list = parse_pdf(filepath)
            process_text(text_content)
            process_images(image_list)
            
            return redirect(url_for('query_page'))
    
    return render_template('upload.html')

@app.route('/query', methods=['GET', 'POST'])
def query_page():
    if request.method == 'POST':
        query = request.form.get('query')
        if query:
            pdf_path = session.get('pdf_path')
            if not pdf_path:
                return redirect(url_for('upload_file'))
            
            relevant_text, relevant_images = process_query(query)
            relevant_images = [f"{os.path.basename(pdf_path).replace('.pdf', '_images/')}{os.path.basename(img)}" for img in relevant_images]
            response = generate_response(query, relevant_text, relevant_images)
            return render_template('query.html', query=response, relevant_text=relevant_text, relevant_images=relevant_images)
    
    if 'pdf_path' not in session:
        return redirect(url_for('upload_file'))
    
    return render_template('query.html')

if __name__ == '__main__':
    app.run(debug=True)