from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>Python CI/CD App</title>
        </head>
        <body style="
            background: linear-gradient(to right, #4facfe, #00f2fe);
            font-family: Arial, sans-serif;
            text-align: center;
            color: white;
            margin-top: 200px;
        ">
            <h1>🚀 Welcome to the Python CI/CD Web App!</h1>
            <p>This Flask app is deployed through a Jenkins CI/CD pipeline.</p>
            <button style="
                background-color: white;
                color: #007BFF;
                border: none;
                padding: 10px 20px;
                border-radius: 8px;
                font-size: 16px;
                cursor: pointer;
                margin-top: 20px;
            " 
            onmouseover="this.style.backgroundColor='#e6e6e6';"
            onmouseout="this.style.backgroundColor='white';">
                Learn More
            </button>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
