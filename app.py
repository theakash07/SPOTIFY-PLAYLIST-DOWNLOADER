from flask import Flask, render_template, request, jsonify, send_file
import os
import subprocess
import shutil
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Directory to store downloaded songs
download_folder = "downloads"
os.makedirs(download_folder, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_playlist():
    spotify_url = request.form.get('url')

    if not spotify_url:
        return jsonify({"error": "No URL provided."}), 400

    try:
        # Generate a secure filename for the playlist
        playlist_name = secure_filename(spotify_url.split('/')[-1])
        output_folder = os.path.join(download_folder, playlist_name)
        os.makedirs(output_folder, exist_ok=True)

        # Use spotdl to download the playlist
        subprocess.run(
            ["spotdl", spotify_url, "--output", output_folder], check=True
        )

        # Zip the downloaded songs using shutil
        zip_file = f"{output_folder}.zip"
        shutil.make_archive(output_folder, 'zip', output_folder)

        # Return the zip file for download
        return send_file(zip_file, as_attachment=True)

    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Failed to download playlist: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
