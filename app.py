from flask import Flask, render_template, request
from summary import summarizer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    try:
        rawtext = request.form['rawtext']
        print("Received text for summarization:", rawtext)
        summary, original, len_orig, len_summ = summarizer(rawtext)
        print("Summary generated:", summary)
        return render_template('summary.html', summary=summary, original=original, len_orig=len_orig, len_summ=len_summ)
    except Exception as e:
        print("Error:", e)
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
