from flask import Flask, Response
from selenium import webdriver
from setup import chromedriver_destination

app = Flask(__name__)

def render_page(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    
    # Adjust the path to your chromedriver executable
    driver = webdriver.Chrome(executable_path=chromedriver_destination, options=options)
    
    driver.get(url)
    rendered_page = driver.page_source
    
    driver.quit()
    
    return rendered_page

@app.route('/proxy/<path:url>')
def proxy(url):
    try:
        rendered_page = render_page(url)
        return Response(rendered_page, content_type='text/html')
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
