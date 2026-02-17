import os
from flask import Flask, request, render_template, redirect, url_for, send_from_directory, flash
from werkzeug.utils import secure_filename
from tasks import process_pdf, celery
from config import UPLOAD_FOLDER, RESULT_FOLDER, BASE_DIR

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

ALLOWED_EXT = {'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXT

app = Flask(__name__)
app.secret_key = 'replace-with-a-secure-key'

@app.route("/", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        if 'file' not in request.files:
            flash("Aucun fichier")
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash("Aucun fichier sélectionné")
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            save_path = os.path.join(UPLOAD_FOLDER, filename)
            file.save(save_path)
            # lancer tâche asynchrone
            task = process_pdf.delay(filename)
            return redirect(url_for('status', task_id=task.id))
    return render_template('upload.html')

@app.route("/status/<task_id>")
def status(task_id):
    res = celery.AsyncResult(task_id)
    info = {
        "state": res.state,
        "result": res.result
    }
    docx_link = None
    if res.successful() and res.result and 'docx' in res.result:
        docx_link = url_for('download_result', filename=res.result['docx'])
    return render_template('status.html', info=info, docx_link=docx_link, task_id=task_id)

@app.route("/download/<filename>")
def download_result(filename):
    return send_from_directory(RESULT_FOLDER, filename, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
