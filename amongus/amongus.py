from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def index():
  # Generate a random color.
  color = random.choice(["red", "green", "blue", "yellow", "purple"])

  # Create the HTML for the square.
  html = """
  <html>
    <head>
      <title>My Website</title>
    </head>
    <body>
      <div style="width: 100px; height: 100px; background-color: {color};"></div>
    </body>
  </html>
  """.format(color=color)
host_name = socket.gethostname()
ip_address = socket.gethostbyname(host_name)
print(ip_address)

  # Return the HTML.
  return html

if __name__ == "__main__":
  app.run(debug=True)
