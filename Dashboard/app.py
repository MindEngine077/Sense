from flask import Flask, request, render_template, jsonify
import requests
from bs4 import BeautifulSoup
from supabase import create_client, Client
import os



# Supabase setup
SUPABASE_URL = "https://jkejzpsklzxxtzyxgvmn.supabase.co"
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImprZWp6cHNrbHp4eHR6eXhndm1uIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDAyMzM2OTgsImV4cCI6MjA1NTgwOTY5OH0.h5IgUumf9uPFqq8haW6tgKZXeiIbhxOijWj2UTtUaRE")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/crawl', methods=['POST'])
def run_crawler():
    """ Crawlt een website en slaat data op in Supabase """
    data = request.json
    url = data.get("url", "https://news.ycombinator.com")

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Pas dit aan naar jouw website!
    articles = soup.select("a.storylink") or soup.select("h2 a")

    crawled_data = []
    for article in articles:
        try:
            supabase.table("crawldata").insert({"title": title, "url": link}).execute()
        except Exception as e:
            return jsonify({"message": "Database error", "error": str(e)}), 500
        link = article.get('href')

        # Opslaan in Supabase
        supabase.table("crawldata").insert({"title": title, "url": link}).execute()
        crawled_data.append({"title": title, "url": link})

    return jsonify({"message": "Crawl voltooid!", "data": crawled_data})

@app.route('/crawldata', methods=['GET'])
def get_crawldata():
    """ Haalt crawldata op uit Supabase """
    response = supabase.table("crawldata").select("*").execute()
    debug_mode = os.getenv("FLASK_DEBUG", "False").lower() in ['true', '1', 't']
    app.run(debug=debug_mode)

if __name__ == '__main__':
    app.run(debug=True)
