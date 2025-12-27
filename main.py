import yt_dlp
from flask import Flask,request,render_template
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def home():
	if request.method == "POST":
		user_input = request.form.get("user_input")
		try :
			downloader(user_input)
			status = f"Successfully downloaded: {user_input}"
		except Exception as e:
			status = f"error {e}"
		return render_template("home.html", status=status)
	return render_template("home.html")
def downloader(name):
	#error handling so the program won't crash if the user puts a wrong song name'
	try:
		#yt_dlp options doesn't matter'
		ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s',
    'postprocessors': [{ 
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'quiet': True
}
		with yt_dlp.YoutubeDL(ydl_opts) as ydl:
			ydl.download([f"ytsearch:{name}"])
	#if the video wasn't found for some reason'
	except yt_dlp.utils.DownloadError as e:
			return
if __name__ == "__main__":
	app.run(debug=False)