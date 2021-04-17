from flask import Flask, render_template, request, jsonify
import os.path
import model
import parameters

app = Flask(__name__)
ALLOWED_EXTENSIONS = {"csv", "xls", "xlsx", "xlsm", "xlsb", "odf", "ods", "odt"}


@app.route('/')
def hello_world():
    return render_template('main.html', **{
        "model": model,
        "parameters": parameters,
        "enumerate": enumerate})


@app.route('/batch', methods=['POST'])
def batch_handler():
    file = request.files['batchInputFile']
    app.logger.debug("Mime-Type: %s; params: %s", file.mimetype, file.mimetype_params)
    if file.filename == '':
        return jsonify({"ok": False, "err": "Empty File"})

    ext = os.path.splitext(file.filename)[1][1:].lower()
    app.logger.debug("File name extension: %s", ext)
    if ext not in ALLOWED_EXTENSIONS:
        return jsonify({"ok": False, "err": "Bad file extension"})

    result = model.process_batch(file, request.form)

    return jsonify({"ok": True, "data": result})


@app.route('/single', methods=['POST'])
def manual_handler():
    result = model.process_single(request.form)
    return jsonify({"ok": True, "data": result})


if __name__ == '__main__':
    app.run()
