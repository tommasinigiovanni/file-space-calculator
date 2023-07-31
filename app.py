from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Set default quantities
    quantities = {
        'Photos': 1000,
        'Videos': 120,  # 2 hours default
        'MP3s': 1000,
        'Documents': 10000,
        'PowerPoints': 500
    }

    total_space = 0
    if request.method == 'POST':
        quantities = {
            'Photos': int(request.form.get('photos', quantities['Photos'])),
            'Videos': int(request.form.get('videos', quantities['Videos'])),
            'MP3s': int(request.form.get('mp3s', quantities['MP3s'])),
            'Documents': int(request.form.get('docs', quantities['Documents'])),
            'PowerPoints': int(request.form.get('ppts', quantities['PowerPoints']))
        }

        # Assumptions
        sizes_mb = {
            'Photos': 5,  # average size of photos in MB
            'Videos': 12, # average size of videos in MB per minute
            'MP3s': 5,  # average size of mp3s in MB per 5 minute song
            'Documents': 0.1,  # average size of documents in MB
            'PowerPoints': 2  # average size of PowerPoints in MB
        }

        total_space = sum(quantities[item]*sizes_mb[item] for item in quantities) / 1024  # calculate total space in GB
        total_space = round(total_space, 2)  # round to 2 decimal places

    return render_template('index.html', quantities=quantities, total_space=total_space)

if __name__ == '__main__':
    app.run(debug=True)

