# app.py

from flask import Flask, request, redirect, url_for, render_template, send_from_directory
import os
from filter_duplicate_lines import remove_duplicates, remove_extra_empty_lines

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['PROCESSED_FOLDER'] = 'processed'

# Ensure upload and processed directories exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['PROCESSED_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    error = request.args.get('error', None)
    # Clear the error message when rendering the template
    return render_template('index.html', error=error)

@app.route('/upload', methods=['POST'])
def upload_file():
    text = request.form.get('text', None)
    file = request.files.get('file', None)

    if not text and not file:
        error = 'You must paste text or choose a file before uploading.'
        return redirect(url_for('index', error=error))

    if text:
        # Save text to a temporary file
        text_file = os.path.join(app.config['UPLOAD_FOLDER'], 'pasted_text.txt')
        with open(text_file, 'w', encoding='utf-8', newline='\n') as f:
            f.write(text)
        input_file_path = text_file
        
    else:
        if file.filename == '':
            error = 'Please choose a file to upload.'
            return redirect(url_for('index', error=error))
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)
        input_file_path = file_path

    intermediate_file = os.path.join(app.config['PROCESSED_FOLDER'], 'dups_removed.txt')
    final_output_file = os.path.join(app.config['PROCESSED_FOLDER'], 'cleaned_output.txt')

    # Process the file or pasted text
    remove_duplicates(input_file_path, intermediate_file)
    remove_extra_empty_lines(intermediate_file, final_output_file)

    return redirect(url_for('download_file', filename='cleaned_output.txt'))

@app.route('/processed/<filename>')
def download_file(filename):
    return send_from_directory(app.config['PROCESSED_FOLDER'], filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
