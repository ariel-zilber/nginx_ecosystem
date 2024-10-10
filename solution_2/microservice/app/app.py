from flask import Flask, send_file, abort
import os
import json
import os

app = Flask(__name__)
import requests

def download_image_if_not_exists(image_url,image_path):
    # Extract the image filename from the URL
    image_name = image_url.split("/")[-1]

    # Check if the image already exists in the tmp directory
    if os.path.exists(image_path):
        print(f"Image already exists at {image_path}")
        return image_path
    else:
        # Download the image and save it to the tmp directory
        try:
            response = requests.get(image_url)
            response.raise_for_status()  # Check if the request was successful
            with open(image_path, 'wb') as img_file:
                img_file.write(response.content)
            print(f"Downloaded image and saved to {image_path}")
            return image_path
        except requests.exceptions.RequestException as e:
            print(f"Failed to download image: {e}")
            return None

# Load configuration from a JSON file
def load_config():
    config_path = 'config.json'
    if os.path.exists(config_path):
        with open(config_path, 'r') as config_file:
            return json.load(config_file)
    else:
        raise FileNotFoundError(f"Configuration file '{config_path}' not found.")

# Load the configuration at startup
animal_config = load_config()
INSTANCE_ID = os.getenv('INSTANCE_ID')
download_image_if_not_exists(animal_config[INSTANCE_ID]["image"],f"/tmp/{animal_config[INSTANCE_ID]['name']}.png")

@app.route('/animal_name')
def animal_name():
    return animal_config[INSTANCE_ID]["name"]


@app.route('/animal_sound')
def animal_sound():
    return animal_config[INSTANCE_ID]["sound"]


@app.route('/animal_image')
def animal_image():
    return send_file(f"/tmp/{animal_config[INSTANCE_ID]['name']}.png", mimetype='image/jpeg')


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
