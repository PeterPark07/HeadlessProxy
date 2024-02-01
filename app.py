from flask import Flask, Response
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from setup import chrome_destination

app = Flask(__name__)

# Configure Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
    
# Set the paths for Chrome and Chromedriver
chrome_options.binary_location = chrome_destination
    

def render_page(url):
    # Create Chrome webdriver instance
    driver = webdriver.Chrome(options=chrome_options)
    
    driver.get(url)
    rendered_page = driver.page_source
    
    driver.quit()
    
    return rendered_page

@app.route('/<path:url>')
def proxy(url):
    try:
        rendered_page = render_page(url)
        return Response(rendered_page, content_type='text/html')
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
