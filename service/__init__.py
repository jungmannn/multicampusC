from flask import Flask, render_template, request, redirect, url_for, session, make_response, jsonify
from service.model import insertBbsData, searchInPlaystore, searchInAppstore
import os 

def createApp():
    app = Flask(__name__)
    # 1. 세션키 생성 => 통상 값은 해쉬값(중복되지 않는 임의값)사용
    initRoute( app )
    return app
def initRoute(app):
    @app.route('/')
    def home():
        return render_template("index.html")

    # POST 전용
    @app.route('/search', methods=['POST'])
    def search():
        info = dict()
        info['points']   = request.form.get('points')
        info['type']     = request.form.get('type')
        info['category'] = request.form.get('category')
        info['rating']   = request.form.get('rating')
        rows = searchInPlaystore( info )
        print(rows)
        if not rows:
            rows = "결과 없음"
        return render_template("search.html", rows= rows)
    if __name__ == '__main__':
        app.run(debug=True)
    
    @app.route('/search2', methods=['POST'])
    def search2():
        info = dict()
        info['points']   = request.form.get('points')
        info['type']     = request.form.get('type')
        info['category'] = request.form.get('category')
        info['rating']   = request.form.get('rating')
        rows = searchInAppstore( info )
        print(rows)
        if not rows:
            rows = "{}" 
        return render_template("search2.html", rows= rows)
        
    @app.route('/chart', methods=['POST'])
    def chart():
        info = dict()
        info['category'] = request.form.get('category')
        return render_template("chart.html", info= info)
    if __name__ == '__main__':
        app.run(debug=True)
    @app.route('/predict')
    def predict():
        return render_template("predictionModel.html")
    if __name__ == '__main__':
        app.run(debug=True)