from flask import render_template
import sys
                          
sys.path.append("./")  

from app import app

@app.route('/')
def home():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)