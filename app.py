from flask import Flask
import os
import datetime
import psutil

app = Flask(__name__)

def get_top_output():
    try:
        return os.popen("top -b -n 1 | head -20").read()
    except:
        return "Error retrieving top output"

@app.route('/htop')
def htop():
    name = "Sriya Rao Muthyala"
    username = os.getenv("USER") or os.getenv("USERNAME") or "Unknown"
    server_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S IST")
    top_output = get_top_output()

    return f"""
    <html>
    <body>
        <h1>System Info</h1>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time (IST):</strong> {server_time}</p>
        <pre>{top_output}</pre>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
