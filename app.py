from flask import Flask, render_template, request
import os

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"

@app.route("/", methods=["GET", "POST"])
def upload():
    msg = ""

    if request.method == "POST":
        file = request.files["file"]
        if file:
            path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(path)
            msg = "File yuklandi ✅"

    return render_template("upload.html", msg=msg)

if __name__ == "__main__":
    app.run(debug=True)
