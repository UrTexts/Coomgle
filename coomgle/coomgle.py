from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def google_search(query, api_key, cx):
    """Perform a Google search using the Google Custom Search API."""
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={api_key}&cx={cx}"
    response = requests.get(url)
    if response.status_code == 200:  # Check if the request was successful
        return response.json()  # Return the search results as a JSON object
    else:
        print(f"Error: {response.status_code}")
        return None

@app.route('/', methods=['GET', 'POST'])
def home():
    results = None
    if request.method == 'POST':
        query = request.form['query']
        api_key = 'AIzaSyBv19wtlCwZtS6JZ3GgYwaWx6V_O47CBsc'  # Replace with your actual Google API key
        cx = '9684bfef8b5df4ec0'  # Replace with your Custom Search Engine ID
        results = google_search(query, api_key, cx)
    return render_template('index.html', results=results)

if __name__ == "__main__":
    app.run(debug=True)
