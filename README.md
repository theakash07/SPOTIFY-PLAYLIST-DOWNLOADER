# Spotify Playlist Downloader

A simple Flask-based web application that allows users to download Spotify playlists as a ZIP file of songs. The application uses `spotdl` to handle the downloading process and provides a clean and interactive interface.

![Spotify Playlist Downloader](https://via.placeholder.com/1200x400)  

## Features
- Input Spotify playlist URL to download the entire playlist.
- Automatically zips downloaded songs for easy sharing.
- Interactive user interface with a responsive design.
- Displays download progress and error messages.

## How It Works
1. User enters the Spotify playlist URL in the provided input field.
2. The app uses `spotdl` to download songs from the playlist.
3. Downloads are compressed into a ZIP file and made available for download.

## Requirements
- Python 3.7+
- Flask
- spotdl
- Bootstrap (for frontend)

## Installation

### Clone the Repository
```bash
git clone https://github.com/yourusername/spotify-playlist-downloader.git
cd spotify-playlist-downloader
```

### Install Dependencies
```bash
pip install flask spotdl werkzeug
```

## Usage
1. Start the Flask server:
```bash
python app.py
```

2. Open your browser and navigate to `http://localhost:5000`.

3. Enter a Spotify playlist URL and click `Download Playlist`.

## Deployment
To deploy this application, use platforms like:

- **Heroku**
- **AWS EC2**
- **Google Cloud**

Note: This app cannot be hosted on GitHub Pages, as it requires a Python backend to function.

## Contributing
Contributions are welcome! Please create a pull request with your changes or improvements.

## Author
**Akash Kumar**  
For inquiries, contact [THEAKASH.EDUCATION07@GMAIL.COM](mailto:THEAKASH.EDUCATION07@GMAIL.COM)

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments
- **spotdl** for the core functionality.
- **Bootstrap** for frontend styling.

