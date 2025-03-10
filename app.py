from flask import Flask, render_template, jsonify
import speedtest

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/speedtest')
def run_speedtest():
    try:
        st = speedtest.Speedtest()

        download_speed = round(st.download() / 1_000_000, 2)  # Convert to Mbps
        upload_speed = round(st.upload() / 1_000_000, 2)  # Convert to Mbps
        ping = round(st.results.ping, 2)

        print(f"Download: {download_speed} Mbps, Upload: {upload_speed} Mbps, Ping: {ping} ms")  # Debugging
        return jsonify({"download": download_speed, "upload": upload_speed, "ping": ping})

    except Exception as e:
        print(f"Error: {str(e)}")  # Debugging
        return jsonify({"error": "Speed test failed"}), 500


if __name__ == "__main__":
    app.run(debug=True)
