from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/generate', methods=['POST'])
def generate():

    brand = request.form['brand']
    industry = request.form['industry']
    objective = request.form['objective']
    product = request.form['product']

    industry = industry.lower()

    # Brand voice logic
    if industry in ["technology", "tech"]:
        voice = ["Premium and innovative", "Modern communication", "Feature focused"]

    elif industry in ["sports", "fitness"]:
        voice = ["Energetic", "Motivational", "Performance driven"]

    elif industry in ["food", "restaurant"]:
        voice = ["Fun", "Casual", "Taste focused"]

    else:
        voice = ["Professional", "Engaging", "Customer focused"]

    # Tweet templates
    templates = [
        f"Introducing the new {product} from {brand}! Experience the future.",
        f"Upgrade your lifestyle with {brand}'s {product}.",
        f"Why settle for less? Try {brand}'s {product}.",
        f"The wait is over! {brand} launches {product}.",
        f"Discover innovation with {brand}'s {product}.",
        f"{brand} is redefining the {industry} industry.",
        f"Take the next step with {brand}'s {product}.",
        f"Smarter. Faster. Better. That's {brand}.",
        f"Your next favorite {product} is here.",
        f"Step into the future with {brand}."
    ]

    tweets = random.sample(templates, 10)

    return render_template("result.html", voice=voice, tweets=tweets)

if __name__ == '__main__':
    app.run(debug=True)
