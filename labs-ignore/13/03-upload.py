from flask import Flask, request, flash, session, url_for, send_from_directory, redirect, render_template
import os
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.secret_key = "123abc"

APPROVED_EXT = set(['png', 'jpg', 'jpeg'])
UPLOAD_FOLDER = 'static/uploads'


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in APPROVED_EXT


@app.route('/')
def index():
    files = [os.path.join(UPLOAD_FOLDER, f) for f in os.listdir(UPLOAD_FOLDER)]
    return render_template('upload_view.html', files=files)


@app.route('/upload', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('no file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('no selected file')
            return redirect(request.url)
        if not allowed_file(file.filename):
            flash('file type not allowed')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_FOLDER, filename))
            flash('File "{}" successfully uploaded'.format(filename))
            return redirect(url_for('index'))
    return render_template('upload.html')


@app.route('/download/<filename>')
def download_file(filename):
    print(filename)
    return send_from_directory(UPLOAD_FOLDER,
                               filename)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
