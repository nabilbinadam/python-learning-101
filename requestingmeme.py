# app.py
from flask import Flask, jsonify
import requests 


app = Flask(__name__)

@app.route('/memelist',methods=['GET'])
def getMeme():
    url="https://api.imgflip.com/get_memes"

    try:
        response=requests.get(url)
        response.raise_for_status()

        meme_data=response.json()

        return jsonify(meme_data)



    except requests.exceptions.RequestException as e:
        # Handle any errors that occur during the request
        return jsonify({"error": str(e)}), 500
   
if __name__ == '__main__':
    app.run(debug=True)