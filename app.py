from flask import Flask, request, render_template, send_file
import re
from io import BytesIO

# === your kanji_to_number() and adjust_timings() goes here ===
# paste the entire fixed logic here from your latest script

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["file"]
        if file and file.filename.endswith(".srt"):
            srt_text = file.read().decode("utf-8")
            adjusted = adjust_timings(srt_text)
            buffer = BytesIO()
            buffer.write(adjusted.encode("utf-8"))
            buffer.seek(0)
            return send_file(buffer, as_attachment=True, download_name="fixed_output.srt", mimetype="text/plain")
    return render_template("index.html")
