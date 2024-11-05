# app.py (create this in the root directory, same level as the portfolio folder)
from portfolio import app

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)