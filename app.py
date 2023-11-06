import psutil
#retrieving information on running processes and system utilization

from flask import Flask, render_template

app = Flask(__name__) 
#name of the app _name_

#setting path
@app.route("/") 
#"/"run on home path
#wheever user comes in at the home path,app is going to run

def index():
    cpu_percent = psutil.cpu_percent(interval=0.5)
    mem_precent = psutil.virtual_memory().percent
    Message = None
    if cpu_percent >= 80 or mem_precent >= 80:
        Message = "High usage of CPU and Memory Detected."
    return render_template("index.html",cpu_percent=cpu_percent,mem_precent=mem_precent,message=Message)

if __name__ == '__main__':
    app.run(debug=True, host = '0.0.0.0')